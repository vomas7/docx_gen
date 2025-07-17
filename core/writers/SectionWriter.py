from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Section import DOCSection


class SectionWriter(BaseWriter):
    """Class provides methods for writing DOCSection objects"""

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
