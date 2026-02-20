from core.ui_objects.paragraph import Paragraph
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Property, Objects
from core.ui_objects.table.cell import Cell
from core.utils.metrics import Twips


class TableRowProperty(BaseContainerTag):
    pass


class TableRow(BaseContainerTag):
    def __init__(
        self,
        columns_count: int,
        block_width: int,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)
        self.columns_count = columns_count
        self.block_width = block_width
        self.default_cell_width = self.block_width // self.columns_count
        self._create_default_cells()

    @property
    def tag(self):
        return "w:tr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": Cell}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableRowProperty, "required_position": 0}]

    def _create_default_cells(self):
        for _ in range(self.columns_count):
            self.objects.append(
                Cell(width=Twips(self.default_cell_width), objects=[Paragraph()])
            )
