import copy

from abc import abstractmethod

from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import Objects, Property


class BaseContainerTag(BaseTag):
    __slots__ = ("_objects", "_property")

    def __init__(
        self, objects: Objects | list = None, property: Property | list = None
    ):
        self.objects = objects
        self.property = property

    @property
    @abstractmethod
    def tag(self) -> str:
        """Must be implemented in child"""
        raise NotImplementedError

    @property
    @abstractmethod
    def access_children(self) -> list[dict]:
        raise NotImplementedError

    @property
    @abstractmethod
    def access_property(self) -> list[dict]:
        raise NotImplementedError

    @property
    def objects(self) -> Objects:
        return self._objects

    @property
    def property(self) -> Property:
        return self._property

    @property.setter
    def property(self, new: Property):
        if new is None:
            self._property = Property(self, initlist=[])
        elif isinstance(new, Property):
            new = copy.deepcopy(new)
            new.linked_parent = self
            self._property = new
        elif isinstance(new, list):
            self._property = Property(self, initlist=new)
        else:
            raise TypeError(f"{new} is not an instance of BaseTag")

    @objects.setter
    def objects(self, new: Objects):
        if new is None:
            self._objects = Objects(self, initlist=[])
        elif isinstance(new, Objects):
            new = copy.deepcopy(new)
            new.linked_parent = self
            self._objects = new
        elif isinstance(new, list):
            self._objects = Objects(self, initlist=new)
        else:
            raise TypeError(f"{new} is not an instance of BaseTag")

    def add(self, item: BaseTag, index=-1):
        if index < 0:
            self.objects.append(item)
        else:
            self.objects.insert(index, item)

    def remove(self, item: BaseTag):
        self.objects.remove(item)

    def pop(self, index: int = -1):
        return self.objects.pop(index)

    def find(self, item: type[BaseTag]) -> list:
        return [obj for obj in self.objects if isinstance(obj, item)]

    def remove_children(self, child_class: type[BaseTag]):
        children = self.find(child_class)
        for child in children:
            self.remove(child)

    def _change_property(self, property: BaseTag):
        position = self._get_property_position(property)
        self.property[position] = property

    def _get_property_position(self, property: BaseTag | type[BaseTag]) -> int:
        return self._get_property_class(property).get("required_position")

    def _get_property_class(self, property: BaseTag | type[BaseTag]):
        try:
            return list(
                filter(
                    lambda x: self._is_class_property(x, property), self.access_property
                )
            )[0]
        except IndexError as index_error:
            raise AttributeError(
                f"The class of the object: {property} "
                f"being modified must be in "
                f"access_property: {self._get_property_classes()}"
            ) from index_error

    @staticmethod
    def _is_class_property(item: dict, property: BaseTag | type[BaseTag]) -> bool:
        cls = item.get("class")
        return isinstance(property, cls) or issubclass(property, cls)

    def _get_property_classes(self):
        return [i.get("class").__name__ for i in self.access_property]

    def _get_property(self, prop: BaseTag | type[BaseTag]) -> BaseTag:
        return self.property[self._get_property_position(prop)]
