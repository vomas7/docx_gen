from typing import List, Any, Callable, Set
from core.exceptions.validation import (
    ValidationError,
    ValidationRequireError,
    ValidationAccessError
)


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
        if iterable:
            invalid_items = all(
                [item for item in iterable if not self._validator(item)])
            print(invalid_items)
            if invalid_items:
                raise ValidationAccessError(invalid_elem=invalid_items)

        super().__init__(iterable or [])

        self._check_required_values()

    def _default_validator(self, item: Any) -> bool:
        """Валидатор по умолчанию - разрешает все элементы"""
        return True

    def _check_required_values(self) -> None:
        """Проверяет наличие всех обязательных значений"""
        if self._required_values:
            missing = self._required_values - set(
                (type(item) for item in self))
            if missing:
                raise ValidationRequireError(
                    invalid_elem=self,
                    missing=missing
                )

    def validate(self, item: Any) -> bool:
        """Проверяет, может ли элемент быть добавлен"""
        return self._validator(item)

    def append(self, item: Any) -> None:
        """Добавляет элемент с валидацией"""
        if not self.validate(item):
            raise ValidationAccessError(invalid_elem=item)
        super().append(item)

    def extend(self, iterable: List[Any]) -> None:
        """Добавляет несколько элементов с валидацией"""
        invalid_items = [item for item in iterable if not self.validate(item)]
        if invalid_items:
            raise ValidationAccessError(invalid_elem=invalid_items)
        super().extend(iterable)

    def insert(self, index: int, item: Any) -> None:
        """Вставляет элемент с валидацией"""
        if not self.validate(item):
            raise ValidationAccessError(invalid_elem=item)
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
            raise ValidationAccessError(invalid_elem=item)

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
