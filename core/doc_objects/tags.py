from core.doc_objects.paragraph import SI_Paragraph

from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseMurkupElement
)
from core.utils.serializers import serialize_ns_to_obj
from typing import Sequence, FrozenSet, Type

# todo придумать как автоматически генерировать обязательные атрибуты (скорее всего просто добавить сторонний метод для middleware списка)


_namespace = globals()


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

    attrs_mapping = {
        "ACCESS_ATTRIBUTES": kwargs.get("ACCESS_ATTRIBUTES", []),
        "ACCESS_CHILDREN": kwargs.get("ACCESS_CHILDREN", []),
        "REQUIRED_CHILDREN": kwargs.get("REQUIRED_CHILDREN", []),
        "REQUIRED_ATTRIBUTES": kwargs.get("REQUIRED_ATTRIBUTES", []),
    }

    for key, seq in attrs_mapping.items():
        if seq:
            class_attrs[key] = serialize_related_obj(seq)

    if is_container:
        def __init__(self, attrs=None, children=None):
            super(type(self), self).__init__(tag_name, attrs, children)

    else:
        def __init__(self, attrs=None):
            super(type(self), self).__init__(tag_name, attrs)

    class_attrs['__init__'] = __init__

    TagClass = type(_class_name, (_ParentCls,), class_attrs)

    return TagClass


pgMarg = tag_factory(
    'w:pgMarg',
    is_container=True,
    ACCESS_ATTRIBUTES=["SI_Paragraph"],
)
