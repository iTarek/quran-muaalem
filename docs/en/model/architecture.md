# Architecture

The repo includes a figure for the multi-level CTC design:

![Multi-level CTC](/figures/mutli-level-ctc.png)

The core model class is `Wav2Vec2BertForMultilevelCTC` in `src/quran_muaalem/modeling/modeling_multi_level_ctc.py`. The inference wrapper ties together:

- `AutoFeatureExtractor` (input features)
- `MultiLevelTokenizer` (reference tokenization)
- `Wav2Vec2BertForMultilevelCTC` (multi-level logits)
- Decoders in `src/quran_muaalem/decode.py`
