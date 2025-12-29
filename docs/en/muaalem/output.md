# Outputs and Explanations

The inference output is a list of `MuaalemOutput` objects (`src/quran_muaalem/muaalem_typing.py`). Each item contains:

- `phonemes`: a `Unit` with decoded phoneme text, probabilities, and ids.
- `sifat`: a list of `Sifa` entries (one per phoneme group), each with optional phonetic attributes.

## Comparing Predictions to Reference

Two helper modules format the outputs for humans:

- `src/quran_muaalem/explain.py` renders a terminal table using `rich`.
  - `explain_for_terminal(...)` builds a diff between predicted phonemes and the reference, then prints a table.
- `src/quran_muaalem/explain_gradio.py` renders HTML for the Gradio UI.
  - `explain_for_gradio(...)` shows a colorized phoneme diff and a table of attributes.

Both use `diff-match-patch` to segment insertions, deletions, and partial matches between the predicted phonemes and the reference phoneme string.

## Output Fields

The `Sifa` dataclass includes these optional attributes (see `src/quran_muaalem/muaalem_typing.py`):

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

Each attribute is a `SingleUnit` with `text`, `prob`, and `idx`.
