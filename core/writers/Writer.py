from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.doc import DOC

from core.writers.SectionWriter import SectionWriter
from core.writers.ParagraphWriter import ParagraphWriter
from core.doc_objects.Paragraph import Paragraph


class Writer(SectionWriter, ParagraphWriter):
    """Class provides method to writing DOCObjects into document word"""
    def __init__(self, doc: 'DOC'):
        super().__init__(doc=doc)
    def add(self, obj):
        if isinstance(obj, Paragraph):
            self.add_paragraph(obj)
