import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import Optional

import httpx
from fastapi import FastAPI, UploadFile, File, Query

from quran_transcript.phonetics.search import (
    PhoneticSearch,
    NoPhonemesSearchResult,
)

from .settings import AppSettings
from .types import SearchResponse, SearchResultResponse


app_settings = AppSettings()

app = FastAPI(title="Quran Muaalem Search API")

_executor: Optional[ThreadPoolExecutor] = None
_phonetic_search: Optional[PhoneticSearch] = None


def get_executor() -> ThreadPoolExecutor:
    global _executor
    if _executor is None:
        _executor = ThreadPoolExecutor(max_workers=app_settings.max_workers)
    return _executor


def get_phonetic_search() -> PhoneticSearch:
    global _phonetic_search
    if _phonetic_search is None:
        _phonetic_search = PhoneticSearch()
    return _phonetic_search


async def call_engine_predict(audio_file: UploadFile) -> str:
    audio_bytes = await audio_file.read()
    async with httpx.AsyncClient(timeout=30.0) as client:
        files = {"file": ("audio.wav", audio_bytes, "audio/wav")}
        response = await client.post(app_settings.engine_url, files=files)
        response.raise_for_status()
        data = response.json()
        return data["phonemes"]


def run_phonetic_search(
    phonemes: str, error_ratio: float
) -> tuple[list[SearchResultResponse], str | None]:
    ph_search = get_phonetic_search()
    try:
        results = ph_search.search(phonemes, error_ratio=error_ratio)
    except NoPhonemesSearchResult:
        return [], "No results found. Try increasing error_ratio."

    response_results = []
    for r in results:
        uthmani_text = ph_search.get_uthmani_from_result(r)
        response_results.append(
            SearchResultResponse(
                sura_idx=r.start.sura_idx,
                aya_idx=r.start.aya_idx,
                uthmani_word_idx=r.start.uthmani_word_idx,
                uthmani_char_idx_start=r.start.uthmani_char_idx,
                uthmani_char_idx_end=r.end.uthmani_char_idx,
                phonemes_idx_start=r.start.phonemes_idx,
                phonemes_idx_end=r.end.phonemes_idx,
                uthmani_text=uthmani_text,
            )
        )
    return response_results, None


@app.post("/search/voice", response_model=SearchResponse)
async def search_voice(
    file: UploadFile = File(...),
    error_ratio: float = Query(default=None),
):
    if error_ratio is None:
        error_ratio = app_settings.error_ratio

    phonemes = await call_engine_predict(file)

    loop = asyncio.get_event_loop()
    results, message = await loop.run_in_executor(
        get_executor(),
        run_phonetic_search,
        phonemes,
        error_ratio,
    )

    return SearchResponse(phonemes=phonemes, results=results, message=message)
