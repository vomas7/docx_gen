from oxml.xmlchemy import BaseContainElement, BaseMurkupElement
from typing import Dict, List


class Run(BaseContainElement):
    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 **attr: Dict[str, str]):
        super().__init__("w:r", attr, children)
