# واجهة Gradio

مدخل الواجهة موجود في `src/quran_muaalem/gradio_app.py` ويُعرّف كسكربت طرفي باسم `quran-muaalem-ui` في `pyproject.toml`.

## ماذا تفعل الواجهة؟

أهم الدوال في `src/quran_muaalem/gradio_app.py`:

- `process_audio(...)` تقوم بتحميل الصوت (عبر `librosa.load`)، وبناء مرجع صوتي من `quran_phonetizer`، وتشغيل `Muaalem`، ثم إرجاع HTML.
- `update_uthmani_ref(...)` تجلب مقطع الرسم العثماني عبر `quran_transcript.Aya`.
- `create_gradio_input_for_field(...)` تُنشئ عناصر الإدخال بالاعتماد على حقول `MoshafAttributes`.

تشغيل الواجهة يتم في `main()` بهذا السطر:

```python
app.launch(server_name="0.0.0.0", share=True)
```

إذا أردت تغيير خيارات التشغيل (إلغاء المشاركة أو تحديد منفذ)، عدّل هذا الاستدعاء.

## تشغيل الواجهة

بعد تثبيت إضافات الواجهة:

```bash
pip install "quran-muaalem[ui]"
quran-muaalem-ui
```

السكربت `quran-muaalem-ui` يشير إلى `quran_muaalem.gradio_app:main` (انظر `pyproject.toml`).
