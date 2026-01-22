from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.table.table_property_content_tags import Justification


class Table(BaseContainerTag):
    @property
    def tag(self):
        return "w:tbl"

    @property
    def access_children(self) -> list[dict]:
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableProperty, "required_position": 0}]


class TableProperty(BaseContainerTag):
    def tag(self):
        return "w:tblPr"

    def access_children(self) -> list[dict]:
        return [
            {"class": Justification},
        ]

    def access_property(self) -> list[dict]:
        return list()


class TableGrid(BaseContainerTag):
    pass
