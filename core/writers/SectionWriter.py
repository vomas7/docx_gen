import copy

from docx.oxml import OxmlElement

from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Section import DOCSection


class SectionWriter(BaseWriter):
    """Class provides methods for writing DOCSection objects"""

    def add_section(self, section: DOCSection, index: int = -1):
        # self.doc._element.body.replace(
        #     self.doc.sections[index]._sectPr,
        #     section._sectPr
        # )
        if index < 0:
            self.doc._element.body.add_section_break()
            self.doc._element.body.replace(
                self.doc.sections[index]._sectPr,
                section._sectPr
            )
        else:
            old_elem = self.doc.paragraphs[index]._element
            old_p = old_elem.getparent()
            new_p, new_pPr = OxmlElement('w:p'), OxmlElement('w:pPr')
            new_pPr.append(section._sectPr)
            new_p.append(new_pPr)
            old_p.insert(old_p.index(old_elem), new_p)
        self.doc.doc_sections.insert(index, section)

    def replace_section(self, section: DOCSection, index: int = -1):
        self.doc._element.body.replace(
            self.doc.sections[index]._sectPr,
            section._sectPr
        )
        self.doc.doc_sections.insert(index, section)
