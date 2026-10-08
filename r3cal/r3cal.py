# -*- coding: utf-8 -*-
# r3cal.py

import tkinter as tk
from tkinter import ttk

# ==================== RENK VERİLERİ ====================
COLORS = {
    "Black":  {"en": "Black",  "tr": "Siyah",      "preview": "#000000"},
    "Brown":  {"en": "Brown",  "tr": "Kahverengi", "preview": "#7B3F00"},
    "Red":    {"en": "Red",    "tr": "Kırmızı",    "preview": "#E60000"},
    "Orange": {"en": "Orange", "tr": "Turuncu",    "preview": "#FF8C00"},
    "Yellow": {"en": "Yellow", "tr": "Sarı",       "preview": "#FFD700"},
    "Green":  {"en": "Green",  "tr": "Yeşil",      "preview": "#007F00"},
    "Blue":   {"en": "Blue",   "tr": "Mavi",       "preview": "#0000D0"},
    "Violet": {"en": "Violet", "tr": "Mor",        "preview": "#8A2BE2"},
    "Grey":   {"en": "Grey",   "tr": "Gri",        "preview": "#808080"},
    "White":  {"en": "White",  "tr": "Beyaz",      "preview": "#FFFFFF"},
    "Gold":   {"en": "Gold",   "tr": "Altın",      "preview": "#DAA520"},
    "Silver": {"en": "Silver", "tr": "Gümüş",      "preview": "#C0C0C0"},
    "None":   {"en": "None",   "tr": "Yok",        "preview": "#E8E8E8"},
}
COLOR_ORDER = ["Black", "Brown", "Red", "Orange", "Yellow", "Green",
               "Blue", "Violet", "Grey", "White", "Gold", "Silver", "None"]
NUM_TO_COLOR = {i + 1: c for i, c in enumerate(COLOR_ORDER)}
COLOR_TO_NUM = {c: i + 1 for i, c in enumerate(COLOR_ORDER)}

# ==================== DEĞER TABLOLARI ====================
DIGIT = {"Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
         "Green": 5, "Blue": 6, "Violet": 7, "Grey": 8, "White": 9}

MULTIPLIER = {"Black": 1, "Brown": 10, "Red": 100, "Orange": 1e3,
              "Yellow": 1e4, "Green": 1e5, "Blue": 1e6, "Violet": 1e7,
              "Grey": 1e8, "White": 1e9, "Gold": 0.1, "Silver": 0.01}

TOLERANCE = {"Black": None, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
             "Green": 0.5, "Blue": 0.25, "Violet": 0.1, "Grey": 0.05,
             "White": None, "Gold": 5, "Silver": 10, "None": 20}

TEMPCO = {"Black": None, "Brown": 100, "Red": 50, "Orange": 15, "Yellow": 25,
          "Green": None, "Blue": 10, "Violet": 5, "Grey": None, "White": None}

VALID_COLORS_FOR = {
    "digit":      ["Black", "Brown", "Red", "Orange", "Yellow", "Green",
                   "Blue", "Violet", "Grey", "White"],
    "multiplier": ["Black", "Brown", "Red", "Orange", "Yellow", "Green",
                   "Blue", "Violet", "Grey", "White", "Gold", "Silver"],
    "tolerance":  ["Black", "Brown", "Red", "Orange", "Yellow", "Green",
                   "Blue", "Violet", "Grey", "White", "Gold", "Silver", "None"],
    "tempco":     ["Black", "Brown", "Red", "Orange", "Yellow", "Green",
                   "Blue", "Violet", "Grey", "White"],
}

BAND_MAP = {
    4: [("d1", "digit"), ("d2", "digit"),
        ("mult", "multiplier"), ("tol", "tolerance")],
    5: [("d1", "digit"), ("d2", "digit"), ("d3", "digit"),
        ("mult", "multiplier"), ("tol", "tolerance")],
    6: [("d1", "digit"), ("d2", "digit"), ("d3", "digit"),
        ("mult", "multiplier"), ("tol", "tolerance"), ("tempco", "tempco")],
}

