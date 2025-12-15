import copy

from abc import abstractmethod

from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import LinkedObjects


class BaseContainerTag(BaseTag):
    __slots__ = ("_linked_objects",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        self.linked_objects = linked_objects

    @property
    @abstractmethod
    def tag(self) -> str:
        """Must be implemented in child"""
        pass

    @property
    @abstractmethod
    def access_children(self) -> set[BaseTag]:
        """Must assign children class that can be in linked_objects"""
        pass

    @property
    def linked_objects(self) -> LinkedObjects:
        return copy.deepcopy(self._linked_objects)

    @linked_objects.setter
    def linked_objects(self, new: LinkedObjects):
        if new is None:
            self._linked_objects = LinkedObjects(self, [])
        elif isinstance(new, LinkedObjects):
            new.linked_parent = self
            self._linked_objects = new
        elif isinstance(new, list):
            self._linked_objects = LinkedObjects(self, new)
        else:
            raise TypeError(f"{new} has not BaseTag objects")

    def add(self, item: BaseTag):
        self._linked_objects.append(item)
