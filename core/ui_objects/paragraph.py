from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.doc_objects.paragraph import SI_Paragraph


class Paragraph(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=SI_Paragraph(),
            linked_objects=linked_objects
        )
