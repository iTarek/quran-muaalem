from typing import Optional, Literal

from pydantic import BaseModel, Field

from quran_transcript.phonetics.moshaf_attributes import MoshafAttributes

DEFAULT_MOSHAF = MoshafAttributes(
    rewaya="hafs",
    madd_monfasel_len=4,
    madd_mottasel_len=4,
    madd_mottasel_waqf=4,
    madd_aared_len=4,
)


class PhonemesSearchSpanApp(BaseModel):
    """Represents a position in the Uthmani Quran text (App version)."""

    sura_idx: int = Field(description="Sura number (1-114)")
    aya_idx: int = Field(description="Aya number within the sura")
    uthmani_word_idx: int = Field(
        description="0-based index of the word within the aya"
    )
    uthmani_char_idx: int = Field(description="0-based character index within the word")
    phonemes_idx: int = Field(description="0-based index in the phoneme sequence")


class SearchResultResponse(BaseModel):
    """Result of a phonetic search match."""

    start: PhonemesSearchSpanApp = Field(description="Start position of the match")
    end: PhonemesSearchSpanApp = Field(
        description="End position of the match (exclusive)"
    )
    uthmani_text: str = Field(description="Matched Uthmani text snippet")


class SearchResponse(BaseModel):
    """Response from the search/voice endpoint."""

    phonemes: str = Field(description="Phonetic representation of the input audio")
    results: list[SearchResultResponse] = Field(description="List of search results")
    message: str | None = Field(
        default=None, description="Optional message (e.g., no results found)"
    )


class ReciterErrorResponse(BaseModel):
    """Error in recitation analysis."""

    uthmani_pos: tuple[int, int] = Field(
        description="Position in Uthmani text (start, end)"
    )
    ph_pos: tuple[int, int] = Field(description="Position in phoneme text (start, end)")
    error_type: Literal["tajweed", "normal", "tashkeel"] = Field(
        description="Type of error: tajweed, normal, or tashkeel"
    )
    speech_error_type: Literal["insert", "delete", "replace"] = Field(
        description="Type of speech error"
    )
    expected_ph: str = Field(description="Expected phonetic text")
    preditected_ph: str = Field(description="Predicted phonetic text")
    expected_len: Optional[int] = Field(
        default=None, description="Expected length (for madd errors)"
    )
    predicted_len: Optional[int] = Field(
        default=None, description="Predicted length (for madd errors)"
    )


class CorrectRecitationResponse(BaseModel):
    """Response from the correct-recitation endpoint."""

    start: PhonemesSearchSpanApp = Field(description="Start position of the match")
    end: PhonemesSearchSpanApp = Field(
        description="End position of the match (exclusive)"
    )
    predicted_phonemes: str = Field(description="Phonetic text from audio prediction")
    reference_phonemes: str = Field(
        description="Reference phonetic text from Uthmani using MoshafAttributes"
    )
    uthmani_text: str = Field(description="Matched Uthmani text snippet")
    errors: list[ReciterErrorResponse] = Field(
        description="List of recitation errors found"
    )


class CorrectRecitationRequest(BaseModel):
    """Request body for correct-recitation endpoint."""

    moshaf: MoshafAttributes = Field(
        default=DEFAULT_MOSHAF, description="Moshaf attributes for phonetization"
    )
    error_ratio: float = Field(
        default=0.1,
        description="Maximum allowed Levenshtein distance as a fraction of query length.",
    )
