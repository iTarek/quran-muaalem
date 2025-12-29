# Moshaf Attributes

The phonetic conversion is controlled by `MoshafAttributes` in `quran-transcript/src/quran_transcript/phonetics/moshaf_attributes.py`. It is a `pydantic.BaseModel` with many Quran-specific recitation options (madd lengths, takbeer, and more).

## How the UI Uses It

In `src/quran_muaalem/gradio_app.py`:

- `REQUIRED_MOSHAF_FIELDS` enumerates the attributes exposed in the UI.
- `create_gradio_input_for_field(...)` introspects `MoshafAttributes.model_fields` and builds inputs.
- `get_arabic_name(...)` and `get_arabic_attributes(...)` (from `quran_transcript.phonetics.moshaf_attributes`) provide label metadata.

To see the full list of available attributes and their defaults, open:

- `quran-transcript/src/quran_transcript/phonetics/moshaf_attributes.py`

If you want to expose more fields in the UI, add them to `REQUIRED_MOSHAF_FIELDS` in `src/quran_muaalem/gradio_app.py`.
