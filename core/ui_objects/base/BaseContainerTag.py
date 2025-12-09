from abc import ABC
from core.ui_objects.base.BaseTag import BaseTag
from core.ui_objects.base.LinkedObjects import LinkedObjects


class BaseContainerTag(ABC, BaseTag):

    __slots__: tuple = ('_linked_objects', )
    _linked_objects: LinkedObjects

    def __init__(self, linked_objects: LinkedObjects = None):
        self._linked_objects = LinkedObjects(linked_objects)
        self._linked_objects.object = self
        self._linked_objects.validate_access_children(linked_objects)

    @property
    def linked_objects(self) -> LinkedObjects:
        return self._linked_objects

    def add(self, item: BaseTag):
        self._linked_objects.append(item)
