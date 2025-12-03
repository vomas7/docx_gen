from typing import List

from core.ui_objects.base import (
    BaseContainerDocx,
    BaseDocx,
    BaseNonContainerDocx
)
from core.oxml_magic.parser import OxmlElement


class Paragraph(BaseContainerDocx):

    #todo нет проверки на отсутсвие текста, поэтому может создать ненужные ran и text
    def __init__(self, linked_objects: List[BaseDocx] = None, text: str = ''):
        super().__init__(
            si_element=OxmlElement("w:p"),
            linked_objects=linked_objects
        )
        self.add(Run(linked_objects=[Text(text)]))


class Run(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=OxmlElement("w:r"),
            linked_objects=linked_objects
        )


class Text(BaseNonContainerDocx):
    def __init__(self, text: str = ''):
        _si_text = OxmlElement("w:t")
        _si_text.text = text
        super().__init__(si_element=_si_text)
