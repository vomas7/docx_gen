from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import LinkedObjects
from core.ui_objects.break_ import Break, BreakSpec
from core.ui_objects.text import Bold, Font, Italic, Tab, Text


class RunProperty(BaseContainerTag):
    __slots__ = ("_bold", "_italic", "_font")

    def __init__(
        self,
        linked_objects: LinkedObjects | list = None,
        bold: bool = False,
        italic: bool = False,
        font: str = None,
    ):
        super().__init__(linked_objects)
        self.bold = bold
        self.italic = italic
        self.font = font

    @property
    def tag(self):
        return "w:rPr"

    @property
    def access_children(self):
        return {Bold, Italic, Font}

    @property
    def bold(self):
        """Bold of text - True | False"""
        return self._bold

    @bold.setter
    def bold(self, value: bool):
        """Set bold for contain text in rPr"""
        if value:
            self._bold = True
            self.add(Bold(), 0)
        elif not value:
            self.remove_children(Bold)
            self._bold = False
        else:
            TypeError(f"value must be bool not {type(value)}")

    @property
    def italic(self):
        """italic of text - True | False"""
        return self._italic

    @italic.setter
    def italic(self, value: bool):
        """Set italic for contain text in rPr"""
        if value:
            self._italic = True
            self.add(Italic(), 0)
        elif not value:
            self.remove_children(Italic)
            self._italic = False
        else:
            TypeError(f"value must be bool not {type(value)}")

    @property
    def font(self):
        if self._font:
            return self._font.name

    @font.setter
    def font(self, value: str):
        if not value:
            self.remove_children(Font)
            self._font = None
        elif isinstance(value, str):
            self._font = Font(value)
            self.add(self._font)
        else:
            TypeError("value of font must be name of font!")


class Run(BaseContainerTag):
    __slots__ = ("run_property", "_bold", "_italic")

    def __init__(
        self,
        linked_objects: LinkedObjects | list = None,
        bold: Bold | bool = False,
        italic: Italic | bool = False,
        font: Font | str = None,
    ):
        super().__init__(linked_objects)
        self.run_property = RunProperty()
        self.bold = bold
        self.italic = italic
        self.font = font

    @property
    def tag(self):
        return "w:r"

    @property
    def access_children(self):
        return {Break, Text, RunProperty, Tab}

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

    def _update_run(self):
        if self._has_any_property() and not self._has_property_in_linked_objects():
            self.add(self.run_property, 0)
        elif not self._has_any_property() and self._has_property_in_linked_objects():
            self.remove_children(RunProperty)

    def _has_property_in_linked_objects(self) -> bool:
        return bool(self.find(RunProperty))

    def _has_any_property(self) -> bool:
        properties = [
            self.run_property.get_attribute(prop_name)
            for prop_name in self.run_property.__slots__
        ]
        return any(properties)

    @property
    def bold(self):
        return self.run_property.bold

    @bold.setter
    def bold(self, value: bool):
        """Set bold for contain text in Run"""
        self.run_property.bold = value
        self._update_run()

    def clear(self):
        """Clear all objects in linked objects"""
        self.linked_objects.clear()

    @property
    def contains_page_break(self):
        raise NotImplementedError

    @property
    def italic(self):
        """italic of text - True | False"""
        return self.run_property.italic

    @italic.setter
    def italic(self, value: bool):
        """Set italic for contain text in Run"""
        self.run_property.italic = value
        self._update_run()

    @property
    def font(self):
        return self.run_property.font

    @font.setter
    def font(self, value: str):
        self.run_property.font = value
        self._update_run()
