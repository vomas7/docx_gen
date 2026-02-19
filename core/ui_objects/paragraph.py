from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Objects, Property
from core.ui_objects.bookmarks import BookmarkEnd, BookmarkStart
from core.ui_objects.run import Run, RunProperty


class ParagraphProperty(BaseContainerTag):
    __slots__ = ()

    def __init__(
        self, objects: Objects | list = None, property: Property | list = None
    ):
        super().__init__(objects=objects, property=property)

    @property
    def tag(self):
        return "w:pPr"

    @property
    def access_children(self):
        return [{"class": RunProperty}]

    @property
    def access_property(self) -> list[dict]:
        return list()


class Paragraph(BaseContainerTag):
    __slots__ = ()

    def __init__(
        self, objects: Objects | list = None, property: Property | list = None
    ):
        super().__init__(objects=objects, property=property)

    @property
    def tag(self):
        return "w:p"

    @property
    def access_children(self):
        return [
            {"class": Run},
            {"class": BookmarkEnd},
            {"class": BookmarkStart},
        ]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": ParagraphProperty, "required_position": 0}]

    def add_run(self, run: Run, index: int = -1):
        self.add(run, index)

    def add_text(self, text: str):
        r = Run()
        r.add_text(text)
        self.add(r)
