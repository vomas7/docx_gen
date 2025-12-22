from core.ui_objects import BaseContainerTag, BaseContentTag, LinkedObjects, \
    Break, Text


from core.ui_objects.atrib.size import Height, Width
from core.ui_objects.atrib.margins import Left, Top, Right, Bottom, Space, LinePitch
from core.ui_objects.atrib.ref import Header, Footer, Gutter



class PageSize(BaseContentTag):
    __slots__ = ("width", "height")

    def __init__(self, width: str, height: str):
        self.width = Width(width)
        self.height = Height(height)

    @property
    def tag(self):
        return "w:pgSz"


class PageMargin(BaseContentTag):
    __slots__ = ("top", "right", "bottom", "left", "header", "footer", "gutter")

    def __init__(self, top: str, right: str, bottom: str, left: str, header: str, footer: str, gutter: str):
        self.top = Top(top)
        self.right = Right(right)
        self.bottom = Bottom(bottom)
        self.left = Left(left)
        self.header = Header(header)
        self.footer = Footer(footer)
        self.gutter = Gutter(gutter)

    @property
    def tag(self):
        return "w:pgMar"


class Cols(BaseContentTag):
    __slots__ = ("space",)

    def __init__(self, space: str):
        self.space = Space(space)

    @property
    def tag(self):
        return "w:cols"


class DocGrid(BaseContentTag):
    __slots__ = ("line_pitch",)
    def __init__(self, line_pitch: str):
        self.line_pitch = LinePitch(line_pitch)


    @property
    def tag(self):
        return "w:docGrid"


class Section(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:sectPr"

    @property
    def access_children(self):
        return {PageSize, PageMargin, Cols, DocGrid}
