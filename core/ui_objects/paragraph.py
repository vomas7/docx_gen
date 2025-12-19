from core.ui_objects import BaseContainerTag, LinkedObjects, Run, Text, BookmarkEnd, BookmarkStart

class ParagraphPr(BaseContainerTag):
    __slots__ = ("_bold",)
    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:pPr"

    @property
    def access_children(self):
        return {}



class Paragraph(BaseContainerTag):
    __slots__ = ("_bold",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:p"

    @property
    def access_children(self):
        return {ParagraphPr, Run, BookmarkEnd, BookmarkStart}

    def add_text(self, text: str | Text):
        self.add(Run(linked_objects=[Text(text=text)]))