from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.doc import DOC

from core.writers.SectionWriter import SectionWriter
from core.writers.ParagraphWriter import ParagraphWriter
from core.writers.TextWriter import TextWriter


class Writer(SectionWriter, ParagraphWriter, TextWriter):
    """Class provides method to writing DOCObjects into document word"""
    def __init__(self, doc: 'DOC'):
        super().__init__(doc=doc)