from __future__ import annotations
from oxml.xmlchemy import BaseContainElement, BaseMurkupElement, \
    BaseAttributeElement
from typing import List, Set, Type
from core.doc_objects.text import Text
from core.doc_objects.run import Run


class Paragraph(BaseContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги
    ACCESS_CHILDREN: Set[Type[BaseMurkupElement]] = {Text, Run, }
    REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = {Run, }
    ACCESS_ATTRIBUTES: Set[...] = set()
    REQUIRED_ATTRIBUTES: Set[...] = set()

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:p", attrs, children)
