from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import LinkedObjects
from core.ui_objects.bookmarks import BookmarkEnd, BookmarkStart
from core.ui_objects.run import Run, RunProperty


class ParagraphProperty(BaseContainerTag):
    __slots__ = ()

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:pPr"

    @property
    def access_children(self):
        return [{"class": RunProperty}]


class Paragraph(BaseContainerTag):
    __slots__ = ()

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:p"

    @property
    def access_children(self):
        return [
            {"class": ParagraphProperty, "required_position": 0},
            {"class": Run},
            {"class": BookmarkEnd},
            {"class": BookmarkStart},
        ]

    def add_run(self, run: Run, index: int = -1):
        self.add(run, index)

    def add_text(self, text: str):
        self.add(Run().add_text(text))
