from core.ui_objects.base.base_attribute import TwipsAttribute, SimpleAttribute
from core.utils.metrics import Length


class Height(TwipsAttribute):
    def __init__(self, value: Length):
        super().__init__(value=value, xml_name="w:h")


class Width(TwipsAttribute):
    def __init__(self, value: Length):
        super().__init__(value=value, xml_name="w:w")


class CX(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="a:cx")


class CY(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="a:cy")


class EffectLeft(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:l")


class EffectTop(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:t")


class EffectRight(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:r")


class EffectBottom(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:b")
