from oxml.xmlchemy import BaseAttributeElement
from docx.oxml.simpletypes import ST_TwipsMeasure


class MetaAttributesElement(type):
    __required_bases = (BaseAttributeElement,)
    __required_attributes = ("default_value", "attr_name", "simple_type")

    def __new__(cls, name, bases, attr):
        _check_bases = all(b in bases for b in cls.__required_bases)
        _check_attr = all(a in attr for a in cls.__required_attributes)
        if not _check_bases:
            raise TypeError(
                f"Class must be a subclass of {cls.__required_bases}"
            )
        if not _check_attr:
            raise TypeError(
                f"Class must contain a required attributes "
                f"{cls.__required_attributes}"
            )

        def initialize(obj, *args, **kwargs):
            _attr_name = kwargs.get("attr_name", None) or attr["attr_name"]
            _value = kwargs.get("value", None) or attr["default_value"]
            _simple_type = (kwargs.get("simple_type", None) or
                            attr["simple_type"])
            super(obj.__class__, obj).__init__(value=_value,
                                               simple_type=_simple_type,
                                               attr_name=_attr_name)

        attr["__init__"] = initialize
        return super().__new__(cls, name, bases, attr)


class Right(BaseAttributeElement, metaclass=MetaAttributesElement):
    default_value = None
    attr_name = "w:right"  # todo заменить строки на енумы
    simple_type = ST_TwipsMeasure

# class Left(BaseAttributeElement):
#     attr_name = "w:left"
#     value = None
#
#     def __init__(self, attr_name, value):
#         super().__init__(attr_name, value, ST_TwipsMeasure)
