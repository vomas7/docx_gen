from enum import Enum
from typing import Literal

from core.ui_objects.base.base_attribute import EnumAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag


class Val(EnumAttribute):
    class Options(Enum):
        none = None
        left = "left"
        right = "right"
        center = "center"

    def __init__(self, value: str | Options | None):
        super().__init__(xml_name="w:val", value=value)


ValSpec = Literal["left", "right", "center"] | Val.Options | None | Val


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
    def val(self) -> Val:
        if not isinstance(self._val, Val):
            raise AttributeError(
                f"Attribute <val> has not type(Val) Its type - {type(self._type)}!"
            )
        return self._val.value

    @val.setter
    def val(self, new_val: ValSpec):
        if not new_val:
            self._val = Val(Val.Options.none)
        elif isinstance(new_val, str | Val.Options):
            self._val = Val(new_val)
        elif isinstance(new_val, Val):
            self._val = Val
        else:
            raise TypeError(f"Wrong type for w:type!: {type(new_val)}")
