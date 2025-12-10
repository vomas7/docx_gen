from collections import UserList


class LinkedObjects(UserList):

    def __init__(self, linked_parent, initlist=None):
        super().__init__(initlist)
        self.linked_parent = linked_parent
        self.validate_access_children(initlist)

    def append(self, item):
        self.validate_access_child(item)
        super().append(item)

    def insert(self, i, item):
        self.validate_access_child(item)
        super().insert(i, item)

    def extend(self, other):
        if isinstance(other, list):
            self.validate_access_children(other)
            super().extend(other)
        elif isinstance(other, LinkedObjects):
            super().extend(other)

    def __setitem__(self, key, value):
        self.validate_access_child(value)
        super().__setitem__(key, value)

    def validate_access_child(self, item):
        from core.ui_objects.base.BaseContainerTag import BaseContainerTag
        allowed = self.linked_parent.allowed_children
        if not item or not allowed:
            return
        if (isinstance(item, BaseContainerTag)
                and isinstance(item, tuple(allowed))):
            return True
        raise TypeError(
            f"It is prohibited to add {item.__class__.__name__} to "
            f"linked_objects of {self.linked_parent.__class__.__name__}"
        )

    def validate_access_children(self, items):
        if items:
            map(lambda item: self.validate_access_child(item), items)
