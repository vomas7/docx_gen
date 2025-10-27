from oxml.xmlchemy import BaseContainElement, BaseMurkupElement
from typing import Dict, List


class Section(BaseContainElement):
    """
    Display <Section> without any
    wrapping at the object level
    """

    def __init__(self,
                 children: List[BaseMurkupElement] = None,
                 **attr: Dict[str, str]):
        super().__init__("w:SectPr", attr, children)
