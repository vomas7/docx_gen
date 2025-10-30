from oxml.xmlchemy import BaseContainElement, BaseMurkupElement
from typing import List
from oxml.xmlchemy import BaseAttributeElement


class Run(BaseContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:r", attrs, children)
