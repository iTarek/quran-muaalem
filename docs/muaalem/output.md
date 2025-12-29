# المخرجات والشرح

الاستدلال يُرجع قائمة من `MuaalemOutput` (`src/quran_muaalem/muaalem_typing.py`). كل عنصر يحتوي على:

- `phonemes`: كائن `Unit` مع نص الفونيمات، الاحتمالات، والمعرّفات.
- `sifat`: قائمة `Sifa` (عنصر لكل مجموعة فونيمات) مع خصائص اختيارية.

## مقارنة التوقع مع المرجع

هناك وحدتان لعرض النتائج:

- `src/quran_muaalem/explain.py` يعرض جدولًا في الطرفية باستخدام `rich`.
  - `explain_for_terminal(...)` يبني فرقًا بين الفونيمات المتوقعة والمرجع ثم يطبع جدولًا.
- `src/quran_muaalem/explain_gradio.py` يولّد HTML لواجهة Gradio.
  - `explain_for_gradio(...)` يعرض فرقًا ملونًا للفونيمات وجدول خصائص.

كلاهما يستخدم `diff-match-patch` لتقسيم الإدراجات والحذف والاختلافات الجزئية بين الفونيمات.

## حقول المخرجات

فئة `Sifa` تتضمن الخصائص التالية (انظر `src/quran_muaalem/muaalem_typing.py`):

- `hams_or_jahr`
- `shidda_or_rakhawa`
- `tafkheem_or_taqeeq`
- `itbaq`
- `safeer`
- `qalqla`
- `tikraar`
- `tafashie`
- `istitala`
- `ghonna`

كل خاصية هي `SingleUnit` وتحتوي على `text` و `prob` و `idx`.
