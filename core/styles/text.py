from typing import Optional, Union

from docx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR
from docx.enum.shape import WD_INLINE_SHAPE
from docx.enum.style import WD_STYLE, WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.text import WD_BREAK
from docx.enum.text import WD_COLOR
from docx.enum.text import WD_LINE_SPACING
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.enum.text import WD_TAB_LEADER
from docx.enum.text import WD_UNDERLINE
from docx.enum.text import WD_COLOR_INDEX
from docx.oxml.text.font import (
    CT_Color,
    CT_Fonts,
    CT_Highlight,
    CT_HpsMeasure,
    CT_RPr,
    CT_Underline,
    CT_VerticalAlignRun,
)
from docx.oxml.text.run import (
    CT_R,
    CT_Text,
    CT_PTab,
    CT_Br,
    CT_Cr,
    CT_NoBreakHyphen,
)
from docx.shared import RGBColor, Length
from docx.text.paragraph import Paragraph

from core.styles.base import BaseStyle
from docx.oxml.simpletypes import ST_VerticalAlignRun


class TextStyle(BaseStyle):
    """Style class for text"""

    # TODO: The class hasn't been completed yet! I haven’t fully figured it out yet.

    _style_attrs = {
        "text_size": ("", ""),  #
        "text_name": ("", ""),  #
        "text_color": ("_color", ""),  #
        "highlight_color": ("_highlight", "val"),
        "underline": ("_underline", "val"),
        "bold": ("_rPr", "b"),
        "italic": ("_rPr", "i"),
        "outline": ("_rPr", "outline"),
        "all_caps": ("_rPr", "caps"),
        "small_caps": ("_rPr", "smallCaps"),
        "strike": ("_rPr", "strike"),
        "double_strike": ("_rPr", "dstrike"),
        "subscript": ("_rPr", ""),  #
        "superscript": ("_rPr", ""),  #
        "complex_script": ("", ""),  #
        "cs_bold": ("_rPr", "bCs"),
        "cs_italic": ("_rPr", "iCs"),
        "emboss": ("_rPr", "emboss"),
        "hidden": ("_rPr", ""),  #
        "imprint": ("_rPr", "imprint"),
        "math": ("_rPr", "oMath"),
        "snap_to_grid": ("_rPr", "snapToGrid"),
        "spec_vanish": ("_rPr", "specVanish"),
        "no_proof": ("_rPr", "noProof"),
        "shadow": ("_rPr", "shadow"),
        "web_hidden": ("_rPr", "webHidden"),
        "vertical_alignment": ("_rPr", "vertAlign"),
        "right_to_left": ("_rPr", "rtl"),
    }

    text_size = Optional[Union[Length, int]]
    font_name = Optional[str]  #
    text_color = Optional[RGBColor]
    highlight_color = Optional[WD_COLOR_INDEX]
    underline = Optional[WD_UNDERLINE]
    bold = Optional[bool]
    italic = Optional[bool]
    outline = Optional[bool]
    all_caps = Optional[bool]
    small_caps = Optional[bool]
    strike = Optional[bool]
    double_strike = Optional[bool]
    subscript = Optional[bool]
    superscript = Optional[bool]
    complex_script = Optional[bool]
    cs_bold = Optional[bool]
    cs_italic = Optional[bool]
    emboss = Optional[bool]
    hidden = Optional[bool]
    imprint = Optional[bool]
    math = Optional[bool]
    snap_to_grid = Optional[bool]
    spec_vanish = Optional[bool]
    no_proof = Optional[bool]
    shadow = Optional[bool]
    web_hidden = Optional[bool]
    vertical_alignment = Optional[ST_VerticalAlignRun]
    right_to_left = Optional[bool]

    NAMESPACE: str = "r"

    def __init__(self, **kwargs):
        self._r = CT_R
        self._rPr = CT_RPr
        self._t = CT_Text
        self._highlight = CT_Highlight
        self._sz = CT_HpsMeasure
        self._br = CT_Br
        self._ptab = CT_PTab
        self._cr = CT_Cr
        self._noBreakHyphen = CT_NoBreakHyphen
        self._underline = CT_Underline
        self._color = CT_Color

        super().__init__(kwargs)
