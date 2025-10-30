from abc import ABC, abstractmethod

from core.exceptions.validation import ValidationError
from core.validators.v_objects import ValidatedArray
from core.validators.xml_components import validate_access_elem

from typing import List
from typing import cast
from typing import Type, Any, FrozenSet

from docx.enum.base import BaseXmlEnum
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.oxml.simpletypes import BaseSimpleType
from docx.oxml.ns import qn
from docx.oxml import OxmlElement


class BaseAttributeElement:
    def __init__(self,
                 attr_name: str = None,
                 value: Any = None,
                 simple_type: Type[BaseSimpleType] | Type[BaseXmlEnum] = None):
        self.attr_name = attr_name
        self._value_attr = value
        self.simple_type = simple_type

    @property
    def _clark_name(self) -> str:
        if ":" in self.attr_name:
            return qn(self.attr_name)
        return self.attr_name

    def get_oxml_value(self) -> str:
        """Возвращает значение для OXML с учетом типа"""
        _u_types = (BaseSimpleType | BaseXmlEnum)
        if self.simple_type and issubclass(self.simple_type, _u_types):
            return self.simple_type.to_xml(self._value_attr)
        return str(self._value_attr)

    @property
    def value_attr(self):
        return self._value_attr

    @value_attr.setter
    def value_attr(self, val):
        self.simple_type.validate(val)
        self._value_attr = val


class BaseMurkupElement(ABC):
    """Базовый класс для всех элементов разметки"""
    # by default there are no restrictions
    ACCESS_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset({
        BaseAttributeElement
    })
    REQUIRED_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset()

    def __init__(self,
                 tag: str,
                 attrs: List[BaseAttributeElement] = None):
        self.tag = tag
        self.validators = {
            validate_access_elem, }  # todo мб вынести в атрибут класса
        self.attrs = ValidatedArray(
            attrs,
            validators=self.validators,
            access_val=self.ACCESS_ATTRIBUTES,
            required_values=self.REQUIRED_ATTRIBUTES
        )

    def _assignment_attr(self, obj: BaseOxmlElement) -> Any:
        """Назначает атрибут OxmlElement"""
        for attr in self.attrs:
            oxml_val = attr.get_oxml_value()
            if oxml_val is None:
                raise AttributeError(f"Attribute {self.tag} has no value")
            obj.set(attr._clark_name, oxml_val)

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
    # by default there are no restrictions
    ACCESS_CHILDREN: FrozenSet[Type[BaseMurkupElement]] = frozenset({
        BaseMurkupElement
    })
    REQUIRED_CHILDREN: FrozenSet[Type[BaseMurkupElement]] = frozenset()

    def __init__(self,
                 tag: str,
                 attrs: List[BaseAttributeElement] = None,
                 children: List[BaseMurkupElement] = None):
        super().__init__(tag, attrs)
        self.validators = {validate_access_elem, }
        self.children = ValidatedArray(
            children,
            validators=self.validators,
            access_val=self.ACCESS_CHILDREN,
            required_values=self.REQUIRED_CHILDREN
        )

    def _to_oxml_element(self) -> BaseOxmlElement:
        """Трансформирует объект в OxmlElement рекурсивно с потомками"""

        oxml = cast(BaseOxmlElement, OxmlElement(self.tag))
        self._assignment_attr(oxml)

        for child in self.children:
            oxml.append(child._to_oxml_element())
        return oxml


class BaseNonContainElement(BaseMurkupElement):
    def __init__(self,
                 tag: str,
                 attrs: List[BaseAttributeElement]):
        super().__init__(tag, attrs)

    def _to_oxml_element(self) -> BaseOxmlElement:
        """Трансформирует объект в OxmlElement"""
        oxml = cast(BaseOxmlElement, OxmlElement(self.tag))
        self._assignment_attr(oxml)
        return oxml
