from abc import ABC, abstractmethod
from typing import Dict, List
from docx.oxml import OxmlElement
from docx.oxml.xmlchemy import BaseOxmlElement
from typing import cast

from core.validators.v_objects import ValidatedArray
from core.validators.xml_components import validate_access_elem


class BaseMurkupElement(ABC):
    """Базовый класс для всех элементов разметки"""

    def __init__(self, tag: str, attr: Dict):
        self.tag = tag
        self.attr = attr

    def to_oxml(self) -> BaseOxmlElement:
        """Трансформирует объект в OxmlElement"""

        return self._to_oxml_element()

    def to_xml_string(self) -> str:
        """Трансформирует объект в XML строку"""

        return self.to_oxml().xml

    @abstractmethod
    def _to_oxml_element(self) -> BaseOxmlElement:
        pass


class BaseContainElement(BaseMurkupElement):
    def __init__(self,
                 tag: str,
                 attr: Dict,
                 children: List[BaseMurkupElement] = None):
        from core.doc_objects.paragraph import Paragraph
        from core.doc_objects.text import Text
        from core.doc_objects.run import Run
        #todo наладить проблему с циклическими импортами
        #todo создать константу по типам и атрибутам
        #todo проверить возможности frozenset
        super().__init__(tag, attr)
        self.children = ValidatedArray(children,
                                       validators={validate_access_elem, },
                                       access_val={Text, Paragraph},
                                       required_values={Text})

    def _to_oxml_element(self) -> BaseOxmlElement:
        """Трансформирует объект в OxmlElement рекурсивно с потомками"""

        oxml = cast(BaseOxmlElement, OxmlElement(self.tag, attrs=self.attr))
        for child in self.children:
            oxml.append(child._to_oxml_element())
        return oxml


class BaseNonContainElement(BaseMurkupElement):
    def __init__(self,
                 tag: str,
                 attr: Dict):
        super().__init__(tag, attr)

    def _to_oxml_element(self) -> BaseOxmlElement:
        """Трансформирует объект в OxmlElement"""

        return cast(BaseOxmlElement, OxmlElement(self.tag, attrs=self.attr))
