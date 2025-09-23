from docx.oxml import OxmlElement, CT_Body

from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Section import DOCSection
from copy import deepcopy

class SectionWriter(BaseWriter):
    """Class provides methods for writing DOCSection objects"""

    def add_section(self, section: DOCSection, index: int = -1):
        section_elem = self.doc.sections[index]._sectPr
        if isinstance(section_elem.getparent(), CT_Body):
            self.doc._element.body.add_p().set_sectPr(section._sectPr.clone())

        else:
            p_elem = OxmlElement('w:p')
            pPr_elem = OxmlElement('w:pPr')
            pPr_elem.append(section._sectPr)
            p_elem.append(pPr_elem)
            self.doc._element.body.insert(index, deepcopy(p_elem))
        self.doc.doc_sections.insert(index, section)

    def replace_section(self, section: DOCSection, index: int = -1):
        self.doc._element.body.replace(
            self.doc.sections[index]._sectPr,
            section._sectPr
        )
        self.doc.doc_sections.insert(index, section)
