from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.section import SI_SectPr
from core.exceptions.elements import ContainerError
from core.utils.v_objects import MiddlewareArray


class Section(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=SI_SectPr(),
            linked_objects=linked_objects
        )

    def _to_SI_element(self):
        if self.parent is None:
            raise ContainerError(
                ("Element '%s' must be wrapped in a container element" % self)
            )
        seq_child = MiddlewareArray()
        for child in self.linked_objects:
            seq_child.append_or_extend(child._to_SI_element())
        seq_child.append(self._si_element)
        return seq_child
