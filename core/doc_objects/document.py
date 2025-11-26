from core.doc_objects.base import BaseTagElement, BaseAttributeElement, \
    BaseContainElement
from typing import List
from core.doc_objects.tags import tag_factory

# SI_Document = tag_factory("w:document", is_container=True)


# analog write :
class SI_Document(BaseContainElement):
    def __init__(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:document", attrs, children)


class SI_Body(BaseContainElement):

    def __init__(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:body", attrs, children)
    # todo may be too like si document
    # consider that xml will be extracted from the template

    # todo realize method for section logic
