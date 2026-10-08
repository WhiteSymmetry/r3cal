"""
r3cal: Resistor Color Code Calculator: Direnç Renk Kodu Hesaplayıcı
"""

__version__ = "0.1.2"
__author__ = "Mehmet Keçeci"
__main__ = "0.1.2"

from .r3cal import (
    # Temel eğri sınıfları
    R3Cal,
    t,
    color_display,
    combo_display,
    band_label,
    parse_color,
    fmt_resistance,
    DIGIT,
    MULTIPLIER,
    TOLERANCE,
    TEMPCO,
    COLORS,

)

__all__ = [
    "R3Cal",
    "t",
    "color_display",
    "combo_display",
    "band_label",
    "parse_color",
    "fmt_resistance",
    "DIGIT", 
    "MULTIPLIER",
    "TOLERANCE",
    "TEMPCO",
    "COLORS",

]
