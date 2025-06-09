from typing import Optional

from dataclasses import asdict
from dataclasses import dataclass

from docx.shared import Pt
from docx.shared import Cm
from docx.shared import Mm
from docx.shared import Emu
from docx.shared import Twips
from docx.shared import Inches
from docx.shared import RGBColor

from docx.enum.text import WD_BREAK as break_type
from docx.enum.text import WD_COLOR as color_name
from docx.enum.text import WD_TAB_LEADER as tab_leader
from docx.enum.text import WD_TAB_ALIGNMENT as tab_align
from docx.enum.text import WD_UNDERLINE as underline_type
from docx.enum.text import WD_LINE_SPACING as line_spacing
from docx.enum.text import WD_ALIGN_PARAGRAPH as paragraph_align

from docx.styles.style import BaseStyle
from docx.text.paragraph import Paragraph

from docx.enum.style import WD_STYLE
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.dml import MSO_COLOR_TYPE
from docx.enum.dml import MSO_THEME_COLOR
from docx.enum.shape import WD_INLINE_SHAPE


WD_STYLE_TYPE.CHARACTER

@dataclass
class TextStyle(BaseStyle):
    """Text style for Word documents
    
    Attributes:

    """
    text_size: Pt = Pt(14.0)
    text_name: str = "Times New Roman"
    text_color: Optional[RGBColor] = None
    highlight_color: Optional[color_name] = color_name.INHERITED
    underline: Optional[underline_type] = None
    bold: bool = None
    italic: bool = None
    outline: bool = None
    all_caps: bool = None
    small_caps: bool = None
    strike: bool = None
    double_strike: bool = None
    subscript: bool = None
    superscript: bool = None
    complex_script: bool = None
    cs_bold: bool = None
    cs_italic: bool = None
    emboss: bool = None
    hidden: bool = None
    imprint: bool = None
    math: bool = None
    snap_to_grid: bool = None
    spec_vanish: bool = None
    no_proof: bool = None
    rtl: bool = None
    shadow: bool = None
    web_hidden: bool  = None

    def get_style_dict(self) -> dict:
        """Return dict with all text style parametres"""
        style_dict = asdict(self)
        return style_dict
    
    def __repr__(self):
        return "Dataclass TextStyle"


@dataclass
class ParagraphStyle(BaseStyle):
    """Paragraph style for Word Document
    
    Attributes:

    """
    alignment: paragraph_align = paragraph_align.LEFT
    line_space: Optional[line_spacing] = line_spacing.SINGLE
    tab_leadment: Optional[tab_leader] = tab_leader.SPACES
    p_break: Optional[break_type] = None
    tab_alignment: Optional[tab_align] = None

    space_before: Optional[Pt] = None
    space_after: Optional[Pt] = None
    first_line_indent : Optional[Pt] = None
    left_indent: Optional[Pt] = None
    right_indent: Optional[Pt] = None
    keep_together: bool = False
    page_break_before: bool = False
    text_direction: str = 'ltr' # ltr = left to right

    def get_style_dict(self) -> dict:
        """Return dict with all paragraph style parametres"""
        style_dict = asdict(self)
        return style_dict


@dataclass
class SectionStyle(BaseStyle):
    pass 


@dataclass
class Image(BaseStyle):
    pass


@dataclass
class CellStyle(BaseStyle):
    pass


@dataclass
class TableStyle(BaseStyle):
    pass
