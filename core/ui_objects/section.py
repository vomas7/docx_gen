from core.ui_objects.atrib.margins import Bottom, Left, LinePitch, Right, Space, Top
from core.ui_objects.atrib.ref import Footer, Gutter, Header
from core.ui_objects.atrib.size import Height, Width
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import Objects, Property
from core.ui_objects.bookmarks import BookmarkEnd, BookmarkStart
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.run import Run
from core.utils.metrics import Length, Twips, Cm
from core.utils.constants import A4_MARGIN_GUTTER, A4_MARGIN_FOOTER, A4_MARGIN_HEADER
from core.utils.constants import A4_MARGIN_BOTTOM, A4_MARGIN_RIGHT
from core.utils.constants import A4_MARGIN_LEFT, A4_MARGIN_TOP
from core.utils.constants import A4_HEIGHT, A4_WIDTH
from core.utils.constants import COLUMN_GAP


class PageSize(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self, width: Twips = None, height: Twips = None):
        self._width = Width(width if width else A4_WIDTH)
        self._height = Height(height if height else A4_HEIGHT)

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
        top: Twips = None,
        right: Twips = None,
        bottom: Twips = None,
        left: Twips = None,
        header: Twips = None,
        footer: Twips = None,
        gutter: Twips = None,
    ):
        self._top = Top(top if top else A4_MARGIN_TOP)
        self._right = Right(right if right else A4_MARGIN_RIGHT)
        self._bottom = Bottom(bottom if bottom else A4_MARGIN_BOTTOM)
        self._left = Left(left if left else A4_MARGIN_LEFT)
        self._header = Header(header if header else A4_MARGIN_HEADER)
        self._footer = Footer(footer if footer else A4_MARGIN_FOOTER)
        self._gutter = Gutter(gutter if gutter else A4_MARGIN_GUTTER)

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

    def __init__(self, space: Twips = None):
        self._space = Space(space if space else COLUMN_GAP)

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

    def __init__(self, line_pitch: Twips = None):
        line_pitch = line_pitch if line_pitch else Twips(360)
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
        self, objects: Objects | list = None, property: Property | list = None
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

    def change_page_size(self, width: Length, height: Length):
        self._change_property(PageSize(width=width.twips, height=height.twips))

    def change_page_margin(
        self,
        top: Cm,
        right: Cm,
        bottom: Cm,
        left: Cm,
        header: Cm,
        footer: Cm,
        gutter: Cm,
    ):
        self._change_property(
            PageMargin(
                top=Twips(top.twips),
                right=Twips(right.twips),
                bottom=Twips(bottom.twips),
                left=Twips(left.twips),
                header=Twips(header.twips),
                footer=Twips(footer.twips),
                gutter=Twips(gutter.twips),
            )
        )

    def change_cols(self, space: Cm):
        self._change_property(Cols(Twips(space.twips)))

    def change_doc_grid(self, line_pitch: Cm):
        self._change_property(DocGrid(Twips(line_pitch.twips)))

    @property
    def page_width(self) -> int | Twips:
        return self._get_property(PageSize).width

    @property
    def page_width_cm(self) -> float | Cm:
        return Twips(self.page_width).cm

    @property
    def left_margin(self) -> int | Twips:
        return self._get_property(PageMargin).left

    @property
    def right_margin(self) -> int | Twips:
        return self._get_property(PageMargin).right
