from typing import Optional, Union

from docx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR
from docx.enum.shape import WD_INLINE_SHAPE
from docx.enum.style import WD_STYLE, WD_STYLE_TYPE
from docx.enum.text import (
    WD_ALIGN_PARAGRAPH,
    WD_BREAK,
    WD_COLOR,
    WD_LINE_SPACING,
    WD_TAB_ALIGNMENT,
    WD_TAB_LEADER,
    WD_UNDERLINE,
)
from docx.oxml.text.paragraph import CT_P
from docx.oxml.text.parfmt import CT_Ind, CT_Jc, CT_PPr, CT_Spacing, CT_TabStop
from docx.oxml.text.run import CT_R, CT_Text
from docx.shared import Cm, Emu, Inches, Length, Mm, Pt, RGBColor, Twips
from docx.styles.style import BaseStyle


class ParagraphStyle(BaseStyle):
    """Style class for paragraph"""

    _style_attrs = {
        "alignment": ("_jc", "val"),
        "tab_leadment": ("_tab", "leader"),
        "tab_alignment": ("_tab", "val"),
        "p_break": ("_p", "p_break"),
        "line_space": ("", ""),
        "space_before": ("_sp", ""),
        "space_after": ("_sp", ""),
        "first_line_indent": ("_ind", "firstLine"),
        "left_indent": ("_ind", "left"),
        "right_indent": ("_ind", "right"),
        "hanging_indent": ("_ind", "hanging"),
        "keep_together": ("", ""),
        "page_break_before": ("", ""),
    }

    alignment: Optional[WD_ALIGN_PARAGRAPH] = WD_ALIGN_PARAGRAPH.LEFT
    line_space: Optional[WD_LINE_SPACING] = WD_LINE_SPACING.SINGLE
    tab_leadment: Optional[WD_TAB_LEADER] = WD_TAB_LEADER.SPACES
    tab_alignment: Optional[WD_TAB_ALIGNMENT]
    p_break: Optional[WD_BREAK]
    space_before: Optional[Union[Length, int]]
    space_after: Optional[Union[Length, int]]
    first_line_indent: Optional[Union[Length, int]]
    left_indent: Optional[Union[Length, int]]
    right_indent: Optional[Union[Length, int]]
    hanging_indent: Optional[Union[Length, int]]
    keep_together: bool = False
    page_break_before: bool = False

    NAMESPACE: str = "p"

    def __init__(self, **kwargs):
        """
        - <w:p> - container for paragraphs. All xml elements containing a paragraph will be located inside it.
        - <w:pPr> - container for all properties of the paragraph object.
        - <w:ind> - element for marking indents.
        - <w:jc> - element to indicate alignment.
        - <w:r> - container for text. All xml elements related to the text will be located inside it.
        Always located inside a paragraph, i.e. inside <w:p>.
        - <w:t> - the text itself is written inside this tag..
        """

        self._p = CT_P  # <w:p>
        self._pPr = CT_PPr  # <w:pPr>
        self._ind = CT_Ind  # <w:ind>
        self._jc = CT_Jc  # <w:jc>
        self._sp = CT_Spacing  # <w:spacing>
        self._tab = CT_TabStop  # <w:tab>
        self._r = CT_R  # <w:r>
        self._t = CT_Text  # <w:t>

        super().__init__(kwargs)
