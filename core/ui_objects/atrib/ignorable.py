from core.ui_objects.base.base_attribute import BaseAttribute

class IgnorableAttribute(BaseAttribute):
    def __init__(self, xml_name: str, value: str):
        self.value = value
        super().__init__(xml_name)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, another: str | int | float):
        if isinstance(another, str):
            self._value = another
        else:
            TypeError(f"another must be str not {type(another)}")

    @property
    def xml_name(self):
        return self._xml_name


class Ignorable(IgnorableAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="mc:Ignorable")
