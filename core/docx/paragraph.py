from typing import List

from core.docx.base import BaseContainerDocx, BaseDocx
from core.doc_objects.paragraph import SI_Paragraph


# todo не забыть про назначение parent

class Paragraph(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=SI_Paragraph(),
            linked_objects=linked_objects
        )
