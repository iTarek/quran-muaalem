# مسار الرسم الصوتي

يعتمد المعلّم القرآني على `quran-transcript` لبناء المرجع الصوتي لكل مقطع. الواجهة وواجهة البرمجة تقومان بذلك قبل الاستدلال.

في `src/quran_muaalem/gradio_app.py`:

- `Aya(...).get_by_imlaey_words(...)` يحدد المقطع المطلوب.
- `quran_phonetizer(uthmani_ref, current_moshaf, remove_spaces=True)` يحول النص إلى رسم صوتي.
- هذا الرسم يمر إلى `Muaalem.__call__` مع الصوت.

بالتالي **المرجع الصوتي مطلوب** للاستدلال. لمزيد من التفاصيل عن بناء الرسم الصوتي راجع قسم Quran Transcript.
