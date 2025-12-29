# Gradio UI

The UI entrypoint is defined in `src/quran_muaalem/gradio_app.py` and exposed as the console script `quran-muaalem-ui` in `pyproject.toml`.

## What the UI Does

Key functions in `src/quran_muaalem/gradio_app.py`:

- `process_audio(...)` loads audio (via `librosa.load`), builds a phonetic reference with `quran_phonetizer`, runs `Muaalem`, and renders HTML output.
- `update_uthmani_ref(...)` fetches Uthmani script segments from `quran_transcript.Aya`.
- `create_gradio_input_for_field(...)` builds UI controls based on `MoshafAttributes` fields.

The app starts in `main()` with:

```python
app.launch(server_name="0.0.0.0", share=True)
```

If you want different launch options (disable sharing or set a port), this is the place to adjust them.

## Running the UI

After installing the UI extras:

```bash
pip install "quran-muaalem[ui]"
quran-muaalem-ui
```

The `quran-muaalem-ui` console script points to `quran_muaalem.gradio_app:main` (see `pyproject.toml`).
