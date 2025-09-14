from typing import Optional

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
from docx.shared import RGBColor
from docx.text.paragraph import Paragraph

from core.styles.base import BaseStyle


class TextStyle(BaseStyle):
    """Класс стилей для текста

    Args:
        BaseStyle (_type_): базовый класс стилей
    """

    _style_attrs = {
        "text_size": (),
        "text_name": (),
        "text_color": (),
        "highlight_color": (),
        "underline": (),
        "bold": (),
        "italic": (),
        "outline": (),
        "all_caps": (),
        "small_caps": (),
        "strike": (),
        "double_strike": (),
        "subscript": (),
        "superscript": (),
        "complex_script": (),
        "cs_bold": (),
        "cs_italic": (),
        "emboss": (),
        "hidden": (),
        "imprint": (),
        "math": (),
        "snap_to_grid": (),
        "spec_vanish": (),
        "no_proof": (),
        "shadow": (),
        "web_hidden": (),
    }

    text_size = Optional[]
    text_name = Optional[]
    text_color = Optional[]
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

        super().__init__(kwargs)
