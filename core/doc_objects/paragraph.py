from __future__ import annotations
from core.doc_objects.base import BaseContainElement, BaseMurkupElement, \
    BaseAttributeElement
from typing import List, Set, Type
from core.doc_objects.text import SI_Text
from core.doc_objects.run import SI_Run


class SI_Paragraph(BaseContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:p", attrs, children)
