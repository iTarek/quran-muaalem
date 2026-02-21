# Quran Muaalem

<div align="center">
<strong>بعون الله وتوفيقه لا شريك له نقدم المعلم القرآني الذكي القادر على كشف أخطاء التلاوة والتجويد وصفات الحروف</strong>

[![PyPI][pypi-badge]][pypi-url]
[![Python Versions][python-badge]][python-url]
[![Hugging Face Model][hf-model-badge]][hf-model-url]
[![Hugging Face Dataset][hf-dataset-badge]][hf-dataset-url]
[![Google Colab][colab-badge]][colab-url]
[![arXiv][arxiv-badge]][arxiv-url]
[![MIT License][mit-badge]][mit-url]
[![Discord][discord-badge]][discord-url]

</div>

[pypi-badge]: https://img.shields.io/pypi/v/quran-muaalem.svg
[pypi-url]: https://pypi.org/project/quran-muaalem/
[mit-badge]: https://img.shields.io/github/license/obadx/quran-muaalem.svg
[mit-url]: https://github.com/obadx/quran-muaalem/blob/main/LICENSE
[python-badge]: https://img.shields.io/pypi/pyversions/quran-muaalem.svg
[python-url]: https://pypi.org/project/quran-muaalem/
[colab-badge]: https://img.shields.io/badge/Google%20Colab-Open%20in%20Colab-F9AB00?logo=google-colab&logoColor=white
[colab-url]: https://colab.research.google.com/drive/1If0G9NtdXiSRu6PVGtIMvLwxizF2jspn?usp=sharing
[hf-model-badge]: https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-blue
[hf-model-url]: https://huggingface.co/obadx/muaalem-model-v3_0
[hf-dataset-badge]: https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-orange
[hf-dataset-url]: https://huggingface.co/datasets/obadx/muaalem-annotated-v3
[arxiv-badge]: https://img.shields.io/badge/arXiv-Paper-<COLOR>.svg
[arxiv-url]: https://arxiv.org/abs/2509.00094
[discord-badge]: https://img.shields.io/badge/Discord-Join%20Community-7289da?logo=discord&logoColor=white
[discord-url]: https://discord.gg/hJWW6fCH

<div align="center" style="background-color: #f0f8ff; border-left: 5px solid #4CAF50; padding: 15px; margin: 20px 0; border-radius: 5px;">
  <h3 style="color: #2c3e50; margin-top: 0;">📖 رابط لتجربة المعلم القرآني</h3>
  <p style="margin: 10px 0;">يرجى الضغط على للتجربة:</p>
  <a href="https://662a040e1863a5445c.gradio.live" style="display: inline-block; background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; font-weight: bold; margin: 10px 0;">الرابط</a>
  <p style="background-color: #ffeb3b; padding: 8px; border-radius: 3px; display: inline-block; margin: 10px 0;">
    ⚠️ <strong>تنبيه:</strong> هذا الرابط سينتهي في <span style="color: #d32f2f; font-weight: bold;">27 أغسطس 2025</span>
  </p>
</div>

