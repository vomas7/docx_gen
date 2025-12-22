from core.ui_objects import BaseContainerTag, BaseContentTag, LinkedObjects, \
    Break, Text


from core.ui_objects.atrib.size import Height, Width
from core.ui_objects.atrib.margins import Left, Top, Right, Bottom, Space, LinePitch
from core.ui_objects.atrib.ref import Header, Footer, Gutter



class PageSize(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self, width: str = None, height: str = None):
        self.width = Width(width)
        self.height = Height(height)

    @property
    def width(self):
        return self._width.value

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height.value

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def tag(self):
        return "w:pgSz"


class PageMargin(BaseContentTag):
    __slots__ = ("_top", "_right", "_bottom", "_left", "_header", "_footer", "_gutter")

    def __init__(self, top: str = None, right: str = None, bottom: str = None, left: str = None, header: str = None, footer: str = None, gutter: str = None):
        self.top = Top(top)
        self.right = Right(right)
        self.bottom = Bottom(bottom)
        self.left = Left(left)
        self.header = Header(header)
        self.footer = Footer(footer)
        self.gutter = Gutter(gutter)

    # Top
    @property
    def top(self):
        return self._top.value

    @top.setter
    def top(self, value):
        self._top = value

    # Right
    @property
    def right(self):
        return self._right.value

    @right.setter
    def right(self, value):
        self._right = value

    # Bottom
    @property
    def bottom(self):
        return self._bottom.value

    @bottom.setter
    def bottom(self, value):
        self._bottom = value

    # Left
    @property
    def left(self):
        return self._left.value

    @left.setter
    def left(self, value):
        self._left = value

    # Header
    @property
    def header(self):
        return self._header.value

    @header.setter
    def header(self, value):
        self._header = value

    # Footer
    @property
    def footer(self):
        return self._footer.value

    @footer.setter
    def footer(self, value):
        self._footer = value

    # Gutter
    @property
    def gutter(self):
        return self._gutter.value

    @gutter.setter
    def gutter(self, value):
        self._gutter = value

    @property
    def tag(self):
        return "w:pgMar"


class Cols(BaseContentTag):
    __slots__ = ("_space",)

    def __init__(self, space: str = None):
        self.space = Space(space)

    @property
    def space(self):
        return self._space.value

    @space.setter
    def space(self, value):
        self._space = value

    @property
    def tag(self):
        return "w:cols"


class DocGrid(BaseContentTag):
    __slots__ = ("_line_pitch",)
    def __init__(self, line_pitch: str = None):
        self.line_pitch = LinePitch(line_pitch)

    @property
    def line_pitch(self):
        return self._line_pitch.value

    @line_pitch.setter
    def line_pitch(self, value):
        self._line_pitch = value

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
