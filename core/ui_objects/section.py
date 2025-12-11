from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.exceptions.elements import ContainerError
from core.utils.v_objects import MiddlewareArray
from core.oxml_magic.parser import OxmlElement

class Section(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            linked_objects=linked_objects
        )
        # todo it may be necessary to add a switch

    @property
    def tag(self):
        return "w:p"
