# Tests

There are two test suites:

- Quran Muaalem: `tests/`
- Quran Transcript: `quran-transcript/tests/`

Run from repo root:

```bash
pytest
```

Optional flag (see `tests/conftest.py`):

```bash
pytest --skip-slow
```

For the `quran-transcript` subproject, you can also run from its folder:

```bash
cd quran-transcript
pytest
```
