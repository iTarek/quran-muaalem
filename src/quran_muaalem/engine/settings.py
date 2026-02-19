from typing import Literal
from pydantic_settings import BaseSettings, SettingsConfigDict
import torch


class Settings(BaseSettings):
    # Model configuration
    model_name_or_path: str = "obadx/muaalem-model-v3_2"
    dtype: Literal["float32", "float16", "bfloat16"] = "bfloat16"

    # Batching configuration
    max_batch_size: int = 32
    batch_timeout: float = 0.4  # seconds

    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    accelerator: Literal["cuda", "cpu", "mps"] = "cuda"
    devices: int = 1

    # Additional LitServer options
    workers_per_device: int = 1
    timeout: float = 30.0  # request timeout in seconds

    @property
    def torch_dtype(self) -> torch.dtype:
        """Convert dtype string to torch.dtype."""
        mapping = {
            "float32": torch.float32,
            "float16": torch.float16,
            "bfloat16": torch.bfloat16,
        }
        return mapping[self.dtype]
