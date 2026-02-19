from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum

class ObjectId(SimpleAttribute):
    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="pic:id")


class ObjectName(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="pic:name")


class ObjectDescr(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="pic:descr")


class ObjectTitle(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="pic:title")


class ObjectHidden(EnumAttribute):

    def __init__(self, value: "ObjectHidden.Options"):
        super().__init__(value=value, xml_name="pic:hidden")

    class Options(Enum):
        hidden = "1"
        visible = "0"
