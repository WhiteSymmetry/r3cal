# r3cal <img src="https://github.com/WhiteSymmetry/r3cal/blob/main/docs/r3cal-256.png" alt="r3cal" align="right" height="140"/>

---

##  r3cal: Resistor Color Code Calculator: Direnç Renk Kodu Hesaplayıcı

---

**English** | [Türkçe](#türkçe)

A modern, multilingual **resistor color code calculator** for Python.
Supports **4, 5, and 6-band resistors**, N/A bands, live previews, and an
optional bilingual (EN/TR) interface. Works both as a **standalone GUI** and
as an **embeddable widget** inside your own Tkinter application.

---

## 📦 Installation

```bash
pip install r3cal
```

```bash
conda install bilgi::r3cal -y
```

Python **3.11+** is required. Tkinter ships with the standard library on
Windows and macOS. On Linux you may need:

```bash
sudo apt install python3-tk        # Debian / Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

---

## ✨ Features

| Feature | Description |
|---|---|
| 4 / 5 / 6-band support | Switch instantly with radio buttons |
| Full color tables | Digit, multiplier, tolerance, tempco — all N/A entries included |
| Tolerances | ±1, 2, 3, 4, 0.5, 0.25, 0.1, 0.05, 5, 10 % and **None = ±20 %** |
| Temperature coefficient | 100, 50, 25, 15, 10, 5 ppm/°C (N/A shown when applicable) |
| Multilingual UI | English / Türkçe / Bilingual (both at once) |
| Flexible input | Dropdown, color number (1–13), English name, or Turkish name |
| Live preview | Each band shows its real color in a swatch |
| Smart formatting | Auto Ω / kΩ / MΩ / GΩ / mΩ / µΩ |
| Font scaling | Built-in **A+ / A−** buttons |
| Embeddable | Pass a `Tk` window *or* a `Frame` |

---

## 🚀 Quick Start

### Standalone

```bash
!python -m r3cal
```

import r3cal, tkinter as tk; r3cal.R3Cal(tk.Tk()); tk.mainloop()

or

```python
import tkinter as tk
import r3cal

r3cal.R3Cal(tk.Tk())
tk.mainloop()
```

### Embedded in your own window

```python
import tkinter as tk
from tkinter import ttk
import r3cal

root = tk.Tk()
root.title("My App")
root.geometry("1000x800")

frame = ttk.Frame(root, padding=6)
frame.pack(fill="both", expand=True)

app = r3cal.R3Cal(frame)   # embed inside a Frame
root.mainloop()
```

### Direct class import

```python
from r3cal import R3Cal
import tkinter as tk

R3Cal(tk.Tk())
tk.mainloop()
```

---

## 🎨 Usage

1. Choose **4 / 5 / 6 bands** at the top.
2. Pick a **language**: `English`, `Türkçe`, or `English + Türkçe`.
3. For each band, do **any of these**:
   - Select a color from the dropdown, **or**
   - Type the **color number** (`1`–`13`) and press Enter, **or**
   - Type the **English** name (`Red`), **or**
   - Type the **Turkish** name (`Kırmızı`).
4. Results update **live**: resistance, tolerance, min/max, tempco.
5. Use **A+ / A−** at the bottom to scale the interface font.

### Color number reference

| # | English | Türkçe | Role |
|---|---------|--------|------|
| 1 | Black | Siyah | Digit / Multiplier / N/A |
| 2 | Brown | Kahverengi | Digit / Multiplier / Tolerance / Tempco |
| 3 | Red | Kırmızı | Digit / Multiplier / Tolerance / Tempco |
| 4 | Orange | Turuncu | Digit / Multiplier / Tolerance / Tempco |
| 5 | Yellow | Sarı | Digit / Multiplier / Tolerance / Tempco |
| 6 | Green | Yeşil | Digit / Multiplier / Tolerance |
| 7 | Blue | Mavi | Digit / Multiplier / Tolerance / Tempco |
| 8 | Violet | Mor | Digit / Multiplier / Tolerance / Tempco |
| 9 | Grey | Gri | Digit / Multiplier / Tolerance |
| 10 | White | Beyaz | Digit / Multiplier / N/A |
| 11 | Gold | Altın | Multiplier (×0.1) / Tolerance (±5 %) |
| 12 | Silver | Gümüş | Multiplier (×0.01) / Tolerance (±10 %) |
| 13 | None | Yok | Tolerance (±20 %) |

---

## 📚 API Reference

### `class r3cal.R3Cal(container)`

Creates the calculator widget. `container` can be either:

- a `tkinter.Tk` / `tkinter.Toplevel` → standalone window,
- a `tkinter.ttk.Frame` → embedded widget.

The instance exposes:

| Attribute | Type | Description |
|---|---|---|
| `scale` | `float` | Current font scale (0.7–2.5). Set programmatically before `_apply_geometry()`. |
| `lang` | `tk.StringVar` | Current language (`"en"`, `"tr"`, `"both"`). |
| `band_count` | `tk.IntVar` | Current band count (4, 5, 6). |

### Color tables (module-level)

```python
from r3cal import DIGIT, MULTIPLIER, TOLERANCE, TEMPCO, COLORS
```

| Name | Meaning |
|---|---|
| `DIGIT` | `{color: 0..9}` |
| `MULTIPLIER` | `{color: multiplier}` (Gold=0.1, Silver=0.01) |
| `TOLERANCE` | `{color: percent or None}` |
| `TEMPCO` | `{color: ppm/°C or None}` |
| `COLORS` | `{key: {"en":…, "tr":…, "preview":…}}` |

### Helper functions

```python
from r3cal import parse_color, fmt_resistance

parse_color("3")             # → "Red"
parse_color("Kırmızı")       # → "Red"
parse_color("1 - Black")     # → "Black"
fmt_resistance(2200)         # → "2.2 kΩ"
```

---

## 🧪 Examples

### 220 Ω, 4-band (Red-Red-Brown-Gold)

| Band | Color |
|---|---|
| 1 | Red |
| 2 | Red |
| 3 | Brown |
| 4 | Gold |

**Result:** `220 Ω ±5 %`, Min `209 Ω`, Max `231 Ω`.

### 220 Ω, 6-band with N/A tempco

| Band | Color |
|---|---|
| 1–3 | Red-Red-Black |
| Multiplier | Black |
| Tolerance | Gold |
| Tempco | Green |

**Result:** `220 Ω ±5 %`, Tempco **N/A**.

### N/A tolerance

Any 4-band resistor with tolerance set to **Black** or **White** shows
`Tolerance = N/A` and `Minimum / Maximum = N/A`.

---

## 🖼️ Screenshot

```
┌─────────────────────────────────────────────────────────────┐
│  Language / Dil: [ English + Türkçe ▾ ]   Bands: ●4 ●5 ●6   │
├─────────────────────────────────────────────────────────────┤
│  Bands / Bantlar                                            │
│  Band/Bant 1 (Digit/Rakam):        [3 - Red (Kırmızı)  ▾]  │
│  Band/Bant 2 (Digit/Rakam):        [3 - Red (Kırmızı)  ▾]  │
│  Band/Bant 3 (Multiplier/Çarpan):  [2 - Brown (Kahv.)  ▾]  │
│  Band/Bant 4 (Tolerance/Tolerans): [11 - Gold (Altın)  ▾]  │
├─────────────────────────────────────────────────────────────┤
│  Results / Sonuçlar                                         │
│  Resistance / Direnç:                220 Ω                  │
│  Tolerance / Tolerans:               ±5 %                   │
│  Minimum:                            209 Ω                  │
│  Maximum / Maksimum:                 231 Ω                  │
│  Temperature Coefficient / …:        -                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Development

```bash
git clone https://github.com/WhiteSymmetry/r3cal.git
cd r3cal
pip install -e .
python -m r3cal
```

---

## 📄 License

AGPL-3.0 License — see [LICENSE](LICENSE).

---

## 🙏 Acknowledgements

Color tables follow the IEC 60062 standard and standard resistor datasheets.
Built with [Tkinter](https://docs.python.org/3/library/tkinter.html) only —
no third-party runtime dependencies.

---
---

# Türkçe

[English](#r3cal) | **Türkçe**

Python için **çok dilli**, modern bir **direnç renk kodu hesaplayıcısı**.
**4, 5 ve 6 bantlı** dirençleri destekler; N/A bantlar, canlı renk önizlemeleri
ve isteğe bağlı **iki dilli (EN/TR) arayüz** sunar. Hem **bağımsız bir GUI**
olarak hem de kendi Tkinter uygulamanıza **gömülebilir bir bileşen** olarak çalışır.

---

## 📦 Kurulum

```bash
pip install r3cal
```

```bash
conda install bilgi::r3cal -y
```

**Python 3.11+** gereklidir. Tkinter, Windows ve macOS'ta standart kütüphaneyle
birlikte gelir. Linux'ta ayrıca kurmanız gerekebilir:

```bash
sudo apt install python3-tk        # Debian / Ubuntu
sudo dnf install python3-tkinter   # Fedora
```

---

## ✨ Özellikler

| Özellik | Açıklama |
|---|---|
| 4 / 5 / 6 bant desteği | Radyo düğmeleriyle anında geçiş |
| Tam renk tabloları | Rakam, çarpan, tolerans, sıcaklık katsayısı — tüm N/A değerleri dâhil |
| Toleranslar | ±1, 2, 3, 4, 0.5, 0.25, 0.1, 0.05, 5, 10 % ve **Yok = ±20 %** |
| Sıcaklık katsayısı | 100, 50, 25, 15, 10, 5 ppm/°C (gerektiğinde N/A gösterilir) |
| Çok dilli arayüz | English / Türkçe / İki Dilli (aynı anda) |
| Esnek giriş | Açılır menü, renk numarası (1–13), İngilizce ad, Türkçe ad |
| Canlı önizleme | Her bant gerçek rengini bir kutuda gösterir |
| Akıllı format | Otomatik Ω / kΩ / MΩ / GΩ / mΩ / µΩ |
| Font ölçekleme | Yerleşik **A+ / A−** butonları |
| Gömülebilir | `Tk` penceresi *veya* `Frame` kabul eder |

---

## 🚀 Hızlı Başlangıç

### Bağımsız çalıştırma

```bash
python -m r3cal
```

veya

```python
import tkinter as tk
import r3cal

r3cal.R3Cal(tk.Tk())
tk.mainloop()
```

### Kendi pencerenize gömme

```python
import tkinter as tk
from tkinter import ttk
import r3cal

root = tk.Tk()
root.title("Uygulamam")
root.geometry("1000x800")

frame = ttk.Frame(root, padding=6)
frame.pack(fill="both", expand=True)

app = r3cal.R3Cal(frame)   # bir Frame içine göm
root.mainloop()
```

### Sınıfı doğrudan içe aktarma

```python
from r3cal import R3Cal
import tkinter as tk

R3Cal(tk.Tk())
tk.mainloop()
```

---

## 🎨 Kullanım

1. Üstten **4 / 5 / 6 bant** seçin.
2. Bir **dil** seçin: `English`, `Türkçe` veya `English + Türkçe`.
3. Her bant için **şunlardan herhangi birini** yapın:
   - Açılır menüden bir renk seçin, **veya**
   - **Renk numarasını** (`1`–`13`) yazıp Enter'a basın, **veya**
   - **İngilizce** adı yazın (`Red`), **veya**
   - **Türkçe** adı yazın (`Kırmızı`).
4. Sonuçlar **anında güncellenir**: direnç, tolerans, min/maks, tempco.
5. Alttaki **A+ / A−** butonlarıyla arayüz yazı boyutunu ölçekleyin.

### Renk numarası referansı

| # | English | Türkçe | Rol |
|---|---------|--------|-----|
| 1 | Black | Siyah | Rakam / Çarpan / N/A |
| 2 | Brown | Kahverengi | Rakam / Çarpan / Tolerans / Tempco |
| 3 | Red | Kırmızı | Rakam / Çarpan / Tolerans / Tempco |
| 4 | Orange | Turuncu | Rakam / Çarpan / Tolerans / Tempco |
| 5 | Yellow | Sarı | Rakam / Çarpan / Tolerans / Tempco |
| 6 | Green | Yeşil | Rakam / Çarpan / Tolerans |
| 7 | Blue | Mavi | Rakam / Çarpan / Tolerans / Tempco |
| 8 | Violet | Mor | Rakam / Çarpan / Tolerans / Tempco |
| 9 | Grey | Gri | Rakam / Çarpan / Tolerans |
| 10 | White | Beyaz | Rakam / Çarpan / N/A |
| 11 | Gold | Altın | Çarpan (×0.1) / Tolerans (±5 %) |
| 12 | Silver | Gümüş | Çarpan (×0.01) / Tolerans (±10 %) |
| 13 | None | Yok | Tolerans (±20 %) |

---

## 📚 API Referansı

### `class r3cal.R3Cal(container)`

Hesaplayıcı bileşenini oluşturur. `container` şunlardan biri olabilir:

- bir `tkinter.Tk` / `tkinter.Toplevel` → bağımsız pencere,
- bir `tkinter.ttk.Frame` → gömülü bileşen.

Örnek üzerinden erişilebilen öznitelikler:

| Öznitelik | Tür | Açıklama |
|---|---|---|
| `scale` | `float` | Geçerli font ölçeği (0.7–2.5). `_apply_geometry()`'den önce programatik olarak ayarlanabilir. |
| `lang` | `tk.StringVar` | Geçerli dil (`"en"`, `"tr"`, `"both"`). |
| `band_count` | `tk.IntVar` | Geçerli bant sayısı (4, 5, 6). |

### Renk tabloları (modül düzeyinde)

```python
from r3cal import DIGIT, MULTIPLIER, TOLERANCE, TEMPCO, COLORS
```

| İsim | Anlam |
|---|---|
| `DIGIT` | `{renk: 0..9}` |
| `MULTIPLIER` | `{renk: çarpan}` (Altın=0.1, Gümüş=0.01) |
| `TOLERANCE` | `{renk: yüzde veya None}` |
| `TEMPCO` | `{renk: ppm/°C veya None}` |
| `COLORS` | `{anahtar: {"en":…, "tr":…, "preview":…}}` |

### Yardımcı fonksiyonlar

```python
from r3cal import parse_color, fmt_resistance

parse_color("3")             # → "Red"
parse_color("Kırmızı")       # → "Red"
parse_color("1 - Black")     # → "Black"
fmt_resistance(2200)         # → "2.2 kΩ"
```

---

## 🧪 Örnekler

### 220 Ω, 4 bant (Kırmızı-Kırmızı-Kahverengi-Altın)

| Bant | Renk |
|---|---|
| 1 | Kırmızı |
| 2 | Kırmızı |
| 3 | Kahverengi |
| 4 | Altın |

**Sonuç:** `220 Ω ±5 %`, Min `209 Ω`, Maks `231 Ω`.

### 220 Ω, 6 bant — N/A tempco'lu

| Bant | Renk |
|---|---|
| 1–3 | Kırmızı-Kırmızı-Siyah |
| Çarpan | Siyah |
| Tolerans | Altın |
| Tempco | Yeşil |

**Sonuç:** `220 Ω ±5 %`, Tempco **N/A**.

### N/A tolerans

Toleransı **Siyah** veya **Beyaz** olan herhangi bir 4 bantlı direnç
`Tolerans = N/A` ve `Minimum / Maksimum = N/A` gösterir.

---

## 🖼️ Ekran Görüntüsü

```
┌─────────────────────────────────────────────────────────────┐
│  Language / Dil: [ English + Türkçe ▾ ]   Bands: ●4 ●5 ●6   │
├─────────────────────────────────────────────────────────────┤
│  Bands / Bantlar                                            │
│  Band/Bant 1 (Digit/Rakam):        [3 - Red (Kırmızı)  ▾]  │
│  Band/Bant 2 (Digit/Rakam):        [3 - Red (Kırmızı)  ▾]  │
│  Band/Bant 3 (Multiplier/Çarpan):  [2 - Brown (Kahv.)  ▾]  │
│  Band/Bant 4 (Tolerance/Tolerans): [11 - Gold (Altın)  ▾]  │
├─────────────────────────────────────────────────────────────┤
│  Results / Sonuçlar                                         │
│  Resistance / Direnç:                220 Ω                  │
│  Tolerance / Tolerans:               ±5 %                   │
│  Minimum:                            209 Ω                  │
│  Maximum / Maksimum:                 231 Ω                  │
│  Temperature Coefficient / …:        -                      │
└─────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Geliştirme

```bash
git clone https://github.com/<kullanıcı>/r3cal.git
cd r3cal
pip install -e .
python -m r3cal
```

---

## 📄 Lisans

AGPL-3.0 Lisansı — ayrıntılar için [LICENSE](LICENSE).

---

## 🙏 Teşekkür

Renk tabloları IEC 60062 standardını ve standart direnç veri sayfalarını
takip eder. Yalnızca [Tkinter](https://docs.python.org/3/library/tkinter.html)
ile inşa edilmiştir — üçüncü taraf çalışma zamanı bağımlılığı yoktur.
```

---

## Notlar

- **`python -m r3cal`** komutunun çalışması için `r3cal/__main__.py` dosyası gerekir:

```python
# r3cal/__main__.py
import tkinter as tk
from .r3cal import R3Cal

R3Cal(tk.Tk())
tk.mainloop()
```

---

# Pixi:

[![Pixi](https://img.shields.io/badge/Pixi-Pixi-brightgreen.svg)](https://prefix.dev/channels/bilgi)

pixi init r3cal

cd r3cal

pixi workspace channel add https://repo.prefix.dev/bilgi --prepend

✔ Added https://repo.prefix.dev/bilgi

pixi add r3cal

✔ Added r3cal >=0.1.2,<2

pixi install

pixi shell

pixi run python -c "import r3cal; print(r3cal.__version__)"

### Çıktı: 0.1.2

pixi remove r3cal

conda install -c https://prefix.dev/bilgi r3cal

pixi run python -c "import r3cal; print(r3cal.__version__)"

### Çıktı: 0.1.2

pixi run pip list | grep r3cal

### r3cal  0.1.2

pixi run pip show r3cal

Name: r3cal

Version: 0.1.2

Summary: r3cal: Resistor Color Code Calculator: Direnç Renk Kodu Hesaplayıcı

Home-page: https://github.com/WhiteSymmetry/r3cal

Author: Mehmet Keçeci

Author-email: Mehmet Keçeci <...>

License: AGPL-3.0-or-later License

Copyright (c) 2026 Mehmet Keçeci

## Citation

If this library was useful to you in your research, please cite us. Following the [GitHub citation standards](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files), here is the recommended citation.

https://github.com/WhiteSymmetry/r3cal

https://pypi.org/project/r3cal

https://prefix.dev/channels/bilgi/packages/r3cal

https://anaconda.org/channels/bilgi/packages/r3cal

### BibTeX


### APA

```
Keçeci, M. (2026). r3cal: Çok Dilli, Gömülebilir ve Standartlara Uygun Bir Direnç Renk Kodu Hesaplayıcı Kütüphanesi. Open Science Articles (OSAs), Zenodo. https://doi.org/10.5281/zenodo.23251543

```
