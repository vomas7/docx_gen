from typing import List, Any, Callable, Set

from typing import List, Any, Callable, Set, Optional, Union
from functools import wraps



class ValidationError(ValueError):
    """Кастомная ошибка для валидации"""
    pass


class ValidatedArray(list):
    def __init__(self,
                 iterable: List[Any] = None,
                 validators: Set[Callable[..., bool]] = None,
                 required_values: Set[Any] = None,
                 **kwargs):
        """
        Class with a validatable feature and required values check.

        Args:
            iterable: Initial array data
            validators: Set of validator functions
            required_values: Set of values that must be present in the array
            **kwargs: Additional arguments for each validator

        """
        self._validators = validators or set()
        self._required_values = set(
            required_values) if required_values else set()

        if self._validators:
            self._validator = lambda x: all(
                func(x, **kwargs) for func in self._validators
            )
        else:
            self._validator = self._default_validator
        #todo убрать хпрдкод ошибок
        #todo настроить для required elem
        if iterable:
            invalid_items = not all([self._validator(item) for item in iterable])
            if invalid_items:
                raise ValidationError(
                    f"Элемент(ы) {invalid_items} не прошл(и) валидацию")

        super().__init__(iterable or [])

        self._check_required_values()

    def _default_validator(self, item: Any) -> bool:
        """Валидатор по умолчанию - разрешает все элементы"""
        return True

    def _check_required_values(self) -> None:
        """Проверяет наличие всех обязательных значений"""
        if self._required_values:
            missing = self._required_values - set((type(item) for item in self))
            if missing:
                raise ValidationError(
                    f"Обязательные элементы отсутствуют: {missing}"
                )

    def validate(self, item: Any) -> bool:
        """Проверяет, может ли элемент быть добавлен"""
        return self._validator(item)

    def append(self, item: Any) -> None:
        """Добавляет элемент с валидацией"""
        if not self.validate(item):
            raise ValidationError(f"Элемент '{item}' не прошел валидацию")
        super().append(item)

    def extend(self, iterable: List[Any]) -> None:
        """Добавляет несколько элементов с валидацией"""
        invalid_items = [item for item in iterable if not self.validate(item)]
        if invalid_items:
            raise ValidationError(
                f"Элемент(ы) {invalid_items} не прошл(и) валидацию")
        super().extend(iterable)

    def insert(self, index: int, item: Any) -> None:
        """Вставляет элемент с валидацией"""
        if not self.validate(item):
            raise ValidationError(f"Элемент '{item}' не прошел валидацию")
        super().insert(index, item)

    def remove(self, item: Any) -> None:
        """Удаляет элемент с проверкой обязательных значений"""
        super().remove(item)
        self._check_required_values()

    def pop(self, index: int = -1) -> Any:
        """Удаляет и возвращает элемент с проверкой обязательных значений"""
        item = super().pop(index)
        self._check_required_values()
        return item

    def clear(self) -> None:
        """Очищает список с проверкой обязательных значений"""
        super().clear()
        self._check_required_values()

    def __setitem__(self, index: int, item: Any) -> None:
        """Устанавливает элемент по индексу с валидацией"""

        if not self.validate(item):
            raise ValidationError(f"Элемент '{item}' не прошел валидацию")

        super().__setitem__(index, item)
        self._check_required_values()


    def __delitem__(self, index: int) -> None:
        """Удаляет элемент по индексу с проверкой обязательных значений"""
        super().__delitem__(index)
        self._check_required_values()


    def __repr__(self) -> str:
        validators_info = f", validators={len(self._validators)}" if self._validators else ""
        required_info = f", required={self._required_values}" if self._required_values else ""
        return f"ValidatedArray({super().__repr__()}{validators_info}{required_info})"

    @property
    def required_values(self) -> Set[Any]:
        """Возвращает множество обязательных значений"""
        return self._required_values.copy()

    @property
    def validators(self) -> Set[Callable[..., bool]]:
        """Возвращает множество валидаторов"""
        return self._validators.copy()

# class ValidatedArray(list):
#     __err_msg = "Элемент(ы) '%s' не прошл(и) валидацию" # todo использовать класс ошибок
#
#     def __init__(self,
#                  iterable: List[Any] = None,
#                  validators: Set[Callable[..., bool]] = None,
#                  **kwargs):
#         """
#             Class with a validatable feature. Takes list of any elements,
#             otherwise create empty list.
#             Args:
#                 iterable: Initial array data
#                 validators: list of validator functions,
#                             returns True if the element is valid
#
#
#
#
#         """
#         if validators:
#             self._validator = lambda x: (
#                 all(func(x, **kwargs) for func in validators)
#             )
#         else:
#             self._validator = self._default_validator
#
#         if iterable:
#             invalid_items = [item for item in iterable if not self._validator(item)]
#             if invalid_items:
#                 raise ValueError(self.__err_msg % invalid_items)
#         super().__init__(iterable or [])
#
#     def _default_validator(self, item: Any, **kwargs) -> bool:
#         """Default validator - allows all elements"""
#         return True
#
#     def set_validator(self, validator: Callable[[Any], bool]) -> None:
#         """Install a custom validator"""
#         self._validator = validator
#
#     def validate(self, item: Any) -> bool:
#         """Check if an element can be added"""
#
#         return self._validator(item)
#
#     def append(self, item: Any) -> None:
#         """Add an element with validation"""
#         if not self.validate(item):
#             raise ValueError(self.__err_msg % item)
#         super().append(item)
#
#     def extend(self, iterable: List[Any]) -> None:
#         """Add multiple elements with validation"""
#         invalid_items = [item for item in iterable if not self.validate(item)]
#         if invalid_items:
#             raise ValueError(self.__err_msg % invalid_items)
#         super().extend(iterable)
#
#     def insert(self, index: int, item: Any) -> None:
#         """Insert element with validation"""
#         if not self.validate(item):
#             raise ValueError(self.__err_msg % item)
#         super().insert(index, item)
#
#     def __setitem__(self, index: int, item: Any) -> None:
#         """Set element by index with validation"""
#         if not self.validate(item):
#             raise ValueError(self.__err_msg % item)
#         super().__setitem__(index, item)
#
#     def __iadd__(self, other):
#         if isinstance(other, list):
#             self.extend(other)
#         else:
#             self.append(other)
#         return self
#
#     def __repr__(self) -> str:
#         return f"ValidatedList({super().__repr__()})"
#
#
#
#
#
