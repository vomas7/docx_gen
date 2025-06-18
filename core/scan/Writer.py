from typing import TYPE_CHECKING, Union

from core.doc_objects.Paragraph import DOCParagraph
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
        self.doc.doc_sections.insert(index, section)

    def replace_section(self, section: DOCSection, index: int = -1):
        self.doc._element.body.replace(
            self.doc.sections[index]._sectPr,
            section._sectPr
        )
        self.doc.doc_sections.insert(index, section)


class ParagraphWriter(BaseWriter):

    def add_paragraph(self,
                      paragraph: Union[DOCParagraph, str],
                      section_index: int = -1,
                      paragraph_index: int = -1):
        if isinstance(paragraph, str):
            paragraph = DOCParagraph(text=paragraph)
        self.doc.add_paragraph(text=paragraph.text)
        self.doc.doc_sections[section_index].insert_linked_objects(paragraph,
                                                                   paragraph_index)

class Writer(SectionWriter, ParagraphWriter):

    def __init__(self, doc: 'DOC'):
        super().__init__(doc=doc)
