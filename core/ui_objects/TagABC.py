from abc import ABC, abstractmethod
from core.ui_objects.namespaces import NAMESPACES


class TagABC(ABC):
    """
        Abstract base class for XML tag representation.

        All concrete tag classes must:
        1. Define __slots__ containing the tag's attributes
        2. Implement the 'tag' property returning the tag name
        3. Initialize all slot attributes in __init__

        The class automatically converts slot-based attributes
        into XML attribute dictionary with proper namespace prefixes.
    """

    __slots__: tuple = ()
    NAMESPACES: dict = NAMESPACES

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
