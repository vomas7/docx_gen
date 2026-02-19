from collections import UserList


class LinkedList(UserList):
    def __init__(self, linked_parent, access_list: list, initlist=None):
        self.linked_parent = linked_parent
        self.access_list = access_list
        self.validate_access_children(initlist)
        super().__init__(initlist)

    def append(self, item):
        self.validate_access_child(item, self.__len__())
        super().append(item)

    def insert(self, index: int, item):
        self.validate_access_child(item, index)
        super().insert(index, item)

    def extend(self, other):
        if isinstance(other, list):
            self.validate_access_children(other)
            super().extend(other)
        elif isinstance(other, Objects):
            super().extend(other)

    def __setitem__(self, index: int, value):
        self.validate_access_child(value, index)
        super().__setitem__(index, value)

    def validate_access_child(self, item, position: int):
        allowed_classes = tuple(child["class"] for child in self.access_list)
        if not item:
            raise TypeError(
                "item is None"
            )
        if not allowed_classes:
            raise TypeError(
                "allowed_classes is None"
            )


        if isinstance(item, allowed_classes):
            matching = [
                child for child in self.access_list if child["class"] is type(item)
            ]
            access = matching[0] if matching else None
            if access and "required_position" in access:
                required_position = access.get("required_position")
                if required_position != position:
                    raise IndexError(
                        f"Object {item} must be on position {required_position} "
                        f"not {position}"
                    )
            return True
        raise TypeError(
            f"It is prohibited to add {item.__class__.__name__} to "
            f"linked_objects of {self.linked_parent.__class__.__name__}"
        )

    def validate_access_children(self, items):
        if items:
            for index, item in enumerate(items):
                self.validate_access_child(item, index)


class Objects(LinkedList):
    """A list of objects that can be inside this tag and their sequence in the docx"""

    def __init__(self, linked_parent, initlist=None):
        super().__init__(linked_parent, linked_parent.access_children, initlist)


class Property(LinkedList):
    """List of object properties (These are usually additional or technical tags)"""

    def __init__(self, linked_parent, initlist=None):
        super().__init__(linked_parent, linked_parent.access_property, initlist)
