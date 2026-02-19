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
        if self.property:
            run_property = self.property[0]
            if isinstance(run_property, RunProperty):
                return run_property
        return None

    @property
    def bold(self):
        """Bold of text - True | False"""
        return self.get_from_run_property("bold")

    @bold.setter
    def bold(self, value: bool):
        """Set bold for contain text in Run"""
        self.set_run_property("bold", value)
        self._update_properties()

    def clear(self):
        """Clear all objects in linked objects"""
        self.objects.clear()

    @property
    def contains_page_break(self):
        raise NotImplementedError

    @property
    def italic(self):
        """italic of text - True | False"""
        return self.get_from_run_property("italic")

    @italic.setter
    def italic(self, value: bool):
        """Set italic for contain text in Run"""
        self.set_run_property("italic", value)
        self._update_properties()

    @property
    def font(self):
        return self.get_from_run_property("font")

    @font.setter
    def font(self, value: str):
        self.set_run_property("font", value)
        self._update_properties()

    def get_from_run_property(self, property_name: str) -> bool | str | None:
        """Getter of property rPr"""
        if self.run_property:
            return self.run_property.get_attribute(property_name)
        return None

    def set_run_property(self, property_name: str, value) -> None:
        """Setter property rPr"""
        if not self.run_property:
            run_property = RunProperty()
            setattr(run_property, property_name, value)
            self.property.insert(0, run_property)
        else:
            setattr(self.run_property, property_name, value)

    def _update_properties(self):
        if self.run_property and not self._has_any_property():
            self.property.remove(self.run_property)

    def _has_any_property(self) -> bool:
        properties = [
            self.get_from_run_property(prop_name)
            for prop_name in self.run_property.__slots__
        ]
        return any(properties)
