from typing import Union

from core.writers.BaseWriter import BaseWriter
from core.doc_objects.Paragraph import DOCParagraph


class ParagraphWriter(BaseWriter):
    """Class provides easily access to write objects to Document"""

    def add_paragraph(
            self,
            elem: DOCParagraph | str,
            p_index: int | None,
            s_index: int = -1
    ):
        elem = DOCParagraph(elem) if isinstance(elem, str) else elem
        section = self.doc.body.linked_objects[s_index]
        section.insert_linked_object(elem, p_index)

