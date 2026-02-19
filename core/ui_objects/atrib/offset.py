from core.ui_objects.base.base_attribute import SimpleAttribute


class X(SimpleAttribute):
    """Позиция X для элемента off"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:x")




class Y(SimpleAttribute):
    """Позиция Y для элемента off"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:y")

