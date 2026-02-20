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
        self.type = CellType(type)

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
    def width(self, new_width: Twips):
        if isinstance(new_width, Twips):
            self._w = new_width
        raise TypeError(f"width must be in Twips not {type(new_width)}!")


class CellProperty(BaseContainerTag):
    def __init__(
        self,
        width: CellWidth = None,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)

    @property
    def tag(self) -> str:
        return "w:tcPr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": CellWidth}]

    @property
    def access_property(self) -> list[dict]:
        return []


class Cell(BaseContainerTag):
    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)

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
        return
