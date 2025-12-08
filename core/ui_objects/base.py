from collections import UserList
from typing import FrozenSet, Type
from abc import abstractmethod, ABC


class BaseDocx:

    __slots__: tuple = ()
    """
         Abstract base class for XML tag representation.
         All concrete tag classes must:
         1. Define __slots__ containing the tag's attributes
         2. Implement the 'tag' property returning the tag name
         3. Initialize all slot attributes in __init__
         The class automatically converts slot-based attributes
         into XML attribute dictionary with proper namespace prefixes.
     """

    @property
    @abstractmethod
    def tag(self):
        pass

    @property
    def attrs(self):
        slots = getattr(self, '__slots__', ())
        if not slots:
            raise AttributeError(
                f"Class {self.__class__.__name__} "
                f"must define non-empty __slots__"
            )
        return {
            f"w:{item.replace('_', '')}": getattr(self, item.replace("_", ""))
            for item in slots
        }


class LinkedObjects(UserList):
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })

    def __init__(self, initlist=None):
        super().__init__(initlist)

    def append(self, item):
        validate_access_children(item, self.ACCESS_CHILDREN)
        super().append(item)

    def insert(self, i, item):
        validate_access_children(item, self.ACCESS_CHILDREN)
        super().insert(i, item)

    def extend(self, other):
        if isinstance(other, list):
            validate_access_childrens(other, self.ACCESS_CHILDREN)
            super().extend(other)
        elif isinstance(other, LinkedObjects):
            super().extend(other)


def validate_access_children(item, access_children):
    if isinstance(item, BaseDocx) and isinstance(item, tuple(access_children)):
        return True
    raise TypeError(f"It is prohibited to add {str(item)} to"
                    f"linked objects.")


def validate_access_childrens(items, access_childrens):
    map(lambda item: validate_access_children(item, access_childrens), items)


class BaseContainerDocx(ABC, BaseDocx):
    _linked_objects: LinkedObjects = LinkedObjects()
    _linked_objects.ACCESS_CHILDREN = frozenset()
    __slots__: tuple = ()

    @property
    def linked_objects(self) -> LinkedObjects:
        return self._linked_objects

    def add(self, item: BaseDocx):
        self._linked_objects.append(item)


class BaseNonContainerDocx(ABC, BaseDocx):
    __slots__: tuple = ()
    pass
