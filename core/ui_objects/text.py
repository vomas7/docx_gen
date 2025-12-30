from typing import Self

from core.ui_objects.base.base_attribute import BaseAttribute
from core.ui_objects.base.base_content_tag import BaseContentTag


class Text(BaseContentTag):
    """tag <w:t> text assignment"""

    def __init__(self, text: Self | str = ""):
        self._text = text.text if isinstance(text, self.__class__) else text

    def __str__(self) -> str:
        return f"Text({self._text})"

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, new_text: str):
        self._text = str(new_text)

    @property
    def tag(self) -> str:
        return "w:t"


class Tab(BaseContentTag):
    @property
    def tag(self) -> str:
        return "w:tab"


class Bold(BaseContentTag):
    @property
    def tag(self) -> str:
        return "w:b"


class Italic(BaseContentTag):
    @property
    def tag(self) -> str:
        return "w:i"


class Ascii(BaseAttribute):
    def __init__(self, ascii: str = "Times New Roman"):
        super().__init__(xml_name="w:ascii")
        self._ascii = ascii

    @property
    def value(self):
        return self._ascii

    @value.setter
    def value(self, another: str):
        if isinstance(another, str) and another.isalpha():
            self._ascii = str(another)


class HAnsi(BaseAttribute):
    def __init__(self, hAnsi: str = "Times New Roman"):
        super().__init__(xml_name="w:hAnsi")
        self._hAnsi = hAnsi

    @property
    def value(self):
        return self._hAnsi

    @value.setter
    def value(self, another: str):
        if isinstance(another, str) and another.isalpha():
            self._hAnsi = str(another)


class Font(BaseContentTag):
    __slots__ = ("_ascii", "_hansi")

    @property
    def tag(self) -> str:
        return "w:rFonts"

    def __init__(self, name: str = "Times New Roman"):
        self.hansi = HAnsi(name)
        self.ascii = Ascii(name)

    @property
    def name(self):
        return self.ascii if self.ascii else self.hansi

    @property
    def ascii(self):
        return self._ascii.value

    @ascii.setter
    def ascii(self, value: str):
        self._ascii = value

    @property
    def hansi(self):
        return self._hansi.value

    @hansi.setter
    def hansi(self, value: str):
        self._hansi = value

    def __str__(self):
        return f"Font({str(self.ascii)})"

    def __repr__(self):
        return self.__str__()
