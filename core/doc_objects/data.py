from dataclasses import dataclass
from decimal import Decimal
from docx.shared import RGBColor, Pt
from typing import Optional
from docx.enum.text import WD_COLOR_INDEX
from docx.enum.text import WD_COLOR
from docx.enum.text import WD_UNDERLINE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.styles.style import BaseStyle
from docx.text.paragraph import Paragraph
from docx.text.run import Run


@dataclass
class TextStyle(BaseStyle):
    """Text style for Word documents
    
    Attributes (directly for text):
        text_size (Decimal)
        text_name (str): font name
        text_color (RGBColor)
        highlight_color (WD_COLOR_INDEX)
        bold (bool)
        italic (bool)
        underline (bool)
        strike (bool)
    
    Attributes (for paragraphs):
        alignment (str)
        line_spacing (Decimal)
        space_before 
        space_after
        left_indent
        right_indent
        keep_together
        page_bereak_before
        text_direction

    """
    double_strike: bool = False
    text_size: Decimal = Decimal("14.0")
    text_name: str = "Times New Roman"
    text_color: Optional[RGBColor] = None
    highlight_color: Optional[WD_COLOR_INDEX] = None
    bold: bool = False
    italic: bool = False
    underline: Optional[WD_UNDERLINE] = None
    strike: bool = None
    subscript: bool = None
    superscript: bool = None

    alignment: str = "center"
    line_spacing: Optional[Decimal] = None
    space_before: Optional[Pt] = None
    space_after: Optional[Pt] = None
    left_indent: Optional[Pt] = None
    right_indent: Optional[Pt] = None
    keep_together: bool = False
    page_break_before: bool = False
    text_direction: str = None


    def apply_to_run(self, run: Run):
        """Set style for text (runs)"""
        font = run.font
        font.size = self.text_size
        font.name = self.text_name
        font.color = self.text_color
        font.bold = self.bold
        font.italic = self.italic
        font.underline = self.underline
        font.strike = self.strike
        font.double_strike = self.double_strike

    def apply_to_paragraph(self, paragraph: Paragraph):
        """Set style for paragraphs"""
        paragraph_format = paragraph.paragraph_format
        if self.alignment == "left":
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        elif self.alignment == "right":
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        else:
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

        for run in paragraph.runs:
            self.apply_to_run(run)


class SectionStyle(BaseStyle):
    pass 

class Image(BaseStyle):
    pass


class CellStyle(BaseStyle):
    pass


class TableStyle(BaseStyle):
    pass
