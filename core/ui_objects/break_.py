from enum import Enum
from typing import Literal

from core.ui_objects.base.base_attribute import EnumAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag


class Type(EnumAttribute):
    class Options(Enum):
        line = None
        page = "page"
        column = "column"
        textwrapping = "textWrapping"

    def __init__(self, value: str | Options | None):
        super().__init__(xml_name="w:type", value=value)


TypeSpec = (
    Literal["page", "column", "textWrapping", "line"] | Type.Options | None | Type
)


class Clear(EnumAttribute):
    class Options(Enum):
        empty = None
        left = "left"
        right = "right"
        all = "all"

    def __init__(self, value: str | Options | None):
        super().__init__(xml_name="w:clear", value=value)


ClearSpec = Literal["left", "right", "all", "empty"] | Clear.Options | None | Clear


class Break(BaseContentTag):
    """Break tag <w:br> assignment"""

    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "w:br"

    @property
    def type(self) -> Type:
        if not isinstance(self._type, Type):
            raise AttributeError(
                f"Attribute <type> has not type(BreakTypeAttribute) "
                f"Its type - {type(self._type)}!"
            )
        return self._type.value

    @type.setter
    def type(self, new_type: TypeSpec):
        if not new_type:
            self._type = Type(Type.Options.line)
        elif isinstance(new_type, (str, Type.Options)):
            self._type = Type(new_type)
        elif isinstance(new_type, Type):
            self._type = new_type
        else:
            raise TypeError(f"Wrong type for w:type!: {type(new_type)}")

    @property
    def clear(self) -> Clear:
        if not isinstance(self._clear, Clear):
            raise AttributeError(
                f"Attribute <w:clear> has not type(BreakClearAttribute)"
                f"Its has type: {type(self._clear)}!"
            )
        return self._clear.value

    @clear.setter
    def clear(self, new_clear: ClearSpec):
        if not new_clear:
            self._clear = Clear(Clear.Options.empty)
        elif isinstance(new_clear, str):
            self._clear = Clear(new_clear)
        elif isinstance(new_clear, Clear):
            self._clear = new_clear
        else:
            raise ValueError(f"Wrong type for w:clear!: {new_clear}")


BreakSpec = Literal["page", "column", "textWrapping"] | Break
