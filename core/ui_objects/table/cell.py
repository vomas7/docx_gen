from core.ui_objects import Objects
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import Property
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.table.table_property_attributes import (
    CellType,
    CellWidthAttribute,
    CellTypeSpec,
)
from core.utils.metrics import Twips


class CellWidth(BaseContentTag):
    __slots__ = ("_w", "_type")

    def __init__(self, w: Twips | None = None, type: CellTypeSpec | None = None):
        self.width = CellWidthAttribute(w)
        self.type = CellType(type if type else "dxa")

    @property
    def tag(self) -> str:
        return "w:tcW"

    @property
    def type(self) -> str:
        return self._type.value

    @type.setter
    def type(self, new_type: CellTypeSpec):
        if not new_type:
            self._type = CellType(CellType.Options.dxa)
        elif isinstance(new_type, str | CellType.Options):
            self._type = CellType(new_type)
        elif isinstance(new_type, CellType):
            self._type = new_type
        else:
            raise TypeError(f"Wrong type for w:type! {type(new_type)}")

    @property
    def width(self):
        return self._w.value

    @width.setter
    def width(self, new_width: CellWidthAttribute):
        if isinstance(new_width, CellWidthAttribute):
            self._w = new_width
        else:
            raise TypeError(f"width must be in Twips not {type(new_width)}!")


class CellProperty(BaseContainerTag):
    __slots__ = ("_width",)

    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
        width: CellWidth | Twips = None,
    ):
        super().__init__(objects=objects, property=property)
        self.width = width

    @property
    def tag(self) -> str:
        return "w:tcPr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": CellWidth}]

    @property
    def access_property(self) -> list[dict]:
        return []

    @property
    def width(self) -> int:
        return self._width.width

    @width.setter
    def width(self, value: Twips | CellWidth):
        if isinstance(value, Twips):
            self._width = CellWidth(w=value)
        elif isinstance(value, CellWidth):
            self._width = value
        elif value is None:
            self._width = CellWidth(w=Twips(2000))
        else:
            raise TypeError(f"Width value must be CellWidth or Twips not {type(value)}")
        self.add(self._width)


class Cell(BaseContainerTag):
    __slots__ = ("_width",)

    def __init__(
        self,
        width: Twips = None,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)
        self.width = width

    @property
    def tag(self) -> str:
        return "w:tc"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": Paragraph}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": CellProperty, "required_position": 0}]

    @property
    def width(self) -> int:
        return self._get_property_attr(CellProperty, "width")

    @width.setter
    @BaseContainerTag.autoclean
    def width(self, value: Twips):
        self._set_property_attr(CellProperty, "width", value)
