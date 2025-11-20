from typing import List, Any, Callable, Set, FrozenSet
from core.exceptions.validation import ValidationError
import collections.abc

class MiddlewareArray(list):
    def __init__(self,
                 iterable: List[Any] = None,
                 actions: Set[Callable[..., bool]] = None,
                 required_types: FrozenSet[Any] = None,
                 **kwargs):
        """
        Class with a validatable feature and required values check.

        Args:
            iterable: Initial array data
            actions: Set of action functions
            required_types: Set of values that must be present in the array
            **kwargs: Additional arguments for each action

        """
        self._actions = actions or set()
        self._required_types = (frozenset(required_types) if
                                 required_types else frozenset())
        _iterable = iterable or []
        if self._actions:
            self._action = lambda x: [
                func(x, **kwargs) for func in self._actions
            ]
        else:
            self._action = self._default_action


        [self._action(item) for item in _iterable]

        super().__init__(_iterable)

        self._check_required_types()

    def _default_action(self, item: Any):
        """Default action - allows all elements"""

    def _check_required_types(self, func_name=None) -> None:
        """Checks for all required values by type"""
        if self._required_types:
            miss = self._required_types - frozenset(
                type(item) for item in self
            )
            if miss:
                _base = f"Elements '{self._required_types}' is required"
                _base += (f"! Operation '{func_name}' not allowed"
                          if func_name else "")
                raise ValidationError(_base)

    def action(self, item: Any):
        """Checks whether the item can be added"""
        self._action(item)

    def append(self, item: Any) -> None:
        """Adds an element with validation"""
        self.action(item)
        super().append(item)

    def extend(self, iterable: List[Any]) -> None:
        """Adds multiple elements with validation"""
        [self._action(item) for item in iterable]
        super().extend(iterable)

    def append_or_extend(self, element: List[Any] | Any) -> None:
        """
        Adds both a single element and multiple elements with validation.
        peculiarities: considers that both string and bytes is sequence
        """
        if isinstance(element, collections.abc.Sequence):
            self.extend(element)
        else:
            self.append(element)


    def insert(self, index: int, item: Any) -> None:
        """Inserts an element with validation"""
        self.action(item)
        super().insert(index, item)

    def remove(self, item: Any) -> None:
        """Deletes an element with the required values checked"""
        super().remove(item)
        self._check_required_types(func_name=self.remove.__name__)

    def pop(self, index: int = -1) -> Any:
        """Deletes and returns an element with the required values checked"""
        item = super().pop(index)
        self._check_required_types(func_name=self.pop.__name__)
        return item

    def clear(self) -> None:
        """Clears the list with the required values checked"""
        super().clear()
        self._check_required_types(func_name=self.clear().__name__)

    def __setitem__(self, index: int, item: Any) -> None:
        """Sets the element by index with validation"""
        self.action(item)
        super().__setitem__(index, item)
        self._check_required_types(func_name=self.__setitem__.__name__)

    def __delitem__(self, index: int) -> None:
        """Deletes an element by index with mandatory values checked"""
        super().__delitem__(index)
        self._check_required_types(func_name=self.__delitem__.__name__)

    def __repr__(self) -> str:
        return f"MiddlewareArray({super().__repr__()})"

    @property
    def required_values(self) -> FrozenSet[Any]:
        """Returns a set of required values"""
        return self._required_types.copy()

    @property
    def actions(self) -> Set[Callable[..., bool]]:
        """Returns a set of actions"""
        return self._actions.copy()
