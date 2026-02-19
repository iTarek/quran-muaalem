from pydantic import Field
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    engine_url: str = Field(
        default="http://0.0.0.0:8000/predict",
        description="URL of the Quran Muaalem engine predict endpoint.",
    )
    host: str = Field(
        default="0.0.0.0",
        description="Bind address for the server.",
    )
    port: int = Field(
        default=8001,
        description="Port number to listen on.",
        ge=1,
        le=65535,
    )
    error_ratio: float = Field(
        default=0.1,
        description="Maximum allowed Levenshtein distance as a fraction of query length.",
        ge=0.0,
        le=1.0,
    )
    max_workers: int = Field(
        default=4,
        description="Number of worker processes for phonetic search executor.",
        ge=1,
    )
