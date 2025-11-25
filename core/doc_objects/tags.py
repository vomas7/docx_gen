from core.doc_objects.paragraph import SI_Paragraph
from abc import ABCMeta
from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseMurkupElement
)
from core.utils.tracker_mixin import MetaRegister
from core.exceptions.validation import ValidationError
from core.utils.serializers import serialize_ns_to_obj
from typing import Sequence, FrozenSet, Type, Dict, Any
import warnings

# todo придумать как автоматически генерировать обязательные атрибуты (скорее всего просто добавить сторонний метод для middleware списка)

from abc import ABCMeta
from typing import Dict, Type, Set, TypeVar, ClassVar
from core.validators.objects import obj_has_all_attrs

from abc import ABCMeta
from typing import Dict, Type, Set, TypeVar, ClassVar

# Тип для элементов разметки
T = TypeVar('T', bound='BaseMurkupElement')


# todo придумать как завести и адаптировать для атрибутов бляяяяяяяяяяяяяяяяяя
# todo не забыть про базовую иницилизацию
# todo как вариант сделать ещё один метакласс, котторый занимается отслеживанием элементов. тогда скорее всего понвдобится самый высокий базовый элемент.
class BaseTagsMeta(ABCMeta, MetaRegister):
    """Метакласс для регистрации элементов разметки и управления их отношениями."""

    _expected_attrs: ClassVar[Set[str]] = {"ACCESS_ATTRIBUTES",
                                           "REQUIRED_ATTRIBUTES",
                                           "ACCESS_CHILDREN",
                                           "REQUIRED_CHILDREN"}

    @classmethod
    def initialize_relations(cls) -> None:
        """Инициализирует отношения между классами после регистрации всех элементов."""
        for class_name, class_obj in cls._registry.items():
            for r_attrs in cls._expected_attrs:
                if hasattr(class_obj, r_attrs):
                    seq_ref = getattr(class_obj, r_attrs)
                    resolved_ref = cls._resolve_class_references(seq_ref)
                    setattr(class_obj, r_attrs, resolved_ref)


    @classmethod
    def _resolve_class_references(cls, seq_ref: Set[Type[T]]) -> None:
        """Заменяет строковые ссылки на реальные классы в атрибутах."""

        # todo придумать решение
        # if seq_ref - set(cls._registry.keys()):
        #     raise NameError(
        #             "Unresolved references in '%s'.'%s': '%s'" %
        #             (clsname, , unresolved_refs)
        #         )
        resolved_ref = set()
        for ref in seq_ref:
            resolved_ref.add(cls._registry[ref])


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
