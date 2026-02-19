from pydantic import BaseModel, Field


class SearchResultResponse(BaseModel):
    """Result of a phonetic search match."""

    sura_idx: int = Field(description="Sura number (1-114)")
    aya_idx: int = Field(description="Aya number within the sura")
    uthmani_word_idx: int = Field(
        description="0-based index of the word within the aya"
    )
    uthmani_char_idx_start: int = Field(
        description="0-based start character index within the word"
    )
    uthmani_char_idx_end: int = Field(
        description="0-based end character index within the word (exclusive)"
    )
    phonemes_idx_start: int = Field(
        description="0-based start index in phoneme sequence"
    )
    phonemes_idx_end: int = Field(
        description="0-based end index in phoneme sequence (exclusive)"
    )
    uthmani_text: str = Field(description="Matched Uthmani text snippet")


class SearchResponse(BaseModel):
    """Response from the search/voice endpoint."""

    phonemes: str = Field(description="Phonetic representation of the input audio")
    results: list[SearchResultResponse] = Field(description="List of search results")
    message: str | None = Field(
        default=None, description="Optional message (e.g., no results found)"
    )
