# الاختبارات

هناك مجموعتان من الاختبارات:

- المعلّم القرآني: `tests/`
- Quran Transcript: `quran-transcript/tests/`

التشغيل من جذر المستودع:

```bash
pytest
```

خيار إضافي (انظر `tests/conftest.py`):

```bash
pytest --skip-slow
```

ولمشروع `quran-transcript` يمكن التشغيل من مجلده:

```bash
cd quran-transcript
pytest
```
