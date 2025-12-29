# واجهة بايثون

الفئة الأساسية للاستدلال هي `Muaalem` في `src/quran_muaalem/inference.py`.

## توقيع الفئة

```python
class Muaalem:
    def __init__(
        self,
        model_name_or_path: str = "obadx/muaalem-model-v3_2",
        device: str = "cpu",
        dtype=torch.bfloat16,
    ):
        ...

    @torch.no_grad()
    def __call__(
        self,
        waves: list[list[float] | torch.FloatTensor | NDArray],
        ref_quran_phonetic_script_list: list[QuranPhoneticScriptOutput],
        sampling_rate: int,
    ) -> list[MuaalemOutput]:
        ...
```

ملاحظات من التنفيذ:

- `sampling_rate` يجب أن يساوي `16000` وإلا سيُرفع `ValueError`.
- القيمة الافتراضية لـ `model_name_or_path` هي `obadx/muaalem-model-v3_2`.
- `dtype` الافتراضي هو `torch.bfloat16`.

## المدخلات المطلوبة

- **الصوت**: مصفوفات الموجة الصوتية بمعدل 16 kHz.
- **المرجع**: كائنات `QuranPhoneticScriptOutput` الناتجة من `quran_transcript.quran_phonetizer`.

## أنواع المخرجات

راجع `src/quran_muaalem/muaalem_typing.py`:

- `Unit`: تسلسل فونيمات مفكوك مع احتمالات ومعرّفات.
- `Sifa`: خصائص لكل مجموعة فونيمات.
- `MuaalemOutput`: الحاوية التي تجمع `phonemes` و `sifat`.

للمثال الكامل راجع كود `README.md`.
