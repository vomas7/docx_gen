from core.doc_objects.styles import ParagraphStyle
from docx.text.paragraph import Paragraph as ParentParagraph
from typing import Union


class Paragraph(ParentParagraph):
    def __init__(self, style: ParagraphStyle):
        self._style = style
        self._iid = None

    @property
    def iid(self):
        return self._iid
    
    @iid.setter
    def iid(self, value: int):
        if not isinstance(value, int):
            raise ValueError("IID must be integer")
        self._iid = value


p = Paragraph()
pp = ParentParagraph()

