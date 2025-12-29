# نظرة عامة على النموذج

التغليف الخاص بالنموذج موجود في `src/quran_muaalem/inference.py` ويحمّل معمارية CTC متعددة المستويات (`Wav2Vec2BertForMultilevelCTC`). أهم الإعدادات:

- `model_name_or_path` (الافتراضي: `obadx/muaalem-model-v3_2`)
- `dtype` (الافتراضي: `torch.bfloat16`)
- `device` (CPU أو CUDA)

المخرجات متعددة المستويات تُفك عبر `src/quran_muaalem/decode.py`.
