# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import FrozenSet, Type, List

from abc import ABC
from core.utils.tracker_mixin import RegisterMeta

class BaseDocx(ABC):

    def __init__(self):
        self.parent = None

    _class_registry = {}



class BaseContainerDocx(BaseDocx):
    # all  <BaseDocx> elements are available by default
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })

    def __init__(self,
                 linked_objects: List[BaseDocx] = None):
        super().__init__()

        self.linked_objects = linked_objects or []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        if cls is not BaseContainerDocx and hasattr(cls, 'tag'):
            cls._class_registry[cls.__name__] = cls.tag


    def add(self, elem):
        self.linked_objects.append(elem)


class BaseNonContainerDocx(BaseDocx):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__()
        if cls is not BaseNonContainerDocx and hasattr(cls, 'tag'):
            cls._class_registry[cls.__name__] = cls.tag
