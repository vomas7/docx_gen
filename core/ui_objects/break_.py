from enum import Enum

from core.ui_objects.base.base_attribute import EnumAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag


class Type(EnumAttribute):
    class Options(Enum):
        line = None
        page = "page"
        column = "column"
        textwrapping = "textWrapping"

    def __init__(self, value: str):
        super().__init__(xml_name="w:type", value=value)


class Clear(EnumAttribute):
    def __init__(self, value: str):
        super().__init__(xml_name="w:clear", value=value)

    class Options(Enum):
        empty = None
        left = "left"
        right = "right"
        all = "all"


class Break(BaseContentTag):
    """Break tag <w:br> assignment"""

    __slots__ = ("_type", "_clear")

    def __init__(self, type: str | Type = None, clear: str | Clear = None):
        self.clear = Clear(clear)
        self.type = Type(type)

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
    def type(self, new_type: Type | str):
        if isinstance(new_type, str):
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
    def clear(self, new_clear: str | Clear):
        if isinstance(new_clear, str):
            self._clear = Clear(new_clear)
        elif isinstance(new_clear, Clear):
            self._clear = new_clear
        else:
            raise ValueError(f"Wrong type for w:clear!: {new_clear}")
