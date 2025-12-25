from core.ui_objects import LinkedObjects, Text
from core.ui_objects.base.base_container_tag import BaseContainerTag
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
        return {RunProperty}


class Paragraph(BaseContainerTag):
    __slots__ = ()

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:p"

    @property
    def access_children(self):
        return {ParagraphProperty, Run, BookmarkEnd, BookmarkStart}

    def add_run(self, run: Run, index: int = -1):
        self.add(run, index)

    def add_text(self, text: str | Text):
        self.add(Run(linked_objects=[Text(text=text)]))
