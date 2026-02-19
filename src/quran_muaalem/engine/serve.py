import io
import time

import librosa
import torch
import litserve as ls
from transformers import AutoFeatureExtractor
import numpy as np

from ..modeling.modeling_multi_level_ctc import Wav2Vec2BertForMultilevelCTC


class QuranMuaalemAPI(ls.LitAPI):
    def __init__(
        self,
        model_name_or_path: str = "obadx/muaalem-model-v3_2",
        dtype: torch.dtype = torch.bfloat16,
        max_audio_seconds: float = 15,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.model_name_or_path = model_name_or_path
        self.dtype = dtype
        self.max_audio_seconds = max_audio_seconds
        self.sampling_rate = 16000
        self.max_features = int(
            np.ceil((self.sampling_rate * self.max_audio_seconds - 400) / (160 * 2))
        )

    def setup(self, device):
        self.device = device
        self.processor = AutoFeatureExtractor.from_pretrained(self.model_name_or_path)
        self.model = Wav2Vec2BertForMultilevelCTC.from_pretrained(
            self.model_name_or_path
        )
        self.model.to(device, dtype=self.dtype)
        self.model.eval()

    def decode_request(self, request):
        audio_file = request["file"]
        audio_bytes = audio_file.file.read()

        audio_array, sr = librosa.load(
            io.BytesIO(audio_bytes),
            sr=self.sampling_rate,
            mono=True,
            duration=self.max_audio_seconds,  # Truncating input speech to max_audio_seconds
        )

        features = self.processor(
            audio_array,
            sampling_rate=sr,
            return_tensors="pt",
            padding="max_length",
            max_length=self.max_features,
        )

        return {
            "input_features": features["input_features"],
            "attention_mask": features["attention_mask"],
        }

    def batch(self, inputs):
        input_features = torch.cat([inp["input_features"] for inp in inputs]).to(
            self.device, dtype=self.dtype
        )
        attention_mask = torch.cat([inp["attention_mask"] for inp in inputs]).to(
            self.device, dtype=self.dtype
        )
        return (input_features, attention_mask)

    def predict(self, x):
        input_features, attention_mask = x
        print("Shape")
        print(input_features.shape)
        with torch.inference_mode():
            level_to_logits = self.model(
                input_features, attention_mask, return_dict=False
            )[0]

        list_of_level_to_logits = []
        for idx in range(level_to_logits["phonemes"].shape[0]):
            d = {}
            for level in level_to_logits:
                d[level] = (
                    level_to_logits[level][idx]
                    .cpu()
                    .to(dtype=torch.float32)
                    .unsqueeze(0)
                )
            list_of_level_to_logits.append(d)

        return list_of_level_to_logits

    def unbatch(self, outputs):
        return outputs

    def encode_response(self, output):
        level_to_logits = output

        level_to_probs = {}
        for level, logits in level_to_logits.items():
            probs = torch.nn.functional.softmax(logits, dim=-1)
            level_to_probs[level] = probs

        phonemes_probs = level_to_probs["phonemes"]
        batch_probs, batch_ids = phonemes_probs.topk(1, dim=-1)

        return {"phonemes": batch_ids.tolist()}
