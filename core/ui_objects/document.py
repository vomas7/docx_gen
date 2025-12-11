from typing import List
from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.ui_objects.api import parse_document_part



class Body(BaseContainerDocx):

    def __init__(self,
                 linked_objects: List[BaseDocx] = None):
        super().__init__(
            linked_objects=linked_objects
        )

    @property
    def tag(self):
        return "w:body"


class Document(BaseContainerDocx):
    def __init__(self):
        super().__init__()
        self._part = parse_document_part
        self._body = None



    @property
    def tag(self):
        return "w:document"


    @property
    def body(self) -> Body:
        if self._body is None:
            self._body = Body(self._si_document.children[0])
        return self._body

    def save(self, path):
        self._part._element.clear()
        # todo подумать над автоматическом собрании элементов
        self._part._element.append(self.body.to_SI_element().to_oxml())

        self._part.save(path)