[![ALT_TEXT](https://img.youtube.com/vi/CsFoznO08-Q/0.jpg)](https://www.youtube.com/watch?v=CsFoznO08-Q)


## الممزيات

* مدرب على الرسم الصوتي للقرآن الكريم: [quran-transcript](https://github.com/obadx/quran-transcript) القادر على كشف أخطاء الحروف والتجويد وصفات الحروف
* نموذج معقول الحجم 660 MP 
* يحتاج فقط إله 1.5 GB من ذاكرة معالج الرسوميات
* معمارية مبتكرة: CTC متعدد المستويات

## المعمارية
معمارية مبتكرة: CTC متعدد المستويات. حيث كل مستوي يتدرب على وجه معين

![multi-lvel-ctc](./assets/figures/mutli-level-ctc.png)

## الخطوات المختصرة للتطوير

* تجميع التلاوت القرآنية من القراء المتقنين: [prepare-quran-dataset](https://github.com/obadx/prepare-quran-dataset)
* تقسيم التلاوت على حسب الوقف وليس الآية باستخدام [المقسم](https://github.com/obadx/recitations-segmenter)
* الحصو على النص القرآني من المقاطع الصوتية باسخدام [نموذج ترتيل](https://huggingface.co/tarteel-ai/whisper-base-ar-quran)
* تصحيح النصوص المستخرجة من ترتيل باستخدام  [خوارزمية التسميع](https://github.com/obadx/quran-transcript)
* تحويل الرسم الإملائي للرسم العثماني: [quran-transcript](https://github.com/obadx/quran-transcript)
* تحويل الرسم العثماني للرسم الصوتي للقرآني الكريم الذي يصف كل قواعد التجويد ما عدا الإشمام: [quran-transcript](https://github.com/obadx/quran-transcript)
* تدريب النموذج على معمارية [Wav2Vec2BERT](https://huggingface.co/docs/transformers/model_doc/wav2vec2-bert)


## استخدام النوذج


### استخدام النموذج عن طريق واجهة gradio

قم بتزيل  [uv](https://docs.astral.sh/uv/) 

```bash
pip install uv
```
أو
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

بعد ذلك قم بتنزيل `ffmpeg`

```bash
sudo apt-get update
sudo apt-get install -y ffmpeg
```

أو من خلال `anaconda`
```bash
conda install ffmpeg
```

قم بتشغيل `gradio` ب command واحد فقط:
```bash
uvx --no-cache --from https://github.com/obadx/quran-muaalem.git[ui]  quran-muaalem-ui
```
او
```bash
uvx quran-muaalem[ui]  quran-muaalem-ui
```

### عن طريق python API


#### Installation

First, install the required dependencies:

```bash
# Install system dependencies
sudo apt-get install -y ffmpeg libsndfile1 portaudio19-dev

# Install Python packages
pip install quran-muaalem librosa "numba>=0.61.2"
```

## Basic Usage Example

```python
"""
Basic example of using the Quran Muaalem package for phonetic analysis of Quranic recitation.
"""

from dataclasses import asdict
import json
import logging

from quran_transcript import Aya, quran_phonetizer, MoshafAttributes
import torch
from librosa.core import load

# Import the main Muaalem class (adjust import based on your actual package structure)
from quran_muaalem import Muaalem

# Setup logging to see informative messages
logging.basicConfig(level=logging.INFO)

def analyze_recitation(audio_path):
    """
    Analyze a Quranic recitation audio file using the Muaalem model.
    
    Args:
        audio_path (str): Path to the audio file to analyze
    """
    # Configuration
    sampling_rate = 16000  # Must be 16000 Hz
    device = "cuda" if torch.cuda.is_available() else "cpu"  # Use GPU if available
    
    # Step 1: Prepare the Quranic reference text
    # Get the Uthmani script for a specific verse (Aya 8, Surah 75 in this example)
    uthmani_ref = Aya(8, 75).get_by_imlaey_words(17, 9).uthmani
    
    # Step 2: Configure the recitation style (Moshaf attributes)
    moshaf = MoshafAttributes(
        rewaya="hafs",        # Recitation style (Hafs is most common)
        madd_monfasel_len=2,  # Length of separated elongation
        madd_mottasel_len=4,  # Length of connected elongation
        madd_mottasel_waqf=4, # Length of connected elongation when stopping
        madd_aared_len=2,     # Length of necessary elongation
    )
    # see: https://github.com/obadx/prepare-quran-dataset?tab=readme-ov-file#moshaf-attributes-docs
    
    # Step 3: Convert text to phonetic representation
    # see docs for phnetizer: https://github.com/obadx/quran-transcript
    phonetizer_out = quran_phonetizer(uthmani_ref, moshaf, remove_spaces=True)
    
    # Step 4: Initialize the Muaalem model
    muaalem = Muaalem(device=device)
    
    # Step 5: Load and prepare the audio
    wave, _ = load(audio_path, sr=sampling_rate, mono=True)
    
    # Step 6: Process the audio with the model
    # The model analyzes the phonetic properties of the recitation
    outs = muaalem(
        [wave],           # Audio data
        [phonetizer_out],          # Phonetic reference
        sampling_rate=sampling_rate
    )
    
    # Step 7: Display the results
    for out in outs:
        print("Predicted Phonemes:", out.phonemes.text)
        
        # Display detailed phonetic features for each phoneme
        for sifa in out.sifat:
            print(json.dumps(asdict(sifa), indent=2, ensure_ascii=False))
            print("*" * 30)
        print("-" * 40)

    # Explaining Results
    explain_for_terminal(
        outs[0].phonemes.text,
        phonetizer_out.phonemes,
        outs[0].sifat,
        phonetizer_out.sifat,
    )


if __name__ == "__main__":
    # Replace with the path to your audio file
    audio_path = "./assets/test.wav"
    
    try:
        analyze_recitation(audio_path)
    except Exception as e:
        logging.error(f"Error processing audio: {e}")
```

Output:

```bash
ءِننننَللَااهَبِكُللِشَيءِنعَلِۦۦمُ۾۾۾بَرَااااءَتُممممِنَللَااهِوَرَسُۥۥلِه
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┳━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┓
┃ Phonemes ┃ Tafashie       ┃ Qalqla       ┃ Ghonna       ┃ Hams Or Jahr ┃ Safeer    ┃ Tikraar     ┃ Tafkheem Or Taqeeq ┃ Istitala      ┃ Shidda Or Rakhawa ┃ Itbaq    ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━╇━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━┩
│ ءِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ ننننَ     │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ للَ       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ mofakham           │ not_mostateel │ between           │ monfateh │
│ اا       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ mofakham           │ not_mostateel │ rikhw             │ monfateh │
│ هَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ بِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ كُ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ للِ       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ شَ        │ motafashie     │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ ي        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ ءِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ ن        │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ عَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ لِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ ۦۦ       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ مُ        │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ ۾۾۾      │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ بَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ رَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ mokarar     │ mofakham           │ not_mostateel │ between           │ monfateh │
│ اااا     │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ mofakham           │ not_mostateel │ rikhw             │ monfateh │
│ ءَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ تُ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ shadeed           │ monfateh │
│ ممممِ     │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ نَ        │ not_motafashie │ not_moqalqal │ maghnoon     │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ للَ       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ mofakham           │ not_mostateel │ between           │ monfateh │
│ اا       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ mofakham           │ not_mostateel │ rikhw             │ monfateh │
│ هِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ وَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ رَ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ mokarar     │ mofakham           │ not_mostateel │ between           │ monfateh │
│ سُ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ safeer    │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ ۥۥ       │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
│ لِ        │ not_motafashie │ not_moqalqal │ not_maghnoon │ jahr         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ between           │ monfateh │
│ ه        │ not_motafashie │ not_moqalqal │ not_maghnoon │ hams         │ no_safeer │ not_mokarar │ moraqaq            │ not_mostateel │ rikhw             │ monfateh │
└──────────┴────────────────┴──────────────┴──────────────┴──────────────┴───────────┴─────────────┴────────────────────┴───────────────┴───────────────────┴──────────┘
```

### API Docs

```python
class Muaalem:
    def __init__(
        self,
        model_name_or_path: str = "obadx/muaalem-model-v3_2",
        device: str = "cpu",
        dtype=torch.bfloat16,
    ):
        """
        Initializing Muallem Model

        Args:
            model_name_or_path: the huggingface model name or path
            device: the device to run model on
            dtype: the torch dtype. Default is `torch.bfloat16` as the model was trained on
        """

    @torch.no_grad()
    def __call__(
        self,
        waves: list[list[float] | torch.FloatTensor | NDArray],
        ref_quran_phonetic_script_list: list[QuranPhoneticScriptOutput],
        sampling_rate: int,
    ) -> list[MuaalemOutput]:
        """Infrence Funcion for the Quran Muaalem Project

                waves: input waves  batch , seq_len with different formats described above
                ref_quran_phonetic_script_list (list[QuranPhoneticScriptOutput]): list of the
                    phonetized ouput of `quran_transcript.quran_phonetizer` with `remove_space=True`

                sampleing_rate (int): has to be 16000

        Returns:
            list[MuaalemOutput]:
                A list of output objects, each containing phoneme predictions and their
                phonetic features (sifat) for a processed input.

            Each MuaalemOutput contains:
                phonemes (Unit):
                    A dataclass representing the predicted phoneme sequence with:
                        text (str): Concatenated string of all phonemes.
                        probs (Union[torch.FloatTensor, list[float]]):
                            Confidence probabilities for each predicted phoneme.
                        ids (Union[torch.LongTensor, list[int]]):
                            Token IDs corresponding to each phoneme.

                sifat (list[Sifa]):
                    A list of phonetic feature dataclasses (one per phoneme) with the
                    following optional properties (each is a SingleUnit or None):
                        - phonemes_group (str): the phonemes associated with the `sifa`
                        - hams_or_jahr (SingleUnit): either `hams` or `jahr`
                        - shidda_or_rakhawa (SingleUnit): either `shadeed`, `between`, or `rikhw`
                        - tafkheem_or_taqeeq (SingleUnit): either `mofakham`, `moraqaq`, or `low_mofakham`
                        - itbaq (SingleUnit): either `monfateh`, or `motbaq`
                        - safeer (SingleUnit): either `safeer`, or `no_safeer`
                        - qalqla (SingleUnit): eithr `moqalqal`, or `not_moqalqal`
                        - tikraar (SingleUnit): either `mokarar` or `not_mokarar`
                        - tafashie (SingleUnit): either `motafashie`, or `not_motafashie`
                        - istitala (SingleUnit): either `mostateel`, or `not_mostateel`
                        - ghonna (SingleUnit): either `maghnoon`, or `not_maghnoon`

            Each SingleUnit in Sifa properties contains:
                text (str): The feature's categorical label (e.g., "hams", "shidda").
                prob (float): Confidence probability for this feature.
                idx (int): Identifier for the feature class.
        """


---

## خوادم API

يحتوي المشروع على خويمين رئيسيين:

1. **المحرك (Engine)**: يشغّل نموذج Wav2Vec2-BERT لتحويل الصوت إلى فونيمات
2. **التطبيق (App)**: يوفر واجهات البحث والتصحيح والنسخ

### التثبيت

```bash
uv add quran-muaalem[engine]
```

### تشغيل الخوادم

```bash
# الطرفية الأولى: تشغيل المحرك (منفذ 8000)
uv run quran-muaalem-engine

# الطرفية الثانية: تشغيل التطبيق (منفذ 8001)
uv run quran-muaalem-app
```

---

## إعدادات المحرك (EngineSettings)

الإعدادات موجودة في `src/quran_muaalem/engine/settings.py`:

| الإعداد | النوع | القيمة الافتراضية | الوصف |
|---------|-------|-------------------|-------|
| `model_name_or_path` | string | `obadx/muaalem-model-v3_2` | مسار نموذج HuggingFace |
| `dtype` | string | `bfloat16` | نوع البيانات: `float32`, `float16`, `bfloat16` |
| `max_audio_seconds` | float | `15` | الحد الأقصى لطول الصوت بالثواني |
| `max_batch_size` | int | `128` | حجم الدفعة القصوى للمعالجة |
| `batch_timeout` | float | `0.4` | مهلة الانتظار للدفعة بالثواني |
| `host` | string | `0.0.0.0` | عنوان ربط الخادم |
| `port` | int | `8000` | منفذ الخادم |
| `accelerator` | string | `cuda` | معالج الأجهزة: `cuda`, `cpu`, `mps` |
| `devices` | int | `1` | عدد الأجهزة |
| `workers_per_device` | int | `1` | عدد العمال لكل جهاز |
| `timeout` | float | `90.0` | مهلة الطلب بالثواني |

---

## إعدادات التطبيق (AppSettings)

الإعدادات موجودة في `src/quran_muaalem/app/settings.py`:

| الإعداد | القيمة الافتراضية | الوصف |
|---------|-------------------|-------|
| `engine_url` | `http://0.0.0.0:8000/predict` | رابط نقطة `/predict` في المحرك |
| `host` | `0.0.0.0` | عنوان ربط الخادم |
| `port` | `8001` | منفذ الخادم |
| `error_ratio` | `0.1` | نسبة الخطأ المسموحة للبحث (0.0-1.0) |
| `max_workers_phonetic_search` | `cpu_count // 2` | عدد عمليات البحث الصوتية المتزامنة |
| `max_workers_phonetization` | `cpu_count // 2` | عدد عمليات الفونتة المتزامنة |

---

## نقاط النهاية

### المحرك (Engine) - المنفذ 8000

| النقطة | الوصف |
|--------|-------|
| `/predict` | تحويل الصوت إلى فونيمات |
| `/health` | فحص حالة الخادم |
| `/docs` | وثائق OpenAPI التفاعلية |
| `/redoc` | وثائق ReDoc البديلة |

### التطبيق (App) - المنفذ 8001

| النقطة | الوصف |
|--------|-------|
| `/health` | فحص حالة التطبيق والاتصال بالمحرك |
| `/search` | البحث في القرآن بالصوت أو النص الصوتي |
| `/correct-recitation` | تحليل التلاوة واكتشاف أخطاء التجويد |
| `/transcript` | نسخ الصوت إلى نص صوتي (وكيل للمحرك) |
| `/docs` | وثائق OpenAPI التفاعلية |
| `/redoc` | وثائق ReDoc البديلة |

---

## خصائص المصحف (MoshafAttributes)

هذه الخصائص تُعرّف قواعد التلاوة لقراءة حفص. جميع الحقول اختيارية:

| الخاصية | العربية | القيم | القيمة الافتراضية | الوصف |
|---------|---------|-------|-------------------|-------|
| `rewaya` | الرواية | `hafs` (حفص) | `hafs` | نوع قراءة القرآن |
| `recitation_speed` | سرعة التلاوة | `mujawad` (مجود), `above_murattal` (فويق المرتل), `murattal` (مرتل), `hadr` (حدر) | `murattal` | سرعة التلاوة مرتبة من الأبطأ إلى الأسرع |
| `takbeer` | التكبير | `no_takbeer` (لا تكبير), `beginning_of_sharh` (التكبير من أول الشرح لأول الناس), `end_of_doha` (التكبير من آخر الضحى لآخر الناس), `general_takbeer` (التكبير أول كل سورة إلا التوبة) | `no_takbeer` | طرق إضافة التكبير (الله أكبر) بعد الاستعاذة (استعاذة) وبين نهاية السورة وبداية السورة |
| `madd_monfasel_len` | مد المنفصل | `2`, `3`, `4`, `5` | `4` | مقدار مد المنفصل (مد النفصل) لقراءة حفص |
| `madd_mottasel_len` | مقدار المد المتصل | `4`, `5`, `6` | `4` | مقدار المد المتصل لقراءة حفص |
| `madd_mottasel_waqf` | مقدار المد المتصل وقفا | `4`, `5`, `6` | `4` | مقدار المد المتصل عند الوقف لقراءة حفص |
| `madd_aared_len` | مقدار مد العارض | `2`, `4`, `6` | `4` | مقدار مد العارض للسكون |
| `madd_alleen_len` | مقدار مد اللين | `2`, `4`, `6` | `None` | مقدار مد اللين عند الوقف (يختصر إلى madd_aared_len) |
| `ghonna_lam_and_raa` | غنة اللام و الراء | `ghonna` (غنة), `no_ghonna` (لا غنة) | `no_ghonna` | الغنة في إدغام النون مع اللام والراء لقراءة حفص |
| `meem_aal_imran` | ميم آل عمران | `waqf` (وقف), `wasl_2` (فتح الميم ومدها حركتين), `wasl_6` (فتح الميم ومدها ستة حركات) | `waqf` | طريقة قراءة {الم الله} في حالة الوصل |
| `madd_yaa_alayn_alharfy` | مقدار المد اللازم الحرفي للعين | `2`, `4`, `6` | `6` | مقدار المد الحرفي اللازم لحرف العين في سورة مريم والشورى |
| `saken_before_hamz` | الساكن قبل الهمز | `tahqeek` (تحقيق), `general_sakt` (سكت عام), `local_sakt` (سكت خاص) | `tahqeek` | كيفية قراءة الساكن قبل الهمز لقراءة حفص |
| `sakt_iwaja` | السكت عند عوجا في الكهف | `sakt` (سكت), `waqf` (وقف), `idraj` (إدراج) | `waqf` | كيفية قراءة عوجا (Iwaja) في سورة الكهف |
| `sakt_marqdena` | السكت عند مرقدنا في يس | `sakt` (سكت), `waqf` (وقف), `idraj` (إدراج) | `waqf` | كيفية قراءة مرقدنا (Marqadena) في سورة يس |
| `sakt_man_raq` | السكت عند من راق في القيامة | `sakt` (سكت), `waqf` (وقف), `idraj` (إدراج) | `sakt` | كيفية قراءة من راق (Man Raq) في سورة القيامة |
| `sakt_bal_ran` | السكت عند بل ران في المطففين | `sakt` (سكت), `waqf` (وقف), `idraj` (إدراج) | `sakt` | كيفية قراءة بل ران (Bal Ran) في سورة المطففين |
| `sakt_maleeyah` | وجه قوله {ماليه هلك} بالحاقة | `sakt` (سكت), `waqf` (وقف), `idgham` (إدغام) | `waqf` | كيفية قراءة ماليه هلك في سورة الحاقة |
| `between_anfal_and_tawba` | وجه بين الأنفال والتوبة | `waqf` (وقف), `sakt` (سكت), `wasl` (وصل) | `waqf` | كيفية قراءة نهاية سورة الأنفال وبداية سورة التوبة |
| `noon_and_yaseen` | الإظهار في النون | `izhar` (إظهار), `idgham` (إدغام) | `izhar` | إدغام النون في يس ون والقلم |
| `yaa_athan` | إثبات الياء وحذفها وقفا | `wasl` (وصل), `hadhf` (حذف), `ithbat` (إثبات) | `wasl` | إثبات أو حذف الياء في {آتاني} في سورة النمل |
| `start_with_ism` | وجه البدأ بكلمة {الاسم} | `wasl` (وصل), `lism` (لسم), `alism` (ألسم) | `wasl` | حكم البدأ بكلمة الاسم في سورة الحجرات |
| `yabsut` | السين والصاد في {يقبض ويبسط} | `seen` (سين), `saad` (صاد) | `seen` | النطق في سورة البقرة |
| `bastah` | السين والصاد في {بسطة} | `seen` (سين), `saad` (صاد) | `seen` | النطق في سورة الأعراف |
| `almusaytirun` | السين والصاد في {المصيطرون} | `seen` (سين), `saad` (صاد) | `saad` | النطق في سورة الطور |
| `bimusaytir` | السين والصاد في {بمصيطر} | `seen` (سين), `saad` (صاد) | `saad` | النطق في سورة الغاشية |
| `tasheel_or_madd` | همزة الوصل | `tasheel` (تسهيل), `madd` (مد) | `madd` | تسهيل أو مد همزة الوصل في {آلذكرين} |
| `yalhath_dhalik` | الإدغام في {يلهث ذلك} | `izhar` (إظهار), `idgham` (إدغام), `waqf` (وقف) | `idgham` | الإدغام في سورة الأعراف |
| `irkab_maana` | الإدغام في {اركب معنا} | `izhar` (إظهار), `idgham` (إدغام), `waqf` (وقف) | `idgham` | الإدغام في سورة هود |
| `noon_tamnna` | الإشمام والروم في {تأمنا} | `ishmam` (إشمام), `rawm` (روم) | `ishmam` | الإشمام والروم في سورة يوسف |
| `harakat_daaf` | حركة الضاد في {ضعف} | `fath` (فتح), `dam` (ضم) | `fath` | حركة الضاد في سورة الروم |
| `alif_salasila` | الألف في {سلاسلا} | `hadhf` (حذف), `ithbat` (إثبات), `wasl` (وصل) | `wasl` | إثبات أو حذف الألف في سورة الإنسان |
| `idgham_nakhluqkum` | إدغام القاف في الكاف | `idgham_kamil` (إدغام كامل), `idgham_naqis` (إدغام ناقص) | `idgham_kamil` | إدغام القاف في الكاف في سورة المرسلات |
| `raa_firq` | راء {فرق} في الشعراء | `waqf` (وقف), `tafkheem` (تفخيم), `tarqeeq` (ترقيق) | `tafkheem` | تفخيم وترقيق الراء في سورة الشعراء |
| `raa_alqitr` | راء {القطر} في سبأ | `wasl` (وصل), `tafkheem` (تفخيم), `tarqeeq` (ترقيق) | `wasl` | تفخيم وترقيق الراء في سورة سبأ |
| `raa_misr` | راء {مصر} في يونس | `wasl` (وصل), `tafkheem` (تفخيم), `tarqeeq` (ترقيق) | `wasl` | تفخيم وترقيق الراء في سورة يونس |
| `raa_nudhur` | راء {نذر} في القمر | `wasl` (وصل), `tafkheem` (تفخيم), `tarqeeq` (ترقيق) | `tafkheem` | تفخيم وترقيق الراء في سورة القمر |
| `raa_yasr` | راء {يسر} بالفجر | `wasl` (وصل), `tafkheem` (تفخيم), `tarqeeq` (ترقيق) | `tarqeeq` | تفخيم وترقيق الراء في سورة الفجر |
| `meem_mokhfah` | هل الميم مخفاة أو مدغمة | `meem` (ميم), `ikhfaa` (إخفاء) | `ikhfaa` | إخفاء أو إدغام الميم في حالة الإخفاء |

---

## قواعد التجويد (Tajweed Rules)

قواعد التجويد المستخدمة في تحليل الأخطاء. يتم استيرادها من `quran_transcript.phonetics.tajweed_rulses`:

| القاعدة | العربية | نوع الفحص | الطول المرجعي | الوصف |
|---------|---------|-----------|---------------|-------|
| `Qalqalah` | قلقة | `match` | 0 | قلقلة - حركة الحرف الساكن عند النطق به |
| `NormalMaddRule` | المد الطبيعي | `count` | 2 | المد الطبيعي الذي يأتي بشكل عادي في الكلمة |
| `MonfaselMaddRule` | المد المنفصل | `count` | 4 | المد المنفصل بين الكلمتين |
| `MottaselMaddRule` | المد المتصل | `count` | 4 | المد المتصل بين حروف الكلمة |
| `MottaselMaddPauseRule` | المد المتصل وقفا | `count` | 4 | المد المتصل عند الوقف |
| `LazemMaddRule` | المد اللازم | `count` | 6 | المد اللازم في الحروف المعينة (مثل الميم في الميم) |
| `AaredMaddRule` | المد العارض للسكون | `count` | 4 | المد الذي يظهر عند الوقف على كلمة معينة |
| `LeenMaddRule` | مد اللين | `count` | 4 | مد اللين للواو الساكنة والياء الساكنة قبلها حرف مفتوح |

### شرح أنواع قواعد التجويد

1. **Qalqalah (قلقة)**: حركة الحرف الساكن عند النطق به، وتحدث في حروف القلقلة: ق، ط، ب، ج، د
2. **NormalMaddRule (المد الطبيعي)**: المد العادي الذي يأتي في الكلمة بشكل طبيعي، طوله حركتان
3. **MonfaselMaddRule (المد المنفصل)**: المد بين الكلمتين عندما ينتهي بكلمة وينتهي آخرها بحرف من حروف المد
4. **MottaselMaddRule (المد المتصل)**: المد داخل الكلمة بين حروف المد
5. **MottaselMaddPauseRule (المد المتصل وقفا)**: المد المتصل عند الوقف على كلمة معينة
6. **LazemMaddRule (المد اللازم)**: المد اللازم في الحروف المعينة مثل الميم في {الم} والهمزة في {ءآل}
7. **AaredMaddRule (المد العارض للسكون)**: المد الذي يظهر عند الوقف بسبب السكون
8. **LeenMaddRule (مد اللين)**: مد اللين للواو الساكنة والياء الساكنة وقبلهما حرف مفتوح

---

## مثال كامل: تصحيح التلاوة

### الأمر (curl)

```bash
curl -X 'POST' \
  'http://localhost:8001/correct-recitation' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'error_ratio=0.1' \
  -F 'file=@WhatsApp Ptt 2026-02-20 at 1.56.35 PM.ogg;type=application/ogg'
```

### الاستجابة (JSON)

```json
{
  "start": {
    "sura_idx": 2,
    "aya_idx": 1,
    "uthmani_word_idx": 0,
    "uthmani_char_idx": 0,
    "phonemes_idx": 0
  },
  "end": {
    "sura_idx": 2,
    "aya_idx": 1,
    "uthmani_word_idx": 0,
    "uthmani_char_idx": 5,
    "phonemes_idx": 25
  },
  "predicted_phonemes": "ءَلِفلَااممِۦۦم",
  "reference_phonemes": "ءَلِفلَااااااممممِۦۦۦۦۦۦم",
  "uthmani_text": "الٓمٓ",
  "errors": [
    {
      "uthmani_pos": [1, 2],
      "ph_pos": [7, 13],
      "error_type": "tajweed",
      "speech_error_type": "replace",
      "expected_ph": "اااااا",
      "preditected_ph": "اا",
      "expected_len": 6,
      "predicted_len": 2,
      "ref_tajweed_rules": [
        {
          "name": {"ar": "المد اللازم", "en": "Lazem Madd"},
          "golden_len": 6,
          "correctness_type": "count",
          "tag": "alif"
        }
      ],
      "inserted_tajweed_rules": null,
      "replaced_tajweed_rules": null,
      "missing_tajweed_rules": null
    },
    {
      "uthmani_pos": [3, 4],
      "ph_pos": [13, 18],
      "error_type": "tajweed",
      "speech_error_type": "replace",
      "expected_ph": "ممممِ",
      "preditected_ph": "ممِ",
      "expected_len": 6,
      "predicted_len": 2,
      "ref_tajweed_rules": [
        {
          "name": {"ar": "المد اللازم", "en": "Lazem Madd"},
          "golden_len": 6,
          "correctness_type": "count",
          "tag": "yaa"
        }
      ],
      "inserted_tajweed_rules": null,
      "replaced_tajweed_rules": null,
      "missing_tajweed_rules": null
    },
    {
      "uthmani_pos": [3, 4],
      "ph_pos": [18, 24],
      "error_type": "tajweed",
      "speech_error_type": "replace",
      "expected_ph": "ۦۦۦۦۦۦ",
      "preditected_ph": "ۦۦ",
      "expected_len": 6,
      "predicted_len": 2,
      "ref_tajweed_rules": [
        {
          "name": {"ar": "المد اللازم", "en": "Lazem Madd"},
          "golden_len": 6,
          "correctness_type": "count",
          "tag": "yaa"
        }
      ],
      "inserted_tajweed_rules": null,
      "replaced_tajweed_rules": null,
      "missing_tajweed_rules": null
    }
  ]
}
```

### شرح الاستجابة

- **start/end**: موقع النتيجة في القرآن (رقم السورة، رقم الآية، موقع الكلمة، موقع الحرف، موقع الفونيم)
- **predicted_phonemes**: الفونيمات المتوقعة من الصوت
- **reference_phonemes**: الفونيمات المرجعية من النص القرآني باستخدام خصائص المصحف
- **uthmani_text**: النص العثماني المطابق
- **errors**: قائمة الأخطاء المكتشفة، كل خطأ يحتوي على:
  - **error_type**: نوع الخطأ (`tajweed` = تجودي، `normal` = عادي، `tashkeel` = تشكيل)
  - **speech_error_type**: نوع خطأ الكلام (`insert` = إدخال، `delete` = حذف، `replace` = استبدال)
  - **expected_ph/predicted_ph**: الفونيم المتوقع والمتنبأ به
  - **expected_len/predicted_len**: الطول المتوقع والمتنبأ به (لمدود مثل المد اللازم)
  - **ref_tajweed_rules**: قواعد التجويد المرجعية التي يجب تطبيقها

---

## وثائق OpenAPI التفاعلية

للحصول على وثائق تفاعلية كاملة مع أمثلة وأوصاف مفصلة لكل المعلمة، الرجاء زيارة:

- **التطبيق (App)**: http://localhost:8001/docs
- **المحرك (Engine)**: http://localhost:8000/docs

تحتوي هذه الوثائق على:
- جميع نقاط النهاية مع أوصافها الكاملة
- جميع المعاملات مع قيمها الافتراضية ونوع البيانات
- أمثلة تفاعلية لكل نقطة نهاية
- مخططات الاستجابة الكاملة
- إمكانية التنفيذ المباشر من المتصفح
```
