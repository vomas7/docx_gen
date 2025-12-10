from enum import Enum
from core.ui_objects.base.BaseAttribute import EnumAttribute
from core.ui_objects.base.BaseContentTag import BaseContentTag


class BreakTypeAttribute(EnumAttribute):

    class BreakTypes(Enum):
        line = None
        page = "page"
        column = "column"
        textwrapping = "textWrapping"

    def __init__(self, value: str):
        super().__init__(
            namespace="w",
            xml_name="type",
            name="type",
            value=value
        )


class BreakClearAttribute(EnumAttribute):

    def __init__(self, value: str):
        super().__init__(
            namespace="w",
            xml_name="clear",
            name="clear",
            value=value
        )

    class ClearTypes(Enum):
        empty = None
        left = 'left'
        right = 'right'
        all = 'all'


class Break(BaseContentTag):
    """Break tag <w:br> assignment"""

    __slots__ = ('_type', '_clear')

    def __init__(self,
                 type: str | BreakTypeAttribute = None,
                 clear: str | BreakClearAttribute = None):
        self.clear = BreakClearAttribute(clear)
        self.type = BreakTypeAttribute(type)

    @property
    def tag(self) -> str:
        return 'w:br'

    @property
    def type(self) -> BreakTypeAttribute:
        if not isinstance(self._type, BreakTypeAttribute):
            raise AttributeError(
                f"Attribute <type> has not type(BreakTypeAttribute) "
                f"Its type - {type(self._type)}!"
            )
        return self._type.value

    @type.setter
    def type(self, new_type: BreakTypeAttribute | str):
        if isinstance(new_type, str):
            self._type = BreakTypeAttribute(new_type)
        elif isinstance(new_type, BreakTypeAttribute):
            self._type = new_type
        else:
            raise TypeError(f"Wrong type for w:type!: {type(new_type)}")

    @property
    def clear(self) -> BreakClearAttribute:
        if not isinstance(self._clear, BreakClearAttribute):
            raise AttributeError(
                f"Attribute <w:clear> has not type(BreakClearAttribute)"
                f"Its has type: {type(self._clear)}!"
            )
        return self._clear.value

    @clear.setter
    def clear(self, new_clear: str | BreakClearAttribute):
        if isinstance(new_clear, str):
            self._clear = BreakClearAttribute(new_clear)
        elif isinstance(new_clear, BreakClearAttribute):
            self._clear = new_clear
        else:
            raise ValueError(
                f"Wrong type for w:clear!: {new_clear}"
            )
