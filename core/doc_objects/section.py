from core.doc_objects.base import BaseContainElement, BaseMurkupElement
from typing import List
from core.doc_objects.base import BaseAttributeElement
from core.doc_objects.paragraph import SI_Paragraph

# class SI_pPr(BaseContainElement):
#     def __init__(self,
#                  children: List[BaseMurkupElement] = None,
#                  attrs: List[BaseAttributeElement] = None):
#         super().__init__("w:pPr", attrs, children)
#

class SI_SectPr(BaseContainElement):
    """
    Display <Section> without any
    wrapping at the object level
    """
    # todo Заполнить подходящими значениями Атрибуты и тэги
    # xpath = "./w:body/w:p/w:pPr/w:sectPr | ./w:body/w:sectPr"

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:SectPr", attrs, children)

