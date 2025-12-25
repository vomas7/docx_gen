from core.ui_objects.base.base_attribute import SimpleAttribute

# here are the attributes that responsible for the reference


class Header(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:header")


class Footer(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:footer")


class Gutter(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:gutter")
