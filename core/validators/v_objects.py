from typing import List, Any, Callable, Set, FrozenSet
from core.exceptions.validation import ValidationError


class ValidatedArray(list):
    def __init__(self,
                 iterable: List[Any] = None,
                 validators: Set[Callable[..., bool]] = None,
                 required_values: FrozenSet[Any] = None,
                 **kwargs):
        """
        Class with a validatable feature and required values check.

        Args:
            iterable: Initial array data
            validators: Set of validator functions
            required_values: Set of values that must be present in the array
            **kwargs: Additional arguments for each validator

        """
        # todo можно добавить ограничение по типам

        self._validators = validators or set()
        self._required_values = (frozenset(required_values) if
                                 required_values else frozenset())

        if self._validators:
            self._validator = lambda x: all(
                func(x, **kwargs) for func in self._validators
            )
        else:
            self._validator = self._default_validator

        all(self._validator(item) for item in iterable)

        super().__init__(iterable or [])

        self._check_required_values()

    def _default_validator(self, item: Any):
        """Default validator - allows all elements"""

    def _check_required_values(self, func_name=None) -> None:
        """Checks for all required values"""
        if self._required_values:
            miss = self._required_values - frozenset(
                type(item) for item in self
            )
            if miss:
                _base = f"Elements '{self._required_values}' is required"
                _base += (f"! Operation '{func_name}' not allowed"
                          if func_name else "")
                raise ValidationError(_base)

    def validate(self, item: Any):
        """Checks whether the item can be added"""
        self._validator(item)

    def append(self, item: Any) -> None:
        """Adds an element with validation"""
        self.validate(item)
        super().append(item)

    def extend(self, iterable: List[Any]) -> None:
        """Adds multiple elements with validation"""
        all(self._validator(item) for item in iterable)
        super().extend(iterable)

    def insert(self, index: int, item: Any) -> None:
        """Inserts an element with validation"""
        self.validate(item)
        super().insert(index, item)

    def remove(self, item: Any) -> None:
        """Deletes an element with the required values checked"""
        super().remove(item)
        self._check_required_values(func_name=self.remove.__name__)

    def pop(self, index: int = -1) -> Any:
        """Deletes and returns an element with the required values checked"""
        item = super().pop(index)
        self._check_required_values(func_name=self.pop.__name__)
        return item

    def clear(self) -> None:
        """Clears the list with the required values checked"""
        super().clear()
        self._check_required_values(func_name=self.clear().__name__)

    def __setitem__(self, index: int, item: Any) -> None:
        """Sets the element by index with validation"""
        self.validate(item)
        super().__setitem__(index, item)
        self._check_required_values(func_name=self.__setitem__.__name__)

    def __delitem__(self, index: int) -> None:
        """Deletes an element by index with mandatory values checked"""
        super().__delitem__(index)
        self._check_required_values(func_name=self.__delitem__.__name__)

    def __repr__(self) -> str:
        validators_info = f", validators={len(self._validators)}" if self._validators else ""
        required_info = f", required={self._required_values}" if self._required_values else ""
        return f"ValidatedArray({super().__repr__()}{validators_info}{required_info})"

    @property
    def required_values(self) -> FrozenSet[Any]:
        """Returns a set of required values"""
        return self._required_values.copy()

    @property
    def validators(self) -> Set[Callable[..., bool]]:
        """Returns a set of validators"""
        return self._validators.copy()
