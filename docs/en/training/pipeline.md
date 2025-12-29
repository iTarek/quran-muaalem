# Pipeline Steps

The high-level steps described in `README.md` are:

1. Collect high-quality recitations.
2. Segment recitations by pause boundaries.
3. Transcribe audio using the Quran-specific Whisper model.
4. Correct transcriptions using the tasmeea algorithm (`quran-transcript`).
5. Convert Imlaey script to Uthmani script (`quran-transcript`).
6. Convert Uthmani to phonetic script (`quran-transcript`).
7. Train with the multi-level CTC architecture (see `src/quran_muaalem/modeling/`).

If you want more details or diagrams here, point me to the training notes you want included.
