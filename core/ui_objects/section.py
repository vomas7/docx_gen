from core.ui_objects import BaseContainerTag, BaseContentTag, LinkedObjects, \
    Break, Text


class PageSize(BaseContentTag):
    __slots__ = ("some",)

    @property
    def tag(self):
        return "w:pgSz"


class PageMargin(BaseContentTag):
    __slots__ = ("some",)

    @property
    def tag(self):
        return "w:pgMar"


class Cols(BaseContentTag):
    __slots__ = ("some",)

    @property
    def tag(self):
        return "w:cols"


class DocGrid(BaseContentTag):
    __slots__ = ("some",)

    @property
    def tag(self):
        return "w:docGrid"


class Section(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        linked_objects = linked_objects or LinkedObjects(linked_parent=self)
        # linked_objects += [PageMargin(), Cols(), DocGrid(), PageSize()]
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:sectPr"

    @property
    def access_children(self):
        return {PageSize, PageMargin, Cols, DocGrid}
