from abc import ABC, abstractmethod
from typing import Dict, List
from docx.oxml import OxmlElement
from docx.oxml.xmlchemy import BaseOxmlElement
from typing import cast

from core.validators.v_objects import ValidatedArray
from core.validators.xml_components import validate_access_elem
from typing import Set, Type


class BaseMurkupElement(ABC):
    """Базовый класс для всех элементов разметки"""

    ACCESSIBLE_ATTRIBUTES: Set[...] = set()  # todo добавить класс атрибутов
    REQUIRED_ATTRIBUTES: Set[...] = set()  # todo добавить класс атрибутов

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
    ACCESSIBLE_CHILDREN: Set[Type[BaseMurkupElement]] = set()
    REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = set()

    def __init__(self,
                 tag: str,
                 attr: Dict,
                 children: List[BaseMurkupElement] = None):
        super().__init__(tag, attr)
        self.children = ValidatedArray(
            children,
            validators={validate_access_elem, },
            access_val=self.ACCESSIBLE_CHILDREN,
            required_values=self.REQUIRED_CHILDREN
        )

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
