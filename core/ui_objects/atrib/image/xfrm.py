from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


# ========== АТРИБУТЫ ПОЗИЦИИ ==========

class OffX(SimpleAttribute):
    """Позиция X (в EMU)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:x")


class OffY(SimpleAttribute):
    """Позиция Y (в EMU)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:y")


# ========== АТРИБУТЫ РАЗМЕРА ==========

class ExtCx(SimpleAttribute):
    """Ширина (в EMU)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:cx")


class ExtCy(SimpleAttribute):
    """Высота (в EMU)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:cy")


# ========== АТРИБУТЫ ВРАЩЕНИЯ И ОТРАЖЕНИЯ ==========

class Rot(SimpleAttribute):
    """Вращение (в 60000-х долях градуса)"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="a:rot")


class FlipH(EnumAttribute):
    """Отражение по горизонтали"""

    def __init__(self, value: "FlipH.Options"):
        super().__init__(value=value, xml_name="a:flipH")

    class Options(Enum):
        no_flip = "0"
        flip = "1"


class FlipV(EnumAttribute):
    """Отражение по вертикали"""

    def __init__(self, value: "FlipV.Options"):
        super().__init__(value=value, xml_name="a:flipV")

    class Options(Enum):
        no_flip = "0"
        flip = "1"


# ========== АТРИБУТ ДЛЯ SpPr ==========

class BwMode(SimpleAttribute):
    """Режим черно-белого отображения"""

    def __init__(self, value: str = "auto"):
        super().__init__(value=value, xml_name="pic:bwMode")

    # class Options(Enum):
    #     auto = "auto"  # Автоматический
    #     white = "white"  # Белый
    #     black = "black"  # Черный
    #     hidden = "hidden"  # Скрытый
    #     gray = "gray"  # Серый
    #     lt_gray = "ltGray"  # Светло-серый
    #     inv_gray = "invGray"  # Инвертированный серый
    #     gray_white = "grayWhite"  # Серо-белый
    #     black_gray = "blackGray"  # Черно-серый
    #     black_white = "blackWhite"  # Черно-белый
    #     color = "color"  # Цветной
