from core.ui_objects.atrib.margins import Bottom, Left, LinePitch, Right, Space, Top
from core.ui_objects.atrib.ref import Footer, Gutter, Header
from core.ui_objects.atrib.size import Height, Width
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import LinkedObjects


class PageSize(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self, width: str = None, height: str = None):
        self._width = Width(width)
        self._height = Height(height)

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

    def __init__(
        self,
        top: str = None,
        right: str = None,
        bottom: str = None,
        left: str = None,
        header: str = None,
        footer: str = None,
        gutter: str = None,
    ):
        self._top = Top(top)
        self._right = Right(right)
        self._bottom = Bottom(bottom)
        self._left = Left(left)
        self._header = Header(header)
        self._footer = Footer(footer)
        self._gutter = Gutter(gutter)

    # Top
    @property
    def top(self):
        return self._top.value

    @top.setter
    def top(self, value):
        self._top.value = value

    # Right
    @property
    def right(self):
        return self._right.value

    @right.setter
    def right(self, value):
        self._right.value = value

    # Bottom
    @property
    def bottom(self):
        return self._bottom.value

    @bottom.setter
    def bottom(self, value):
        self._bottom.value = value

    # Left
    @property
    def left(self):
        return self._left.value

    @left.setter
    def left(self, value):
        self._left.value = value

    # Header
    @property
    def header(self):
        return self._header.value

    @header.setter
    def header(self, value):
        self._header.value = value

    # Footer
    @property
    def footer(self):
        return self._footer.value

    @footer.setter
    def footer(self, value):
        self._footer.value = value

    # Gutter
    @property
    def gutter(self):
        return self._gutter.value

    @gutter.setter
    def gutter(self, value):
        self._gutter.value = value

    @property
    def tag(self):
        return "w:pgMar"


class Cols(BaseContentTag):
    __slots__ = ("_space",)

    def __init__(self, space: str = None):
        self._space = Space(space)

    @property
    def space(self):
        return self._space.value

    @space.setter
    def space(self, value):
        self._space.value = value

    @property
    def tag(self):
        return "w:cols"


class DocGrid(BaseContentTag):
    __slots__ = ("_line_pitch",)

    def __init__(self, line_pitch: str = None):
        self._line_pitch = LinePitch(line_pitch)

    @property
    def line_pitch(self):
        return self._line_pitch.value

    @line_pitch.setter
    def line_pitch(self, value):
        self._line_pitch.value = value

    @property
    def tag(self):
        return "w:docGrid"


class Section(BaseContainerTag):
    __slots__ = ("_pgSz",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)
        self._pgSz = PageSize()

    @property
    def tag(self):
        return "w:sectPr"

    @property
    def access_children(self):
        return {PageSize, PageMargin, Cols, DocGrid}
