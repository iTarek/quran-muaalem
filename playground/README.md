# Playground — Interactive Mushaf for Quran Muaalem

An interactive Quran Mushaf web app that serves as a visual playground for testing the **Quran Muaalem** API. Instead of testing with `curl` or Postman, you can recite into your microphone and see the AI-powered correction results rendered beautifully on an authentic Mushaf layout.

Built on top of the open-source [Java Quran Web](https://github.com/iTarek/Java-Quran-Web) project.

## Features

- **Search (Find My Position)** — Recite a few ayahs and the app finds your location in the Quran, navigating the Mushaf to the matched ayah
- **Recite (Correct Tajweed)** — Tap an ayah, recite it, and get instant feedback on tajweed errors with rule names in Arabic and English
- **Full Mushaf** — All 604 pages rendered with QCF4 fonts in authentic Mushaf Madina layout
- **Tafseer & Translation** — Long-press any ayah for Arabic tafseer (Al-Muyassar) and English translation (Saheeh International)
- **Audio Playback** — Listen to verse recitation by Mishary Alafasy

## Quick Start

1. **Start the engine and app servers:**

   ```bash
   # Terminal 1 — Start the engine (Wav2Vec2-BERT model)
   uv run quran-muaalem-engine --accelerator mps  # or --accelerator cuda

   # Terminal 2 — Start the app server (from the project root)
   uv run quran-muaalem-app
   ```

2. **Open the playground:**

   Navigate to **http://localhost:8001** in your browser.

   > The app server automatically serves the playground when it detects the `playground/` directory in the current working directory.

3. **Try it out:**
   - Click **Search** → recite "بسم الله الرحمن الرحيم" → the Mushaf navigates to the matched ayah
   - Tap an ayah to select it → click **Recite** → recite the ayah → see tajweed correction results

## How It Works

```
Browser (playground)
    ↓ fetch(/search, /correct-recitation)
App Server (localhost:8001) — FastAPI
    ↓
Engine Server (localhost:8000) — Wav2Vec2-BERT
```

The playground is a pure static web app (HTML + CSS + vanilla JS) that calls the Quran Muaalem API endpoints directly. When served from the app server, no proxy or CORS configuration is needed — everything runs on the same port.

## Technology

- **Zero dependencies** — Pure vanilla JavaScript, HTML, and CSS
- **QCF4 fonts** — Official Quran Complex Fonts v4 (WOFF2, ~36 MB)
- **Web Audio API** — Microphone recording with WAV encoding, no external libraries
- **Responsive** — Works on desktop and mobile with touch support

## Credits

- Mushaf viewer based on [Java Quran Web](https://github.com/iTarek/Java-Quran-Web) (GPL-3.0)
- QCF4 fonts from King Fahd Complex for the Printing of the Holy Quran
- Tafseer: Al-Tafseer Al-Muyassar | Translation: Saheeh International
- Audio: Mishary Rashid Alafasy via everyayah.com
