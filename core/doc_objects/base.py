from abc import ABC, abstractmethod

from core.utils.v_objects import MiddlewareArray
from core.validators.xml_components import validate_access_elem

from typing import List
from typing import cast
from typing import Type, Any, FrozenSet

from docx.enum.base import BaseXmlEnum
from docx.oxml.simpletypes import BaseSimpleType
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.oxml.xmlchemy import serialize_for_reading
from lxml import etree


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
        """Returns a value for OXML given the type"""
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
    """Base class for all markup elements"""

    # by default there are no restrictions
    ACCESS_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset({
        BaseAttributeElement
    })
    REQUIRED_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset()

    def __init__(self,
                 tag: str,
                 attrs: List[BaseAttributeElement] = None):
        self._tag = tag
        _attribute_actions = {validate_access_elem, }

        self.attrs = MiddlewareArray(
            attrs,
            actions=_attribute_actions,
            required_values=self.REQUIRED_ATTRIBUTES,
            access_val=self.ACCESS_ATTRIBUTES
        )

    def _assignment_attr(self, obj: etree.ElementBase) -> Any:
        """Assigns an OxmlElement attribute"""
        for attr in self.attrs:
            oxml_val = attr.get_oxml_value()
            if oxml_val is None:
                raise AttributeError(f"Attribute {attr} has no value")
            obj.set(attr._clark_name, oxml_val)

    def to_oxml(self) -> etree.ElementBase:
        """Transforms an object into an etree.element"""
        _oxml = cast(etree.ElementBase, OxmlElement(self.tag))

        return self._to_oxml_element(_oxml)

    def to_xml_string(self) -> str:
        """Transforms an object into an XML string"""
        return serialize_for_reading(self.to_oxml())

    @abstractmethod
    def _to_oxml_element(
            self,
            oxml_elem: etree.ElementBase
    ) -> etree.ElementBase:
        pass

    @property
    def tag(self):
        return self._tag

    def __repr__(self):
        return f'<{type(self)} object at {hex(id(self))}>'

    def __str__(self):
        return f'{type(self)} object at {hex(id(self))}>'



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

        _tag_actions = {validate_access_elem, }
        self.children = MiddlewareArray(
            children,
            actions=_tag_actions,
            required_values=self.REQUIRED_CHILDREN,
            access_val=self.ACCESS_CHILDREN
        )

    def _to_oxml_element(self,
                         oxml_elem: etree.ElementBase) -> etree.ElementBase:
        """
            Transforms an object into an
            OxmlElement recursively with its descendants
        """

        self._assignment_attr(oxml_elem)

        for child in self.children:
            oxml_elem.append(child.to_oxml())
        return oxml_elem


class BaseNonContainElement(BaseMurkupElement):
    def __init__(self,
                 tag: str,
                 attrs: List[BaseAttributeElement]):
        super().__init__(tag, attrs)

    def _to_oxml_element(self, oxml_elem) -> etree.ElementBase:
        """Transforms an object into an OxmlElement"""

        self._assignment_attr(oxml_elem)
        return oxml_elem
