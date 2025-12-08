from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseTagElement
)
from docx.oxml.ns import nsmap
from core.doc_objects.base import BaseAttributeElement
from docx.oxml.simpletypes import BaseSimpleType
from docx.enum.base import BaseXmlEnum

from typing import Type


def _name_autofill_by_tag(tag_name: str) -> str:
    """Returns name like SI_<tag name> the name begins with a capital letter"""

    prefix, tagroot = tag_name.split(':')
    if prefix not in nsmap:
        raise AttributeError(f"Prefix '{prefix}' is not defined!")
    return 'SI_' + tag_name.replace(f'{prefix}:', '').title()


def attr_factory(attr_name,
                 simple_type,
                 parent_cls,
                 cls_name=None,
                 default=None):
    """
    Factory of attributes
        Parameters:
        param: attr_name is a markup attribute name
        param: simple_type is rule how to convert this attribute
        param: parent_cls is the parent class
        param: cls_name is the class name, if not provided, the auto-fill method will be used
        param: default: default value for markup attribute
    """

    class_name = cls_name or _name_autofill_by_tag(attr_name)

    class_attrs = {"__name__": class_name,
                   "__module__": __name__, }

    def __init__(self,
                 value=default,
                 simple_type: (Type[BaseSimpleType] |
                               Type[BaseXmlEnum]) = simple_type
                 ):
        super(type(self), self).__init__(value=value,
                                         simple_type=simple_type,
                                         attr_name=attr_name)

    class_attrs['__init__'] = __init__
    return type(class_name, (parent_cls,), class_attrs)
