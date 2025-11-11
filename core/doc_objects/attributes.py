from core.doc_objects.base import BaseAttributeElement
from docx.oxml.simpletypes import ST_TwipsMeasure
from typing import Type
from docx.enum.base import BaseXmlEnum
from docx.oxml.simpletypes import BaseSimpleType


def attr_factory(attr_name,
                 simple_type=ST_TwipsMeasure,
                 default=None):
    """
    Factory of attributes, returns a class with <attr_name> class name without prefix <w:>
    """
    class_name = attr_name.replace('w:', '').title()

    class AttributeClass(BaseAttributeElement):
        _default_value = default
        _simple_type = simple_type

        def __init__(self,
                     value=_default_value,
                     simple_type: Type[BaseSimpleType] | Type[
                         BaseXmlEnum] = _simple_type
                     ):
            super().__init__(
                value=value,
                simple_type=simple_type,
                attr_name=attr_name
            )

    AttributeClass.__name__ = class_name
    AttributeClass.__qualname__ = class_name
    return AttributeClass


Right = attr_factory(
    "w:right",
    simple_type=ST_TwipsMeasure,
    default=None
)
Left = attr_factory(default=100000, attr_name="w:left")
Top = attr_factory(default=500, attr_name="w:top")
Bottom = attr_factory(default=500, attr_name="w:bottom")
