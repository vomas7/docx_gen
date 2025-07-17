from typing import Union

from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Paragraph import DOCParagraph


class ParagraphWriter(BaseWriter):
    """Class provides methods for writing DOCParagraphs objects"""
    def add_paragraph(self,
                      paragraph: Union[DOCParagraph, str],
                      section_index: int = -1,
                      paragraph_index: int = -1):
        if isinstance(paragraph, str):
            paragraph = DOCParagraph(text=paragraph)
        self.doc.add_paragraph(text=paragraph.text)
        self.doc.doc_sections[section_index].insert_linked_objects(
            paragraph,
            paragraph_index
        )
