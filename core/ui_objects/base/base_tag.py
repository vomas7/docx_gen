from abc import ABC, abstractmethod
from typing import Any

from core.oxml_magic.ns import qn
from core.ui_objects.base.base_attribute import BaseAttribute


class BaseTag(ABC):
    __slots__: tuple = ()
    """
         Abstract base class for XML tag representation.
         All concrete tag classes must:
         1. Define __slots__ containing the tag's attributes
         2. Implement the 'tag' property returning the tag name
         3. Initialize all slot attributes in __init__
         The class automatically converts slot-based attributes
         into XML attribute dictionary with proper namespace prefixes.
     """

    @property
    @abstractmethod
    def tag(self):
        """Must assign tag like return string for safety"""
        pass

    @property
    def attrs(self):
        """Complete dict with attributes for XML craft"""
        slots = getattr(self, "__slots__", ())
        attrs = {}
        for slot in slots:
            attribute = self.get_attribute(slot)
            if (
                attribute
                and isinstance(attribute, BaseAttribute)
                and attribute.value is not None
            ):
                _value = attribute.value
                value = _value if isinstance(_value, str) else str(_value)
                attrs[qn(attribute.xml_name)] = value
        return attrs

    def get_attribute(self, attribute: str) -> Any:
        return getattr(self, attribute) if hasattr(self, attribute) else None

    def __str__(self):
        attrs = self.attrs
        attrs_str = " ".join(f'{key}="{value}"' for key, value in attrs.items())
        return f"{self.__class__.__name__}: <{self.tag} {attrs_str}/>"
