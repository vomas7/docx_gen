from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.exceptions.elements import ContainerError
from core.utils.v_objects import MiddlewareArray
from docx.oxml import OxmlElement

class Section(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=OxmlElement("w:SectPr"),
            linked_objects=linked_objects
        )
        # todo it may be necessary to add a switch

    def _to_SI_element(self, si_element):
        if self.parent is None:
            raise ContainerError(
                ("Element '%s' must be wrapped in a container element" % self)
            )
        seq_child = MiddlewareArray()
        for child in self.linked_objects:
            seq_child.append_or_extend(child.to_SI_element())
        seq_child.append(si_element)  # todo make it optional
        return seq_child
