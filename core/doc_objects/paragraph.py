from __future__ import annotations
from core.doc_objects.base import BaseContainElement, BaseTagElement, \
    BaseAttributeElement
from typing import List


class SI_Paragraph(BaseContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги
    # todo сделать заполнение обязательных атрибутов и тегов атоматическим
    ACCESS_CHILDREN = {"SI_Run", "SI_Text", "SI_Paragraph"}
    def __init__(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:p", attrs, children)


class SI_pPr(BaseContainElement):
    def __init__(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:pPr", attrs, children)
