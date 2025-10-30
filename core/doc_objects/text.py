from core.doc_objects.base import BaseNonContainElement, BaseAttributeElement
from typing import List


class Text(BaseNonContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги

    def __init__(self,
                 text: str = "",
                 attrs: List[BaseAttributeElement] = None):
        self.text = text
        super().__init__("w:t", attrs)

    def _to_oxml_element(self):
        oxml = super()._to_oxml_element()
        oxml.text = self.text
        return oxml
