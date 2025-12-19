from core.ui_objects import LinkedObjects, BaseContainerTag


class Body(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:body"

    @property
    def access_children(self):
        return {}

    # def __str__(self):
    #     return str(hash(id(self)))

class Document(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:document"

    @property
    def access_children(self):
        return {Body}

