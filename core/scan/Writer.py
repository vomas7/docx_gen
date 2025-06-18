from typing import TYPE_CHECKING

from core.doc_objects.Section import DOCSection

if TYPE_CHECKING:
    from core.doc import DOC

class BaseWriter:

    def __init__(self, doc: 'DOC'):
        self.doc = doc

class SectionWriter(BaseWriter):

    def add_section(self, section: DOCSection, index: int = -1):
        self.doc._element.body.add_section_break()
        self.doc._element.body.replace(
            self.doc.sections[index]._sectPr,
            section._sectPr
        )
        self.doc.elements.insert(index, section)

    def replace_section(self, section: DOCSection, index: int = -1):
        self.doc._element.body.replace(
            self.doc.sections[index]._sectPr,
            section._sectPr
        )
        self.doc.elements.insert(index, section)

class Writer(SectionWriter):

    def __init__(self, doc: 'DOC'):
        super().__init__(doc=doc)
