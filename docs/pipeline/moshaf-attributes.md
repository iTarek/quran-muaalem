# خصائص المصحف

التحويل الصوتي يتحكم به كائن `MoshafAttributes` الموجود في `quran-transcript/src/quran_transcript/phonetics/moshaf_attributes.py`. وهو `pydantic.BaseModel` يحتوي على خيارات قرائية عديدة (مدود، تكبير، وغيرها).

## كيف تستخدمه الواجهة

في `src/quran_muaalem/gradio_app.py`:

- `REQUIRED_MOSHAF_FIELDS` يحدد الحقول الظاهرة في الواجهة.
- `create_gradio_input_for_field(...)` يبني عناصر الإدخال من `MoshafAttributes.model_fields`.
- `get_arabic_name(...)` و `get_arabic_attributes(...)` (من `quran_transcript.phonetics.moshaf_attributes`) تضيفان تسميات عربية للحقول.

للاطلاع على القائمة الكاملة والافتراضيات، افتح:

- `quran-transcript/src/quran_transcript/phonetics/moshaf_attributes.py`

ولإظهار حقول إضافية في الواجهة، أضفها إلى `REQUIRED_MOSHAF_FIELDS` في `src/quran_muaalem/gradio_app.py`.
