---
layout: home
hero:
  name: Quran Muaalem
  text: Correct Holy Quran recitations detecting letters, diarctization, attribute of articulations and Tajweed rules using AI opensource for Muslims
  tagline: Model + tools + transcript pipeline in one repo
  actions:
    - theme: brand
      text: Getting Started
      link: /en/getting-started
    - theme: alt
      text: Quran Transcript
      link: /en/quran-transcript/
features:
  - title: Multi-level CTC
    details: The model decodes phonemes and tajweed-related attributes using a multi-level CTC head.
  - title: Reference-aware analysis
    details: Inference compares predicted phonemes with a reference phonetic script from quran-transcript.
  - title: Gradio UI
    details: A ready-to-run UI is wired in src/quran_muaalem/gradio_app.py.
---

## Project Links

- GitHub: https://github.com/obadx/quran-muaalem
- PyPI: https://pypi.org/project/quran-muaalem/
- Hugging Face model: https://huggingface.co/obadx/muaalem-model-v3_2
- Hugging Face dataset: https://huggingface.co/datasets/obadx/muaalem-annotated-v3
- Paper: https://arxiv.org/abs/2509.00094

## What This Repo Contains

- Quran Muaalem inference and UI code under `src/quran_muaalem/`.
- A full Quran transcript toolkit under `quran-transcript/` (packaged as `quran-transcript`).
- Deployment and experiment helpers under `deploy/`, `tests/`, and `assets/`.

Use the navigation to dive into each component.
