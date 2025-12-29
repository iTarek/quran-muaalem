# المعمارية

يتضمن المستودع شكلًا يوضح تصميم CTC متعدد المستويات:

![Multi-level CTC](/figures/mutli-level-ctc.png)

الفئة الأساسية هي `Wav2Vec2BertForMultilevelCTC` في `src/quran_muaalem/modeling/modeling_multi_level_ctc.py`. طبقة الاستدلال تربط بين:

- `AutoFeatureExtractor` لاستخراج الخصائص
- `MultiLevelTokenizer` لترميز المرجع
- `Wav2Vec2BertForMultilevelCTC` لإخراج اللوغيتس متعددة المستويات
- أدوات فك الشيفرة في `src/quran_muaalem/decode.py`
