from ctypes.wintypes import tagMSG
from typing import List
from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.doc_objects.document import SI_Body
from docx.parts.document import DocumentPart
from core.oxml_magic.parser import to_si_element
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from docx.oxml import CT_Document


class Body(BaseContainerDocx):

    def __init__(self,
                 linked_objects: List[BaseDocx] = None):
        super().__init__(
            linked_objects=linked_objects
        )


class Document(BaseContainerDocx):
    def __init__(self,
                 document_elem: "CT_Document",
                 document_part: DocumentPart):
        super().__init__()
        self._part = document_part
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
