from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Section import DOCSection


class SectionWriter(BaseWriter):
    """Class provides easily access to write objects to Document"""

    def add_section(self, elem: DOCSection, index: int | None = None):
        self.doc.body.insert_linked_object(elem, index)

