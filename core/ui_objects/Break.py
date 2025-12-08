from enum import Enum
from typing import Literal
from docx.enum.text import WD_BREAK_TYPE
from core.ui_objects.base import BaseNonContainerDocx


class BreakTypes(Enum):
    line = None
    page = "page"
    column = "column"
    textwrapping = "textWrapping"


class ClearTypes(Enum):
    empty = None
    left = 'left'
    right = 'right'
    all = 'all'


Types = str | WD_BREAK_TYPE | BreakTypes | Literal[6, 7, 8, 9, 10, 11] | None


class Break(BaseNonContainerDocx):
    """Break tag <w:br> assignment"""

    __slots__ = ('__type', '__clear')

    def __init__(self,
                 type: Types = BreakTypes.line,
                 clear: str | ClearTypes | None = ClearTypes.empty):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return 'w:br'

    @property
    def type(self) -> str:
        if not isinstance(self.__type, BreakTypes):
            raise AttributeError(
                f"Attribute <w:type> has not type(BrakeTypes) "
                f"Its type - {type(self.__type)}!"
            )
        return self.__type.value

    @type.setter
    def type(self, new_type: Types):

        if not new_type:
            self.__type = BreakTypes.line

        elif isinstance(new_type, str):
            self.__type = getattr(BreakTypes, new_type.lower().strip())

        elif isinstance(new_type, BreakTypes):
            self.__type = new_type

        elif isinstance(new_type, int) or isinstance(new_type, WD_BREAK_TYPE):
            new_type = int(new_type) if isinstance(new_type, int) \
                else new_type.value
            if new_type <= 6:
                self.__type = BreakTypes.line
            elif 6 < new_type < 9:
                self.__type = BreakTypes.page if new_type == 7 \
                    else BreakTypes.column
            elif 9 <= new_type <= 11:
                self.__type = BreakTypes.textwrapping
                if new_type == 9:
                    self.__clear = ClearTypes.left
                elif new_type == 10:
                    self.__clear = ClearTypes.right
                else:
                    self.__clear = ClearTypes.all
            else:
                raise ValueError(f"Unable to determine type number {new_type}")

        else:
            raise ValueError(f"Unable to determine type {new_type}")

    @property
    def clear(self) -> str:
        if not isinstance(self.__clear, ClearTypes):
            raise AttributeError(
                f"Attribute <w:clear> has not type(ClearTypes)"
                f"Its has type: {type(self.__clear)}!"
            )
        return self.__clear.value

    @clear.setter
    def clear(self, new_clear: str | ClearTypes):
        if isinstance(new_clear, str):
            self.__clear = getattr(ClearTypes, new_clear.lower().strip())
        elif isinstance(new_clear, ClearTypes):
            self.__clear = new_clear
        else:
            raise ValueError(
                f"Validation error: Unable to determine clear {new_clear}"
            )

a = Break()

print(a.attrs)
