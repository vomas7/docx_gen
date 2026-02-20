import copy
from abc import abstractmethod
from typing import overload
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

    # OBJECTS METHODS
    def add(self, item: BaseTag, index=-1):
        if index < 0:
            self.objects.append(item)
        else:
            self.objects.insert(index, item)

    def remove(self, item: BaseTag):
        self.objects.remove(item)

    def clear(self):
        self.objects.clear()

    def pop(self, index: int = -1):
        return self.objects.pop(index)

    def find(self, item: type[BaseTag]) -> list:
        return [obj for obj in self.objects if isinstance(obj, item)]

    def remove_children(self, child_class: type[BaseTag]):
        children = self.find(child_class)
        for child in children:
            self.remove(child)

    # PROPERTY METHODS
    @overload
    def get_property(self, name: str) -> None | BaseTag: ...

    @overload
    def get_property(self, cls: type[BaseTag]) -> None | BaseTag: ...

    def get_property(self, search) -> None | BaseTag:
        if isinstance(search, str):
            print(self.property)
            if search not in self.allowed_property_names:
                return None
            for prop in self.property:
                search_name = prop.__class__.__name__
                if search == search_name:
                    return prop
        elif isinstance(search, type):
            if search not in self.allowed_property_classes:
                return None
            for prop in self.property:
                if isinstance(prop, search):
                    return prop
        return None

    def assign_property(self, property: BaseTag):
        position = self._get_property_required_position(property.__class__)
        self.property[position] = property

    def _get_property_required_position(self, property: type[BaseTag]) -> int:
        return self._get_property_config(property).get("required_position")

    def _get_property_config(self, property: type[BaseTag]):
        try:
            return list(
                filter(lambda x: self.is_prop_class(x, property), self.access_property)
            )[0]
        except IndexError as index_error:
            raise AttributeError(
                f"The class of the object: {property} "
                f"being modified must be in "
                f"access_property: {self.allowed_property_names}"
            ) from index_error

    @staticmethod
    def is_prop_class(item: dict, property_cls: type[BaseTag]) -> bool:
        return item.get("class") is property_cls

    @property
    def allowed_property_names(self):
        return [i.get("class").__name__ for i in self.access_property]

    @property
    def allowed_property_classes(self):
        return [i.get("class") for i in self.access_property]

    def _get_property_attr(self, prop: type[BaseTag] | str, attr_name: str):
        prop = self.get_property(prop)
        return prop.get_attribute(attr_name) if prop else None

    def _set_property_attr(self, prop: type[BaseTag], attr_name: str, value):
        property_object = self.get_property(prop)
        if not property_object:
            index = self._get_property_required_position(prop)
            property_object = prop()
            self.property.insert(index, property_object)
        setattr(property_object, attr_name, value)

    def _has_active_property(self) -> bool:
        """Check if any property has active attributes"""
        if not self.property:
            return False
        for prop in self.property:
            slots = getattr(prop, "__slots__", ())
            for slot in slots:
                value = getattr(prop, slot, None)
                if value is not None and value is not False:
                    return True
        return False

    def _cleanup_inactive_property(self):
        if self.property and not self._has_active_property():
            self.property.clear()

    @classmethod
    def autoclean(cls, func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            self._cleanup_inactive_property()
            return result

        return wrapper

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
