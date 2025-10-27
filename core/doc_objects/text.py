from oxml.xmlchemy import BaseNonContainElement
from typing import Dict


class Text(BaseNonContainElement):
    def __init__(self,
                 text: str = "",
                 **attr: Dict[str, str]):
        self.text = text
        super().__init__("w:t", attr)

    def _to_oxml_element(self):
        oxml = super()._to_oxml_element()
        oxml.text = self.text
        return oxml
