from core.ui_objects import Objects
from core.ui_objects.table.validator import validate_word_table_columns
from core.ui_objects.base.base_attribute import TwipsAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Property
from core.utils.metrics import Twips


class W(TwipsAttribute):
    def __init__(self, w: Twips):
        super().__init__("w:w", value=w)


class TableGrid(BaseContainerTag):
    def __init__(
        self,
        columns_count: int,
        block_width: int,
        objects: Objects | list = None,
        property: Property | list = None,
    ):
        super().__init__(objects=objects, property=property)
        validate_word_table_columns(columns_count)
        self.column_count = columns_count
        self._block_width = block_width
        self._create_columns()

    @property
    def tag(self) -> str:
        return "w:tblGrid"

    @property
    def access_children(self) -> list[dict]:
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": GridColumn}]

    def _create_columns(self):
        print(1, self._block_width)
        print(2, self.column_count)
        one_column_width = self._block_width // self.column_count
        print(3, one_column_width)
        print(4, Twips(one_column_width))
        for _ in range(self.column_count):
            self.property.append(GridColumn(Twips(one_column_width)))


class GridColumn(BaseContentTag):
    """Column tag <w:gridCol> assignment"""

    __slots__ = ("_w",)

    def __init__(self, width: Twips):
        self.w = width

    @property
    def tag(self) -> str:
        return "w:gridCol"

    @property
    def w(self) -> int:
        return self._w.value

    @w.setter
    def w(self, new: Twips):
        self._w = W(new)
