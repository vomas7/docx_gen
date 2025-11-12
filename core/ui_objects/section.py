from typing import List

from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.section import SI_SectPr
from core.exceptions.elements import ContainerError

class Section(BaseContainerDocx):
    def __init__(self, linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=SI_SectPr(),
            linked_objects=linked_objects
        )

    def _to_SI_element(self):
        for child in self.linked_objects:
            if self.parent is None:
                raise ContainerError(
                    ("Element '%s' must be wrapped in a container element"
                     % self)
                )
            self.parent._si_element.children.append(child.to_SI_element())
        return self._si_element