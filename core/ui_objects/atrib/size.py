from core.ui_objects.base.base_attribute import SimpleAttribute


class Height(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="w:h")


class Width(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="w:w")
