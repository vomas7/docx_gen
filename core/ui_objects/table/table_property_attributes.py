from enum import Enum
from typing import Literal
from core.ui_objects.base.base_attribute import EnumAttribute, TwipsAttribute
from core.ui_objects.base.base_attribute import BaseAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.utils.metrics import Twips


class JustificationVal(EnumAttribute):
    class Options(Enum):
        none = None
        left = "left"
        right = "right"
        center = "center"

    def __init__(self, value: str | Options | None):
        super().__init__(xml_name="w:val", value=value)


ValSpec = (
    Literal["left", "right", "center"]
    | JustificationVal.Options
    | None
    | JustificationVal
)


class Justification(BaseContentTag):
    """
    This element specifies the table alignment
    which shall be applied to table in this paragraph.
    """

    __slots__ = ("_val",)

    @property
    def tag(self) -> str:
        return "w:jc"

    def __init__(self, val: ValSpec = None):
        self.val = val

    @property
    def val(self) -> JustificationVal:
        if not isinstance(self._val, JustificationVal):
            raise AttributeError(
                f"Attribute <val> has not type(Val) Its type - {type(self._type)}!"
            )
        return self._val.value

    @val.setter
    def val(self, new_val: ValSpec):
        if not new_val:
            self._val = JustificationVal(JustificationVal.Options.none)
        elif isinstance(new_val, str | JustificationVal.Options):
            self._val = JustificationVal(new_val)
        elif isinstance(new_val, JustificationVal):
            self._val = JustificationVal
        else:
            raise TypeError(f"Wrong type for w:type!: {type(new_val)}")


class CellType(EnumAttribute):
    class Options(Enum):
        dxa = "dxa"
        nil = "nil"
        pct = "pct"
        auto = "auto"

    def __init__(self, value):
        super().__init__(xml_name="w:type", value=value)


CellTypeSpec = Literal["dxa", "nil", "pct", "auto"] | CellType.Options | CellType


CellWidthSpec = Twips | None


class CellWidthAttribute(TwipsAttribute):
    # TODO add PercentAttribute because CellWidth can also be in percent
    def __init__(self, value: Twips = None):
        super().__init__(xml_name="w:w", value=value)


class TableStyle(BaseContentTag):
    __slots__ = ("_val",)

    def __init__(self, val=None):
        self.style = val

    @property
    def tag(self) -> str:
        return "w:tblStyle"

    @property
    def style(self) -> str:
        return self._val.value

    @style.setter
    def style(self, style_name: str):
        if isinstance(style_name, str):
            self._val = StyleVal(style_name)
        elif isinstance(style_name, StyleVal):
            self._val = style_name
        else:
            raise ValueError(f"style id must be str | StyleVal not {type(style_name)}")


class StyleVal(BaseAttribute):
    def __init__(self, value: str = None):
        super().__init__(xml_name="w:val")
        self._val = value

    @property
    def value(self):
        return self._val

    @value.setter
    def value(self, new: str):
        if isinstance(new, str):
            self._val = new
        else:
            raise ValueError(f"style value must be str not {type(new)}")
