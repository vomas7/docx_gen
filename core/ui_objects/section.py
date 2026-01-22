from core.ui_objects import BaseTag
from core.ui_objects.atrib.margins import Bottom, Left, LinePitch, Right, Space, Top
from core.ui_objects.atrib.ref import Footer, Gutter, Header
from core.ui_objects.atrib.size import Height, Width
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import Objects, Property
from core.ui_objects.bookmarks import BookmarkEnd, BookmarkStart
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.run import Run


class PageSize(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self, width: int = 12240, height: int = 15840):
        self._width = Width(width)
        self._height = Height(height)

    @property
    def width(self):
        return self._width.value

    @width.setter
    def width(self, value):
        self._width.value = value

    @property
    def height(self):
        return self._height.value

    @height.setter
    def height(self, value):
        self._height.value = value

    @property
    def tag(self):
        return "w:pgSz"


class PageMargin(BaseContentTag):
    __slots__ = ("_top", "_right", "_bottom", "_left", "_header", "_footer", "_gutter")

    def __init__(
            self,
            top: int = 1440,
            right: int = 1800,
            bottom: int = 1440,
            left: int = 1800,
            header: int = 720,
            footer: int = 720,
            gutter: int = 0,
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

    def __init__(self, space: int = 720):
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

    def __init__(self, line_pitch: int = 360):
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
    def __init__(
            self,
            objects: Objects | list = None,
            property: Property | list = None
    ):
        if not property:
            property = [PageSize(), PageMargin(), Cols(), DocGrid()]
        super().__init__(objects, property)

    @property
    def tag(self):
        return "w:sectPr"

    @property
    def access_children(self):
        return [
            {"class": Paragraph},
            {"class": Run},
            {"class": BookmarkEnd},
            {"class": BookmarkStart},
        ]

    @property
    def access_property(self):
        return [
            {"class": PageSize, "required_position": 0},
            {"class": PageMargin, "required_position": 1},
            {"class": Cols, "required_position": 2},
            {"class": DocGrid, "required_position": 3},
        ]

    def change_page_size(self, width: int, height: int):
        self._change_property(PageSize(width=width, height=height))

    def change_page_margin(
            self,
            top: int,
            right: int,
            bottom: int,
            left: int,
            header: int,
            footer: int,
            gutter: int
    ):
        self._change_property(
            PageMargin(
                top=top,
                right=right,
                bottom=bottom,
                left=left,
                header=header,
                footer=footer,
                gutter=gutter)
        )

    def change_cols(self, space: int):
        self._change_property(Cols(space))

    def change_doc_grid(self, line_pitch: int):
        self._change_property(DocGrid(line_pitch))
