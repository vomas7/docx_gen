from core.doc_objects.base import BaseAttributeElement
from docx.oxml.simpletypes import ST_TwipsMeasure
from core.utils.annotaions import annotation_catcher


class MetaAttributesElement(type):
    """
        Initializes __init__ for each Attribute class.
        Restricts  | __required_attributes | attributes for class
        and parent | __required_bases |
    """

    __required_bases = (BaseAttributeElement,)
    __required_attributes = ("default_value", "attr_name", "simple_type")

    def __init__(cls, cls_name, bases, namespace):
        super().__init__(cls_name, bases, namespace)

        _check_bases = all(issubclass(cls, b) for b in cls.__required_bases)
        _check_attr = all(a in namespace for a in cls.__required_attributes)
        if not _check_bases:
            raise TypeError(
                f"Class must be a subclass of {cls.__required_bases}"
            )
        if not _check_attr:
            raise TypeError(
                f"Class must contain a required attributes "
                f"{cls.__required_attributes}"
            )

        @annotation_catcher(
            'self',
            attr_name=namespace["attr_name"],
            value=namespace["default_value"],
            simple_type=namespace["simple_type"]
        )
        def initialize(arg):
            super(arg.self.__class__, arg.self).__init__(
                value=arg.value,
                simple_type=arg.simple_type,
                attr_name=arg.attr_name
            )

        cls.__init__ = initialize


class Right(BaseAttributeElement, metaclass=MetaAttributesElement):
    default_value = None
    attr_name = "w:right"  # todo заменить строки на енумы
    simple_type = ST_TwipsMeasure


class Left(BaseAttributeElement, metaclass=MetaAttributesElement):
    default_value = 100000
    attr_name = "w:left"  # todo заменить строки на енумы
    simple_type = ST_TwipsMeasure
