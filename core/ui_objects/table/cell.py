from core.ui_objects import Objects
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Property
from core.ui_objects.paragraph import Paragraph


class TableCellWidth:
    pass


class TableCellProperty(BaseContainerTag):
    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)

    @property
    def tag(self) -> str:
        return "w:tcPr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": TableCellWidth}]

    @property
    def access_property(self) -> list[dict]:
        return []


class TableCell(BaseContainerTag):
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
        return [{"class": TableCellProperty, "required_position": 0}]
