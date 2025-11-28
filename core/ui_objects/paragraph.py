from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx, BaseNonContainerDocx
from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.run import SI_Run
from core.doc_objects.text import SI_Text

class Paragraph(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None, text: str = ''):
        super().__init__(
            si_element=SI_Paragraph(),
            linked_objects=linked_objects
        )
        self.add(Run(linked_objects=[Text(text)]))

class Run(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=SI_Run(),
            linked_objects=linked_objects
        )

class Text(BaseNonContainerDocx):
    def __init__(self, text: str= ''):
        super().__init__(
            si_element=SI_Text(text=text)
        )