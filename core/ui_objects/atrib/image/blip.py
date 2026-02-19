from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


# ========== ПРОЗРАЧНОСТЬ ==========


class Embed(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="r:embed")


class CState(EnumAttribute):
    """Состояние сжатия изображения"""

    def __init__(self, value: str = "print"):
        super().__init__(value=value, xml_name="a:cstate")

    class Options(Enum):
        print = "print"
        screen = "screen"
        hq = "hq"
        always = "always"


class AlphaMod(SimpleAttribute):
    """Модификатор прозрачности (0-100000)"""

    def __init__(self, value: str = "10000"):
        super().__init__(value=value, xml_name="a:alphaMod")


class AlphaModFix(SimpleAttribute):
    """Фиксированный модификатор прозрачности (0-100000)"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="a:alphaModFix")


# ========== ЯРКОСТЬ И КОНТРАСТ ==========

class Gain(SimpleAttribute):
    """Усиление яркости (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:gain")


class BlackLevel(SimpleAttribute):
    """Уровень черного (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:blackLevel")


class Gamma(SimpleAttribute):
    """Гамма-коррекция (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:gamma")


# ========== ОСНОВНЫЕ ЦВЕТА ==========


class Gray(SimpleAttribute):
    """Коррекция серого канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:gray")


class Red(SimpleAttribute):
    """Коррекция красного канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:red")


class Green(SimpleAttribute):
    """Коррекция зеленого канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:green")


class Blue(SimpleAttribute):
    """Коррекция синего канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:blue")


# ========== МОДИФИКАТОРЫ ЦВЕТОВ ==========

class RedMod(SimpleAttribute):
    """Модификатор красного канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:redMod")


class GreenMod(SimpleAttribute):
    """Модификатор зеленого канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:greenMod")


class BlueMod(SimpleAttribute):
    """Модификатор синего канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:blueMod")


# ========== HSL (HUE, SATURATION, LUMINANCE) ==========

class Hue(SimpleAttribute):
    """Оттенок (0-21600000, где 21600000 = 360°)"""

    def __init__(self, value: str = "10000"):
        super().__init__(value=value, xml_name="a:hue")


class HueMod(SimpleAttribute):
    """Модификатор оттенка (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:hueMod")


class Sat(SimpleAttribute):
    """Насыщенность (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:sat")


class SatMod(SimpleAttribute):
    """Модификатор насыщенности (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:satMod")


class Lum(SimpleAttribute):
    """Яркость (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:lum")


class LumMod(SimpleAttribute):
    """Модификатор яркости (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:lumMod")


# ========== КОНТРАСТ И РЕЗКОСТЬ ==========

class Cont(SimpleAttribute):
    """Контрастность (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:cont")


class ContMod(SimpleAttribute):
    """Модификатор контрастности (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="a:contMod")


class Sharp(SimpleAttribute):
    """Резкость (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:sharp")


# ========== ДРУГИЕ ЭФФЕКТЫ ==========

class Shade(SimpleAttribute):
    """Затемнение (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:shade")


class Tint(SimpleAttribute):
    """Тонирование (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="a:tint")


# ========== ЦВЕТА ЗАЛИВКИ ==========

class BuClr(SimpleAttribute):
    """Цвет фона (background color) в формате RRGGBB hex"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="a:buClr")


class BuClrTx(SimpleAttribute):
    """Цвет текста фона (background color text) в формате RRGGBB hex"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="a:buClrTx")
