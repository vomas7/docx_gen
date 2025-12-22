import copy

from abc import abstractmethod

from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import LinkedObjects
from typing import Type


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
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: LinkedObjects):
        new = copy.deepcopy(new)
        if new is None:
            self._linked_objects = LinkedObjects(self, [])
        elif isinstance(new, LinkedObjects):
            new.linked_parent = self
            self._linked_objects = new
        elif isinstance(new, list):
            self._linked_objects = LinkedObjects(self, new)
        else:
            raise TypeError(f"{new} has not BaseTag objects")

    def add(self, item: BaseTag, index=-1):
        self._linked_objects.insert(index, item)

    def remove(self, item: BaseTag):
        self._linked_objects.remove(item)

    def pop(self, index: int = -1):
        return self._linked_objects.pop(index)

    def find(self, item: Type[BaseTag]) -> list:
        return [obj for obj in self.linked_objects if isinstance(obj, item)]

    def remove_child(self, child: BaseTag):
        children = self.find(type(child))
        for child in children:
            self.remove(child)
