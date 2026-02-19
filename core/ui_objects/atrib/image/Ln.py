from core.ui_objects.base.base_attribute import SimpleAttribute


class LineWidth(SimpleAttribute):
    """Ширина линии в EMU"""

    def __init__(self, value: str = "9525"):
        super().__init__(value=value, xml_name="a:w")


class LineCap(SimpleAttribute):
    """Тип окончания линии"""

    def __init__(self, value: str = "flat"):
        super().__init__(value=value, xml_name="a:cap")

    # class Options(Enum):
    #     flat = "flat"  # Прямое окончание
    #     round = "round"  # Скругленное окончание
    #     square = "square"  # Квадратное окончание


class LineCmpd(SimpleAttribute):
    """Составная линия"""

    def __init__(self, value: str = "sng"):
        super().__init__(value=value, xml_name="a:cmpd")

    # class Options(Enum):
    #     sng = "sng"  # Одинарная
    #     dbl = "dbl"  # Двойная
    #     thickThin = "thickThin"  # Толстая-тонкая
    #     thinThick = "thinThick"  # Тонкая-толстая
    #     tri = "tri"  # Тройная


class LineAlign(SimpleAttribute):
    """Выравнивание линии"""

    def __init__(self, value: str = "ctr"):
        super().__init__(value=value, xml_name="a:align")

    # class Options(Enum):
    #     ctr = "ctr"  # По центру границы фигуры
    #     in_ = "in"  # Внутри границы фигуры
    #     out = "out"  # Снаружи границы фигуры
