from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Objects, Property
from core.ui_objects.break_ import Break, BreakSpec
from core.ui_objects.text import Bold, Font, Italic, Tab, Text
from core.ui_objects.image.image import Drawing


class RunProperty(BaseContainerTag):
    __slots__ = ("_bold", "_italic", "_font")

    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
        bold: bool = False,
        italic: bool = False,
        font: str = None,
    ):
        super().__init__(objects, property)
        self.bold = bold
        self.italic = italic
        self.font = font

    @property
    def tag(self):
        return "w:rPr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": Bold}, {"class": Italic}, {"class": Font}]

    @property
    def access_property(self) -> list[dict]:
        return list()

    @property
    def bold(self):
        """Bold of text - True | False"""
        return self._bold

    @bold.setter
    def bold(self, value: bool):
        """Set bold for contain text in rPr"""
        if isinstance(value, bool) and value:
            self._bold = True
            self.add(Bold())
        elif isinstance(value, bool) and not value:
            self.remove_children(Bold)
            self._bold = False
        else:
            raise TypeError(f"Bold value must be bool not {type(value)}")

    @property
    def italic(self):
        """italic of text - True | False"""
        return self._italic

    @italic.setter
    def italic(self, value: bool):
        """Set italic for contain text in rPr"""
        if isinstance(value, bool) and value:
            self._italic = True
            self.add(Italic())
        elif isinstance(value, bool) and not value:
            self.remove_children(Italic)
            self._italic = False
        else:
            raise TypeError(f"Italic value must be bool not {type(value)}")

    @property
    def font(self):
        return self._font

    @font.setter
    def font(self, value: str):
        if isinstance(value, str):
            self._font = value
            self.add(Font(value))
        elif not value:
            self.remove_children(Font)
            self._font = None
        else:
            raise TypeError(f"font value must be str not {type(value)}")


class Run(BaseContainerTag):
    __slots__ = ("_bold", "_italic", "_font")

    def __init__(
        self,
        objects: Objects | list = None,
        property: Property | list = None,
        bold: Bold | bool = False,
        italic: Italic | bool = False,
        font: Font | str = None,
    ):
        super().__init__(objects, property)
        self.bold = bold
        self.italic = italic
        self.font = font

    @property
    def tag(self):
        return "w:r"

    @property
    def access_children(self):
        return [
            {"class": Break},
            {"class": Text},
            {"class": Tab},
            {"class": Drawing},
        ]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": RunProperty, "required_position": 0}]

    def add_break(self, break_: BreakSpec, index: int = -1):
        """Adds a break (page or column) to the Run"""
        if not break_:
            raise TypeError("Cannot add break: break_ cannot be None")
        elif isinstance(break_, str):
            self.add(Break(type=break_), index)
        elif isinstance(break_, Break):
            self.add(break_, index)
        else:
            raise TypeError(f"break_ must be str or Break, not {type(break_).__name__}")

    def add_picture(self):
        raise NotImplementedError

    def add_text(self, text: Text | str, index: int = -1):
        """
        Add text to the Run.
        Strings are automatically converted to Text objects.
        """
        self.add(Text(text), index)

    def add_tab(self, index: int = -1):
        """Add tab (\t) to the Run"""
        self.add(Tab(), index)

    @property
    def run_property(self):
        return self.get_property("RunProperty")

    @property
    def bold(self):
        """Bold of text - True | False"""
        return self._get_property_attr(RunProperty, "bold")

    @bold.setter
    @BaseContainerTag.autoclean
    def bold(self, value: bool):
        """Set bold for contain text in Run"""
        self._set_property_attr(RunProperty, "bold", value)

    @property
    def contains_page_break(self) -> bool:
        return bool(self.find(Break))

    @property
    def italic(self):
        """italic of text - True | False"""
        return self._get_property_attr(RunProperty, "italic")

    @italic.setter
    @BaseContainerTag.autoclean
    def italic(self, value: bool):
        """Set italic for contain text in Run"""
        self._set_property_attr(RunProperty, "italic", value)

    @property
    def font(self):
        return self._get_property_attr(RunProperty, "font")

    @font.setter
    @BaseContainerTag.autoclean
    def font(self, value: str):
        self._set_property_attr(RunProperty, "font", value)
