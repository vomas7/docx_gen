from core.doc_objects.paragraph import SI_Paragraph
from abc import ABCMeta
from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseMurkupElement
)
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

#todo придумать как завести и адаптировать для атрибутов бляяяяяяяяяяяяяяяяяя
#todo не забыть про базовую иницилизацию
#todo как вариант сделать ещё один метакласс, котторый занимается отслеживанием элементов. тогда скорее всего понвдобится самый высокий базовый элемент.
class BaseTagsMeta(ABCMeta):
    """Метакласс для регистрации элементов разметки и управления их отношениями."""

    _registry: ClassVar[Dict[str, Type['BaseMurkupElement']]] = {}
    _base_attrs: ClassVar[Set[str]] = {"ACCESS_ATTRIBUTES",
                                       "REQUIRED_ATTRIBUTES"}
    _container_attrs: ClassVar[Set[str]] = {"ACCESS_CHILDREN",
                                            "REQUIRED_CHILDREN"}

    # Имена базовых классов для избежания циклических импортов
    _base_class_names: ClassVar[Set[str]] = {
        'BaseMurkupElement',
        'BaseContainElement',
        'BaseNonContainElement'
    }

    def __init__(cls, name: str, bases: tuple, attrs: dict) -> None:
        super().__init__(name, bases, attrs)

        # Проверяем атрибуты только для конкретных элементов (не базовых классов)
        if BaseTagsMeta._is_concrete_element(name):
            cls._validate_attributes()
            BaseTagsMeta._registry[name] = cls

    @classmethod
    def _is_concrete_element(cls, class_name: str) -> bool:
        """Проверяет, является ли класс конкретным элементом (исключает базовые классы)."""
        return (class_name not in cls._base_class_names and
                not class_name.startswith('Base'))

    @classmethod
    def _is_container_element(cls, target_class: Type[T]) -> bool:
        """Проверяет, является ли класс контейнерным элементом по имени его базовых классов."""
        # Проверяем по именам базовых классов чтобы избежать циклических импортов
        base_names = {base.__name__ for base in target_class.__mro__}
        return 'BaseContainElement' in base_names

    def _validate_attributes(cls) -> None:
        """Проверка обязательных атрибутов класса."""
        if not obj_has_all_attrs(cls, BaseTagsMeta._base_attrs):
            raise AttributeError(
                f"Missing required base attributes in {cls.__name__}")

        if BaseTagsMeta._is_container_element(cls):
            if not obj_has_all_attrs(cls, BaseTagsMeta._container_attrs):
                raise AttributeError(
                    f"Missing container attributes in {cls.__name__}")

    @classmethod
    def initialize_relations(cls) -> None:
        """Инициализирует отношения между классами после регистрации всех элементов."""
        for class_name, class_obj in cls._registry.items():
            cls._resolve_class_references(class_obj)

    @classmethod
    def _resolve_class_references(cls, target_class: Type[T]) -> None:
        """Заменяет строковые ссылки на реальные классы в атрибутах."""
        attrs_to_resolve = cls._base_attrs.copy()

        if cls._is_container_element(target_class):
            attrs_to_resolve.update(cls._container_attrs)

        for attr_name in attrs_to_resolve:
            original_values = getattr(target_class, attr_name, set())
            resolved_classes = {
                cls._registry[ref] for ref in original_values
                if ref in cls._registry
            }
            # Сохраняем оригинальные значения для отладки
            unresolved_refs = original_values - set(cls._registry.keys())
            if unresolved_refs:
                raise NameError(
                    "Unresolved references in '%s'.'%s': '%s'" %
                    (target_class.__name__, attr_name, unresolved_refs)
                )

            setattr(target_class, attr_name, resolved_classes)

    @classmethod
    def get_registry(cls) -> Dict[str, Type['BaseMurkupElement']]:
        """Возвращает копию реестра зарегистрированных классов."""
        return cls._registry.copy()

    @classmethod
    def register_base_class(cls, class_name: str) -> None:
        """Добавляет имя класса в список базовых классов."""
        cls._base_class_names.add(class_name)


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
