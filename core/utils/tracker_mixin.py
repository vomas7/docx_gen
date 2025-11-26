from typing import Set, Dict, Type, Any, ClassVar, TypeVar
from abc import ABCMeta


class RegisterMeta(type):
    _registry: Dict[str, Any] = {}

    def __new__(mcls, clsname, clsbases, namespace):
        cls = super().__new__(mcls, clsname, clsbases, namespace)
        mcls._registry[clsname] = cls
        setattr(cls, '_registry', cls._registry)
        return cls


T = TypeVar('T', bound='BaseMurkupElement')


class RelationDefMeta(ABCMeta, RegisterMeta):
    """Метакласс для регистрации элементов разметки и управления их отношениями."""

    _expected_attrs: ClassVar[Set[str]] = {"ACCESS_ATTRIBUTES",
                                           "REQUIRED_ATTRIBUTES",
                                           "ACCESS_CHILDREN",
                                           "REQUIRED_CHILDREN"}

    @classmethod
    def initialize_relations(cls) -> None:
        """Инициализирует отношения между классами после регистрации всех элементов."""
        for cls_name, class_obj in cls._registry.items():
            for r_attrs in cls._expected_attrs:
                if hasattr(class_obj, r_attrs):
                    seq_ref = getattr(class_obj, r_attrs)
                    cls_ref = cls._resolve_cls_ref(seq_ref, r_attrs, cls_name)
                    setattr(class_obj, r_attrs, cls_ref)

    @classmethod
    def _resolve_cls_ref(cls, seq_ref: Set, r_attr, cls_name) -> Set[Type[T]]:
        """Заменяет строковые ссылки на реальные классы в атрибутах."""
        resolved_ref = set()
        for ref in seq_ref:
            if isinstance(ref, str):
                obj = cls._registry.get(ref)

                if obj is None:
                    raise NameError(
                        "undefined references in "
                        "class: '%s'. attribute: '%s' reference: '%s'" %
                        (cls_name, r_attr, ref)
                    )
                ref = obj
            resolved_ref.add(ref)
        return resolved_ref
