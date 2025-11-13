from docx.oxml.xmlchemy import BaseOxmlElement

from core.doc_objects.base import BaseMurkupElement, BaseAttributeElement, BaseContainElement
from typing import List


class SI_Document():
    """
        Is responsible for generating all document
        more likely will retrieve element from document part from pydocx
    """


class SI_Body(BaseContainElement):
    """is the root of all elements and manipulates specifically logic"""

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:Body", attrs, children)
    #todo may be too like si document
    # consider that xml will be extracted from the template