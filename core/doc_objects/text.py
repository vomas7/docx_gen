from oxml.xmlchemy import BaseNonContainElement, BaseAttributeElement
from typing import Dict
from typing import Type


class Text(BaseNonContainElement):
    def __init__(self,
                 text: str = "",
                 attr: Type[BaseAttributeElement] = None):
        self.text = text
        super().__init__("w:t", attr)

    def _to_oxml_element(self):
        oxml = super()._to_oxml_element()
        oxml.text = self.text
        return oxml
