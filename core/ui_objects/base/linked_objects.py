from collections import UserList


class LinkedObjects(UserList):
    def __init__(self, linked_parent, initlist=None):
        self.linked_parent = linked_parent
        super().__init__(initlist)
        self.validate_access_children(initlist)

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
        elif isinstance(other, LinkedObjects):
            super().extend(other)

    def __setitem__(self, index: int, value):
        self.validate_access_child(value, index)
        super().__setitem__(index, value)

    def validate_access_child(self, item, position: int):
        allowed = (child["class"] for child in self.linked_parent.access_children)
        if not item or not allowed:
            return None
        if isinstance(item, tuple(allowed)):
            matching = [
                child
                for child in self.linked_parent.access_children
                if child["class"] is type(item)
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


class HiddenElements(LinkedObjects):
    """This class responsible for sequence of xml elements, which contains into parent element, but we should hide it.
    it's suitable when need to make sequence of linked objects is another then xml tree structure"""

    def __init__(self, linked_parent, initlist=None):
        super().__init__(linked_parent, initlist)

    def validate_access_child(self, item, position: int):
        allowed = (
            child["class"] for child in self.linked_parent.access_hidden_children
        )
        if not item:
            return None
        if isinstance(item, tuple(allowed)):
            matching = [
                child
                for child in self.linked_parent.access_hidden_children
                if child["class"] is type(item)
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
