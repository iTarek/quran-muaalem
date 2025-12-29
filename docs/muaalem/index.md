# نظرة عامة على المعلّم القرآني

المعلّم القرآني هو طبقة الاستدلال التي تقارن التلاوة بمرجع صوتي وتُخرج الفونيمات وخصائص التجويد. نقاط الدخول الأساسية:

- الفئة `Muaalem` في `src/quran_muaalem/inference.py`
- واجهة Gradio في `src/quran_muaalem/gradio_app.py`

## مسار الاستدلال الأساسي

داخل `Muaalem.__call__` في `src/quran_muaalem/inference.py`:

1. يتم ترميز المرجع الصوتي عبر `MultiLevelTokenizer`.
2. تُستخرج خصائص الصوت بـ `AutoFeatureExtractor` من `transformers`.
3. النموذج `Wav2Vec2BertForMultilevelCTC` ينفذ المرور الأمامي.
4. فك الشيفرة يتم عبر `phonemes_level_greedy_decode` و `multilevel_greedy_decode` في `src/quran_muaalem/decode.py`.
5. تُبنى خصائص كل مجموعة فونيمات داخل كائنات `Sifa` وتُعاد كـ `MuaalemOutput`.

هذا يعني أنك تمرر الصوت مع مرجع صوتي مُستخرج من `quran_transcript.quran_phonetizer`.

## ملفات أساسية

- `src/quran_muaalem/inference.py` — فئة النموذج ومسار الاستدلال.
- `src/quran_muaalem/decode.py` — منطق فك الشيفرة والمحاذاة.
- `src/quran_muaalem/muaalem_typing.py` — تعريفات المخرجات (`Unit`, `Sifa`, `MuaalemOutput`).
- `src/quran_muaalem/gradio_app.py` — واجهة المستخدم وإعدادات المصحف.
