from __future__ import annotations
from oxml.xmlchemy import BaseContainElement, BaseMurkupElement
from typing import Dict, List, Set, Type
from core.doc_objects.text import Text
from core.doc_objects.run import Run


class Paragraph(BaseContainElement):
    # todo Заполнить подходящими значениями
    ACCESSIBLE_CHILDREN: Set[Type[BaseMurkupElement]] = {Text, Run, }
    REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = {Run, }
    ACCESSIBLE_ATTRIBUTES: Set[...] = set()
    REQUIRED_ATTRIBUTES: Set[...] = set()

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 **attr: Dict[str, str]):
        super().__init__("w:p", attr, children)