# ==================== ÇOKLU DİL STRINGLERİ ====================
STRINGS = {
    "app_title":       {"en": "Resistor Color Code Calculator",
                        "tr": "Direnç Renk Kodu Hesaplayıcı"},
    "language_label":  {"en": "Language:", "tr": "Dil:"},
    "band_count":      {"en": "Number of bands:", "tr": "Bant sayısı:"},
    "bands_word":      {"en": "bands", "tr": "bant"},
    "bands_section":   {"en": "Bands", "tr": "Bantlar"},
    "results_section": {"en": "Results", "tr": "Sonuçlar"},
    "resistance":      {"en": "Resistance", "tr": "Direnç"},
    "tolerance":       {"en": "Tolerance", "tr": "Tolerans"},
    "minimum":         {"en": "Minimum", "tr": "Minimum"},
    "maximum":         {"en": "Maximum", "tr": "Maksimum"},
    "tempco":          {"en": "Temperature Coefficient", "tr": "Sıcaklık Katsayısı"},
    "type_digit":      {"en": "Digit", "tr": "Rakam"},
    "type_multiplier": {"en": "Multiplier", "tr": "Çarpan"},
    "type_tolerance":  {"en": "Tolerance", "tr": "Tolerans"},
    "type_tempco":     {"en": "Temp. Coef.", "tr": "Sıc. Kats."},
    "hint":            {"en": "Hint: Type a color number (1–13) or a color name (EN/TR), then press Enter.",
                        "tr": "İpucu: Renk numarasını (1–13) veya renk adını (EN/TR) yazıp Enter'a basın."},
    "na":              {"en": "N/A", "tr": "N/A"},
}

LANG_OPTIONS = [("en", "English"), ("tr", "Türkçe"), ("both", "English + Türkçe")]


# ==================== ÇEVİRİ / GÖRÜNTÜLEME ====================
def t(key, lang):
    e = STRINGS.get(key)
    if e is None:
        return key
    en, tr = e["en"], e["tr"]
    if lang == "en":
        return en
    if lang == "tr":
        return tr
    if en == tr:
        return en
    return f"{en} / {tr}"


def color_display(key, lang):
    c = COLORS[key]
    if lang == "en":
        return c["en"]
    if lang == "tr":
        return c["tr"]
    return f"{c['en']} ({c['tr']})"


def combo_display(key, lang):
    return f"{COLOR_TO_NUM[key]} - {color_display(key, lang)}"


def band_label(num, band_type, lang):
    en_t = STRINGS["type_" + band_type]["en"]
    tr_t = STRINGS["type_" + band_type]["tr"]
    if lang == "en":
        return f"Band {num} ({en_t})"
    if lang == "tr":
        return f"Bant {num} ({tr_t})"
    return f"Band/Bant {num} ({en_t}/{tr_t})"


def parse_color(text):
    if not text:
        return None
    s = text.strip()
    if " - " in s:
        head = s.split(" - ", 1)[0].strip()
        if head.isdigit():
            return NUM_TO_COLOR.get(int(head))
    if s.isdigit():
        return NUM_TO_COLOR.get(int(s))
    low = s.lower()
    for key, c in COLORS.items():
        if c["en"].lower() == low or c["tr"].lower() == low:
            return key
        if f"{c['en']} ({c['tr']})".lower() == low:
            return key
    return None


def fmt_resistance(val):
    if val is None:
        return "N/A"
    if val >= 1e9:  return f"{val / 1e9:.4g} GΩ"
    if val >= 1e6:  return f"{val / 1e6:.4g} MΩ"
    if val >= 1e3:  return f"{val / 1e3:.4g} kΩ"
    if val >= 1:    return f"{val:.4g} Ω"
    if val >= 1e-3: return f"{val * 1e3:.4g} mΩ"
    return f"{val * 1e6:.4g} µΩ"


