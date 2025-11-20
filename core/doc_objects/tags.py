from core.doc_objects.paragraph import SI_Paragraph
from abc import ABCMeta
from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseMurkupElement
)
from core.utils.serializers import serialize_ns_to_obj
from typing import Sequence, FrozenSet, Type, Dict, Any

# todo придумать как автоматически генерировать обязательные атрибуты (скорее всего просто добавить сторонний метод для middleware списка)

#
# class TrackingMeta(type):
#     _registry = {}
#
#     def __new__(cls, name, bases, attrs):
#         # print(cls._registry)
#         return super().__new__(cls, name, bases, attrs)
#
#     def __init__(cls, name, bases, attrs):
#         super().__init__(name, bases, attrs)
#         TrackingMeta._registry[name] = cls
#
#     @classmethod
#     def get_registered_classes(cls):
#         return cls._registry
#
#     def _initialize_references(f):
#         pass
#
#
# class BaseMeta(TrackingMeta):
#     pass
#
#
# class X(metaclass=BaseMeta):
#     pass
#
#
# class Y(X):
#     pass
#
#
# class Z(metaclass=BaseMeta):
#     pass
#
#
# print("Registered classes:", TrackingMeta.get_registered_classes())

# {<class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>}


_namespace = globals()


class BaseTagsMeta(ABCMeta):
    def __new__(cls, clsname, bases, attrs):
        attrs_mapping = {
            "ACCESS_ATTRIBUTES": attrs.get("ACCESS_ATTRIBUTES", []),
            "ACCESS_CHILDREN": attrs.get("ACCESS_CHILDREN", []),
            "REQUIRED_CHILDREN": attrs.get("REQUIRED_CHILDREN", []),
            "REQUIRED_ATTRIBUTES": attrs.get("REQUIRED_ATTRIBUTES", []),
        }

        for key, seq in attrs_mapping.items():
            if seq:
                attrs[key] = serialize_related_obj(seq)

        return super().__new__(cls, clsname, bases, attrs)

    def __init__(cls, name, bases, attrs):
        super().__init__(name, bases, attrs)
        BaseTagsMeta._registry[name] = cls

    @classmethod
    def get_registered_classes(cls):
        return cls._registry


def serialize_related_obj(
        seq: Sequence[str]
) -> FrozenSet[Type[BaseMurkupElement]]:
    return frozenset(
        {serialize_ns_to_obj(ns=_namespace, attr=i) for i in seq}
    )


def tag_factory(
        tag_name,
        is_container,
        **kwargs
) -> Type[BaseMurkupElement]:
    """
    Factory of attributes, returns a class with <tag_name> class name without prefix <w:>
    """
    _class_name = tag_name.replace('w:', 'SI_')
    _ParentCls = BaseContainElement if is_container else BaseNonContainElement

    class_attrs = {
        '__name__': _class_name,
        '__qualname__': _class_name,
        '__module__': __name__,
    }
    class_attrs.update(kwargs)

    if is_container:
        def __init__(self, attrs=None, children=None):
            super(type(self), self).__init__(tag_name, attrs, children)

    else:
        def __init__(self, attrs=None):
            super(type(self), self).__init__(tag_name, attrs)

    class_attrs['__init__'] = __init__

    TagClass = BaseTagsMeta(_class_name, (_ParentCls,), class_attrs)

    return TagClass
