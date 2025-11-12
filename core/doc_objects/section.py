from core.doc_objects.base import BaseContainElement, BaseMurkupElement
from typing import List
from core.doc_objects.base import BaseAttributeElement


class SI_Section(BaseContainElement):
    """
    Display <Section> without any
    wrapping at the object level
    """
    # todo Заполнить подходящими значениями Атрибуты и тэги


    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:SectPr", attrs, children)