# ==================== UYGULAMA ====================
class r3cal:
    # ---------- VARSAYILAN FONT BOYUTLARI ----------
    BASE_UI     = 11   # Label, Combobox, Radiobutton, Button, Entry
    BASE_HINT   = 11   # İpucu ve renk listesi satırları
    BASE_TITLE  = 12   # Bölüm başlıkları (Bands / Results)
    BASE_RESULT = 12   # Sonuç değerleri

    def __init__(self, root):
        self.root = root

        # ---------- Ölçek ----------
        self.scale = 1.0   # A+/A− butonları bunu değiştirir; 1.0 = yukarıdaki sabit boyutlar

        self.style = ttk.Style()
        try:
            self.style.theme_use("clam")
        except tk.TclError:
            pass

        self._configure_styles()

        # ---------- Durum ----------
        self.lang = tk.StringVar(value="both")
        self.band_count = tk.IntVar(value=4)

        self.band_values = {
            "d1": "Red", "d2": "Red", "d3": "Black",
            "mult": "Brown", "tol": "Gold", "tempco": "Brown",
        }
        self.current_band_map = []
        self.band_vars, self.band_combos = [], []
        self.band_previews, self.band_frames, self.band_labels = [], [], []

        # ---------- Arayüz ----------
        self._build_ui()
        self._apply_geometry()
        self.apply_language()

    # ---------- Font / Stil ----------
    def _configure_styles(self):
        s = self.scale
        ui     = max(6, int(round(self.BASE_UI     * s)))
        hint   = max(6, int(round(self.BASE_HINT   * s)))
        title  = max(7, int(round(self.BASE_TITLE  * s)))
        result = max(6, int(round(self.BASE_RESULT * s)))

        st = self.style
        st.configure(".",                 font=("TkDefaultFont", ui))
        st.configure("TLabel",            font=("TkDefaultFont", ui))
        st.configure("TButton",           font=("TkDefaultFont", ui))
        st.configure("TRadiobutton",      font=("TkDefaultFont", ui))
        st.configure("TCombobox",         font=("TkDefaultFont", ui))
        st.configure("TLabelframe.Label", font=("TkDefaultFont", title, "bold"))
        st.configure("Title.TLabel",      font=("TkDefaultFont", title, "bold"))
        st.configure("Hint.TLabel",       font=("TkDefaultFont", hint))
        st.configure("Result.TLabel",     font=("TkDefaultFont", result, "bold"))

        # Combobox'ın AÇILIR LİSTESİ için ayrı font ayarı
        self.root.option_add("*TCombobox*Listbox.font", ("TkDefaultFont", ui))
        self.root.option_add("*TCombobox*Font",          ("TkDefaultFont", ui))

    def _apply_geometry(self):
        s = self.scale
        w = int(1150 * max(1.0, s * 0.85))
        h = int(790 * max(1.0, s * 0.80))
        self.root.geometry(f"{w}x{h}")
        self.root.minsize(int(700 * max(1.0, s * 0.85)),
                          int(680 * max(1.0, s * 0.80)))

        band_lbl_w   = int(34 * s) if s >= 1.0 else 34
        combo_w      = int(30 * s) if s >= 1.0 else 30
        result_hdr_w = int(40 * s) if s >= 1.0 else 40
        preview_w    = max(3, int(3 * s))

        for lbl in self.band_labels:
            lbl.config(width=band_lbl_w)
        for cb in self.band_combos:
            cb.config(width=combo_w)
        for pv in self.band_previews:
            pv.config(width=preview_w, height=1)
        for hdr in self.result_headers.values():
            hdr.config(width=result_hdr_w)

        self.hint_label.config(wraplength=max(600, w - 40))

    # ---------- Arayüz ----------
    def _build_ui(self):
        # Üst bar
        top = ttk.Frame(self.root, padding=10)
        top.pack(fill="x")

        self.lang_label = ttk.Label(top, text="Language / Dil:")
        self.lang_label.pack(side="left", padx=(0, 5))

        self.lang_combo = ttk.Combobox(top, state="readonly", width=22)
        self.lang_combo["values"] = [lbl for _, lbl in LANG_OPTIONS]
        self.lang_combo.current(2)
        self.lang_combo.pack(side="left", padx=(0, 20))
        self.lang_combo.bind("<<ComboboxSelected>>", self._on_lang_change)

        self.band_count_label = ttk.Label(top, text="Number of bands:")
        self.band_count_label.pack(side="left", padx=(0, 5))
        self.radio_buttons = {}
        for n in (4, 5, 6):
            rb = ttk.Radiobutton(top, text=str(n), variable=self.band_count,
                                 value=n, command=self.update_bands)
            rb.pack(side="left", padx=3)
            self.radio_buttons[n] = rb

        # Bantlar
        self.bands_frame = ttk.LabelFrame(self.root, text="Bands", padding=10)
        self.bands_frame.pack(fill="x", padx=10, pady=(0, 5))

        for i in range(6):
            row = ttk.Frame(self.bands_frame)

            lbl = ttk.Label(row, text="", width=34, anchor="w")
            lbl.pack(side="left")

            preview = tk.Label(row, width=3, height=1, bg="#EEEEEE",
                               relief="solid", borderwidth=1)
            preview.pack(side="left", padx=(0, 8))

            var = tk.StringVar()
            combo = ttk.Combobox(row, textvariable=var, state="normal", width=30)
            combo.pack(side="left", fill="x", expand=True)
            combo.bind("<<ComboboxSelected>>", lambda e, idx=i: self._commit(idx))
            combo.bind("<Return>",              lambda e, idx=i: self._commit(idx))
            combo.bind("<FocusOut>",            lambda e, idx=i: self._commit(idx))

            self.band_vars.append(var)
            self.band_combos.append(combo)
            self.band_previews.append(preview)
            self.band_frames.append(row)
            self.band_labels.append(lbl)

        self.hint_label = ttk.Label(self.root, style="Hint.TLabel",
                                    foreground="gray", justify="left",
                                    wraplength=780)
        self.hint_label.pack(anchor="w", padx=14, pady=(0, 5))

        # Sonuçlar
        self.results_frame = ttk.LabelFrame(self.root, text="Results", padding=12)
        self.results_frame.pack(fill="both", expand=True, padx=10, pady=(5, 5))

        self.result_headers = {}
        self.result_values = {}
        for key in ("resistance", "tolerance", "minimum", "maximum", "tempco"):
            r = ttk.Frame(self.results_frame)
            r.pack(fill="x", pady=4)
            h = ttk.Label(r, text="", width=40, anchor="w")
            h.pack(side="left")
            v = ttk.Label(r, text="-", style="Result.TLabel")
            v.pack(side="left")
            self.result_headers[key] = h
            self.result_values[key] = v

        # Alt bar: A− / A+
        bottom = ttk.Frame(self.root, padding=(10, 0, 10, 10))
        bottom.pack(fill="x")

        ttk.Button(bottom, text="A+", width=4,
                   command=lambda: self._change_scale(+0.1)
                   ).pack(side="right", padx=2)
        ttk.Button(bottom, text="A−", width=4,
                   command=lambda: self._change_scale(-0.1)
                   ).pack(side="right", padx=2)

    # ---------- Ölçek değişimi ----------
    def _change_scale(self, delta):
        self.scale = max(0.7, min(2.5, round(self.scale + delta, 2)))
        self._configure_styles()
        self._apply_geometry()
        self.apply_language()

    # ---------- Olaylar ----------
    def _on_lang_change(self, _event=None):
        self.lang.set(LANG_OPTIONS[self.lang_combo.current()][0])
        self.apply_language()

    def update_bands(self):
        self.apply_language()

    def _commit(self, i):
        if i >= len(self.current_band_map):
            return
        vkey, btype = self.current_band_map[i]
        valid = VALID_COLORS_FOR[btype]
        c = parse_color(self.band_vars[i].get())
        if c is None or c not in valid:
            c = self.band_values[vkey]
            if c is None or c not in valid:
                c = self._default_for(btype)
        self.band_values[vkey] = c
        self.band_vars[i].set(combo_display(c, self.lang.get()))
        self._update_preview(i)
        self.calculate()

    def _update_preview(self, i):
        if i >= len(self.current_band_map):
            return
        vkey, _ = self.current_band_map[i]
        c = self.band_values[vkey]
        self.band_previews[i].config(bg=COLORS[c]["preview"] if c else "#EEEEEE")

    @staticmethod
    def _default_for(btype):
        return {"digit": "Red", "multiplier": "Brown",
                "tolerance": "Gold", "tempco": "Brown"}.get(btype, "Black")

    # ---------- Dil uygulama ----------
    def apply_language(self):
        lang = self.lang.get()
        count = self.band_count.get()
        self.current_band_map = BAND_MAP[count]

        # Başlıklar
        self.root.title(t("app_title", lang))
        self.lang_label.config(text="Language / Dil:")
        self.band_count_label.config(text=t("band_count", lang))
        for n, rb in self.radio_buttons.items():
            rb.config(text=f"{n} {t('bands_word', lang)}")
        self.bands_frame.config(text=t("bands_section", lang))
        self.results_frame.config(text=t("results_section", lang))

        for key, h in self.result_headers.items():
            h.config(text=t(key, lang) + ":")

        # İpucu — 3 renk satırı (5 + 4 + 4)
        color_lines = []
        group_sizes = (5, 4, 4)
        idx = 1
        for size in group_sizes:
            chunk = COLOR_ORDER[idx - 1: idx - 1 + size]
            line = " · ".join(f"{i} {color_display(c, lang)}"
                              for i, c in enumerate(chunk, start=idx))
            color_lines.append(line)
            idx += size
        self.hint_label.config(
            text=t("hint", lang) + "\n" + "\n".join(color_lines))

        # Bantlar
        for i in range(6):
            if i < count:
                vkey, btype = self.current_band_map[i]
                self.band_labels[i].config(
                    text=band_label(i + 1, btype, lang) + ":")
                self.band_combos[i]["values"] = [
                    combo_display(c, lang) for c in VALID_COLORS_FOR[btype]
                ]
                self.band_vars[i].set(
                    combo_display(self.band_values[vkey], lang))
                self.band_frames[i].pack(fill="x", pady=3)
                self._update_preview(i)
            else:
                self.band_frames[i].pack_forget()

        self.calculate()

    # ---------- Hesaplama ----------
    def calculate(self):
        count = self.band_count.get()
        try:
            v = self.band_values
            tempco_val = None

            if count == 4:
                d1, d2 = DIGIT[v["d1"]], DIGIT[v["d2"]]
                value = (d1 * 10 + d2) * MULTIPLIER[v["mult"]]
                tol_val = TOLERANCE[v["tol"]]
            elif count == 5:
                d1, d2, d3 = DIGIT[v["d1"]], DIGIT[v["d2"]], DIGIT[v["d3"]]
                value = (d1 * 100 + d2 * 10 + d3) * MULTIPLIER[v["mult"]]
                tol_val = TOLERANCE[v["tol"]]
            else:
                d1, d2, d3 = DIGIT[v["d1"]], DIGIT[v["d2"]], DIGIT[v["d3"]]
                value = (d1 * 100 + d2 * 10 + d3) * MULTIPLIER[v["mult"]]
                tol_val = TOLERANCE[v["tol"]]
                tempco_val = TEMPCO[v["tempco"]]

            self.result_values["resistance"].config(text=fmt_resistance(value))

            if tol_val is None:
                self.result_values["tolerance"].config(text="N/A")
                self.result_values["minimum"].config(text="N/A")
                self.result_values["maximum"].config(text="N/A")
            else:
                self.result_values["tolerance"].config(text=f"±{tol_val} %")
                self.result_values["minimum"].config(
                    text=fmt_resistance(value * (1 - tol_val / 100)))
                self.result_values["maximum"].config(
                    text=fmt_resistance(value * (1 + tol_val / 100)))

            if count == 6:
                self.result_values["tempco"].config(
                    text="N/A" if tempco_val is None
                    else f"{tempco_val} ppm/°C")
            else:
                self.result_values["tempco"].config(text="-")
        except Exception:
            for k in self.result_values:
                self.result_values[k].config(text="-")


if __name__ == "__main__":
    root = tk.Tk()
    r3cal(root)
    root.mainloop()
