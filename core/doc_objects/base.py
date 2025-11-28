from abc import ABC, abstractmethod

from core.utils.v_objects import MiddlewareArray
from core.validators.v_objects import validate_access_type

from typing import List
from typing import cast
from typing import Type, Any, FrozenSet

from docx.enum.base import BaseXmlEnum
from docx.oxml.simpletypes import BaseSimpleType
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.oxml.xmlchemy import serialize_for_reading
from lxml import etree
from core.utils.tracker_mixin import RelationDefMeta


class BaseMarkupElement(metaclass=RelationDefMeta):
    """Root element for word docx markup elements."""
    pass


class BaseAttributeElement(BaseMarkupElement):
    """Base class for attribute elements."""

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


class BaseTagElement(BaseMarkupElement, etree.ElementBase, ABC):
    """Base class for all markup elements"""

    # by default there are no restrictions
    ACCESS_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset({
        "BaseAttributeElement"
    })
    REQUIRED_ATTRIBUTES: FrozenSet[Type[BaseAttributeElement]] = frozenset()

    def _init(self, attrs: List[BaseAttributeElement] = None):
        _attribute_actions = {validate_access_type, }
        # Note: attributes should be added into array from existing elements in initializing
        self.attrs = MiddlewareArray(
            attrs,
            actions=_attribute_actions,
            required_types=self.REQUIRED_ATTRIBUTES,
            access_val=self.ACCESS_ATTRIBUTES
        )

    def _assignment_attr(self) -> Any:
        """Assigns an OxmlElement attribute"""
        for attr in self.attrs:
            oxml_val = attr.get_oxml_value()
            if oxml_val is None:
                raise AttributeError(f"Attribute {attr} has no value")
            self.set(attr._clark_name, oxml_val)

    # todo согласовать найминг, т.к self уже является объектом
    def to_oxml(self) -> etree.ElementBase:
        """Transforms a single objects into tree of markup elements."""
        # _oxml = cast(etree.ElementBase, OxmlElement(self.tag))
        self._assignment_attr()
        return self._fold_elements()

    def to_xml_string(self) -> str:
        """Transforms an object into an XML string"""

        return serialize_for_reading(self.to_oxml())

    @abstractmethod
    def _fold_elements(self) -> etree.ElementBase:
        pass

    def __repr__(self):
        return f'<{type(self)} object at {hex(id(self))}>'

    def __str__(self):
        return f'{type(self)} object at {hex(id(self))}>'


class BaseContainElement(BaseTagElement):
    """Base class for all contain-markup elements"""
    # todo .....

    # by default there are no restrictions
    ACCESS_CHILDREN: FrozenSet[Type[BaseTagElement]] = frozenset({
        "BaseMarkupElement"
    })
    REQUIRED_CHILDREN: FrozenSet[Type[BaseTagElement]] = frozenset()

    def _init(self,
              attrs: List[BaseAttributeElement] = None,
              children: List[BaseTagElement] = None):
        super()._init(attrs)

        _tag_actions = {validate_access_type, }
        # Note: children should be added into array from existing elements in initializing. Because letter this elements will be drawing!

        self.children = MiddlewareArray(
            children,
            actions=_tag_actions,
            required_types=self.REQUIRED_CHILDREN,
            access_val=self.ACCESS_CHILDREN
        )

    def _fold_elements(self) -> etree.ElementBase:
        """To collect all child elements into tree elements"""

        for child in self.children:
            self.append(child.to_oxml())
        return self


class BaseNonContainElement(BaseTagElement):
    """Base class for all non contain-markup elements"""

    def _init(self, attrs: List[BaseAttributeElement] = None):
        super()._init(attrs)

    def _fold_elements(self) -> etree.ElementBase:
        """To collect into tree of elements"""

        return self
