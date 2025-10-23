from typing import List, Any, Callable, Set


class ValidatedArray(list):
    __err_msg = "Элемент(ы) '%s' не прошл(и) валидацию" # todo использовать класс ошибок

    def __init__(self,
                 iterable: List[Any] = None,
                 validators: Set[Callable[[Any], bool]] = None):
        """
            Class with a validatable feature. Takes list of any elements,
            otherwise create empty list.
            Args:
                iterable: Initial array data
                validators: list of validator functions,
                            returns True if the element is valid
        """
        if validators:
            self._validator = lambda x: all(func(x) for func in validators)
        else:
            self._validator = self._default_validator

        if iterable:
            invalid_items = [item for item in iterable if not self._validator(item)]
            if invalid_items:
                raise ValueError(self.__err_msg % invalid_items)
        super().__init__(iterable or [])

    def _default_validator(self, item: Any) -> bool:
        """Default validator - allows all elements"""
        return True

    def set_validator(self, validator: Callable[[Any], bool]) -> None:
        """Install a custom validator"""
        self._validator = validator

    def validate(self, item: Any) -> bool:
        """Check if an element can be added"""

        return self._validator(item)

    def append(self, item: Any) -> None:
        """Add an element with validation"""
        if not self.validate(item):
            raise ValueError(self.__err_msg % item)
        super().append(item)

    def extend(self, iterable: List[Any]) -> None:
        """Add multiple elements with validation"""
        invalid_items = [item for item in iterable if not self.validate(item)]
        if invalid_items:
            raise ValueError(self.__err_msg % invalid_items)
        super().extend(iterable)

    def insert(self, index: int, item: Any) -> None:
        """Insert element with validation"""
        if not self.validate(item):
            raise ValueError(self.__err_msg % item)
        super().insert(index, item)

    def __setitem__(self, index: int, item: Any) -> None:
        """Set element by index with validation"""
        if not self.validate(item):
            raise ValueError(self.__err_msg % item)
        super().__setitem__(index, item)

    def __iadd__(self, other):
        if isinstance(other, list):
            self.extend(other)
        else:
            self.append(other)
        return self

    def __repr__(self) -> str:
        return f"ValidatedList({super().__repr__()})"
