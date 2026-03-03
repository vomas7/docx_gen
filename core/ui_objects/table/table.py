from core.ui_objects import Objects
from core.ui_objects.base.linked_objects import Property
from core.ui_objects.section import Section
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.table.column import TableGrid
from core.ui_objects.table.row import TableRow
from core.ui_objects.table.table_property_attributes import Justification
from core.ui_objects.table.table_property_attributes import TableStyle, StyleVal
from core.ui_objects.table.validator import validate_word_table_rows
from core.ui_objects.table.validator import validate_word_table_columns
from core.utils.constants import DEFAULT_TABLE_STYLE
from core.utils.metrics import Twips


class Table(BaseContainerTag):
    def __init__(
        self,
        rows: int = None,
        cols: int = None,
        section: Section = None,
        objects: Objects | list = None,
        property: Property | list = None,
        table_style: str | StyleVal = None,
    ):
        super().__init__(objects=objects, property=property)
        validate_word_table_rows(rows)
        validate_word_table_columns(cols)
        self.rows = rows
        self.columns = cols
        self.table_style = table_style
        if self.rows and self.columns:
            self.section = section if section else Section()
            self.block_width = self._calculate_block_width()
            self._create_table()
            self.style = table_style

    @property
    def tag(self):
        return "w:tbl"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": TableRow}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableProperty, "required_position": 0}, {"class": TableGrid}]

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

    @property
    def style(self):
        return self._get_property_attr(TableProperty, "style")

    @style.setter
    def style(self, table_style: str):
        self._set_property_attr(TableProperty, "style", table_style)


class TableProperty(BaseContainerTag):
    __slots__ = ("_style",)

    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
        style: str = None,
    ):
        super().__init__(objects=objects, property=property)
        self.style = style

    @property
    def tag(self):
        return "w:tblPr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": Justification}, {"class": TableStyle}]

    @property
    def access_property(self) -> list[dict]:
        return list()

    @property
    def style(self):
        return self._style

    @style.setter
    def style(self, style_id: str):
        style_id = style_id if style_id else DEFAULT_TABLE_STYLE
        new_style = TableStyle(style_id)
        self.change_siblings(new_style)
        self._style = style_id

    def _get_table_style_index(self) -> int | None:
        for index, obj in enumerate(self.objects):
            if isinstance(obj, TableStyle):
                return index
        return None
