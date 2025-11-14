from typing import List
from core.ui_objects.base import BaseContainerDocx, BaseDocx
from core.doc_objects.document import SI_Body
from docx.parts.document import DocumentPart
from docx.oxml import CT_Document
from core.oxml_magic.ct_objects import convert_to_Si


class Body(BaseContainerDocx):

    def __init__(self,
                 si_element: SI_Body,
                 linked_objects: List[BaseDocx] = None):
        super().__init__(
            si_element=si_element,
            linked_objects=linked_objects
        )


class Document:
    def __init__(self,
                 document_elem: CT_Document,
                 document_part: DocumentPart):
        self._part = document_part
        self._si_document = convert_to_Si(document_elem)
        self._body = None

    @property
    def body(self):
        if self._body is None:
            self._body = Body(self._si_document.children[0])
        return self._body
