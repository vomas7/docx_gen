from types import NoneType

from core.ui_objects.section import Section
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.table.column import TableGrid
from core.ui_objects.table.row import TableRow
from core.ui_objects.table.table_property_attributes import Justification
from core.ui_objects.table.validator import validate_word_table_rows
from core.ui_objects.table.validator import validate_word_table_columns
from core.utils.metrics import Twips


class Table(BaseContainerTag):
    def __init__(self, rows: int = None, cols: int = None, section: Section = None):
        super().__init__()
        if isinstance(rows, NoneType) or isinstance(cols, NoneType):
            return
        if not section:
            section = Section()
        validate_word_table_rows(rows)
        validate_word_table_columns(cols)
        self.rows = rows
        self.columns = cols
        self.section = section
        self.block_width = self._calculate_block_width()
        self._create_table()

    @property
    def tag(self):
        return "w:tbl"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": TableGrid}, {"class": TableRow}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableProperty, "required_position": 0}]

    def _create_table(self):
        self._create_table_grid()
        self._create_rows()

    def _create_table_grid(self):
        self.objects.append(
            TableGrid(columns_count=self.columns, block_width=self.block_width)
        )

    def _create_rows(self):
        for _ in range(self.rows):
            self.objects.append(
                TableRow(block_width=self.block_width, columns_count=self.columns)
            )

    def _calculate_block_width(self) -> float | Twips:
        """Calculate page width without left and right margins"""
        page_width = self.section.page_width
        left = self.section.left_margin
        right = self.section.right_margin
        return page_width - left - right


class TableProperty(BaseContainerTag):
    @property
    def tag(self):
        return "w:tblPr"

    def access_children(self) -> list[dict]:
        return [
            {"class": Justification},
        ]

    def access_property(self) -> list[dict]:
        return list()
