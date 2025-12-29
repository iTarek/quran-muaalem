# Phonetic Pipeline

Quran Muaalem relies on `quran-transcript` to build a phonetic reference for each verse segment. The UI and API both do this before inference.

In `src/quran_muaalem/gradio_app.py`:

- `Aya(...).get_by_imlaey_words(...)` selects the requested verse segment.
- `quran_phonetizer(uthmani_ref, current_moshaf, remove_spaces=True)` converts it to a phonetic script.
- That phonetic script is passed to `Muaalem.__call__` alongside the audio.

This means **the reference script is required** for inference. For details on how `quran_transcript` creates the phonetic script, see the Quran Transcript section.
