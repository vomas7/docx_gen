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


# def tag_factory(
#         class_name,
#         parent_cls,
#         **kwargs
# ) -> Type[BaseTagElement]:
#     """
#     Factory of attributes, returns a class with <tag_name> class name without prefix <w:>
#     :param class_name: class name
#     :param is_container: if is container True otherwise False
#     :param kwargs: defines attributes into class
#     """
#
#     class_attrs = {
#         '__name__': class_name,
#         '__qualname__': class_name,
#         '__module__': __name__,
#     }
#     class_attrs.update(kwargs)
#
#     if is_container:
#         def _init(self, attrs=None, children=None):
#             super(type(self), self)._init(attrs, children)
#
#     else:
#         def _init(self, attrs=None):
#             super(type(self), self)._init(attrs)
#
#     class_attrs['_init'] = _init
#
#     return type(class_name, (parent_cls,), class_attrs)


def attr_factory(attr_name,
                 simple_type,
                 parent_cls,
                 cls_name=None,
                 default=None):
    """
    Factory of attributes, returns a class with <attr_name> class name without prefix <w:>
    """

    class_name = cls_name or _name_autofill_by_tag(attr_name)

    # class AttributeClass(BaseAttributeElement):
    #     _default_value = default
    #     _simple_type = simple_type
    class_attrs = {"__name__": class_name,
                   "__module__": __name__, }

    def __init__(self,
                 value=default,
                 simple_type: (Type[BaseSimpleType] |
                               Type[BaseXmlEnum]) = simple_type
                 ):
        super(type(self), self).__init__(value=value,
                                         simple_type=simple_type,
                                         attr_name=attr_name
                                         )

    class_attrs['__init__'] = __init__
    return type(class_name, (parent_cls,), class_attrs)
