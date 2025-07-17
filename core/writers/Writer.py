from core.doc import DOC
from core.writers.SectionWriter import SectionWriter
from core.writers.ParagraphWriter import ParagraphWriter


class Writer(SectionWriter, ParagraphWriter):
    """Class provides method to writing DOCObjects into document word"""
    def __init__(self, doc: DOC):
        super().__init__(doc=doc)
