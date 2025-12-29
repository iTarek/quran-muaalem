# Model Overview

The model wrapper lives in `src/quran_muaalem/inference.py` and loads a multi-level CTC architecture (`Wav2Vec2BertForMultilevelCTC`). The model is configured via:

- `model_name_or_path` (default: `obadx/muaalem-model-v3_2`)
- `dtype` (default: `torch.bfloat16`)
- `device` (CPU or CUDA)

The model outputs logits for multiple levels. Decoding is handled in `src/quran_muaalem/decode.py`.
