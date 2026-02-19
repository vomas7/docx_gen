from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


class GraphicFrameLocksNS(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="xmlns:a")


class NoChangeAspect(EnumAttribute):
    """Запрет изменения пропорций"""

    def __init__(self, value: "NoChangeAspect.Options"):
        super().__init__(value=value, xml_name="a:noChangeAspect")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeArrowheads(EnumAttribute):
    """Запрет изменения стрелок (для линий)"""

    def __init__(self, value: "NoChangeArrowheads.Options"):
        super().__init__(value=value, xml_name="a:noChangeArrowheads")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoEditPoints(EnumAttribute):
    """Запрет редактирования точек фигуры"""

    def __init__(self, value: "NoEditPoints.Options"):
        super().__init__(value=value, xml_name="a:noEditPoints")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoAdjustHandles(EnumAttribute):
    """ Запрет изменения ручек настройки"""

    def __init__(self, value: "NoAdjustHandles.Options"):
        super().__init__(value=value, xml_name="a:noAdjustHandles")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeShapeType(EnumAttribute):
    """Запрет изменения типа фигуры"""

    def __init__(self, value: "NoChangeShapeType.Options"):
        super().__init__(value=value, xml_name="a:noChangeShapeType")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeStart(EnumAttribute):
    """Запрет изменения начальной точки"""

    def __init__(self, value: "NoChangeStart.Options"):
        super().__init__(value=value, xml_name="a:noChangeStart")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeEnd(EnumAttribute):
    """Запрет изменения конечной точки"""

    def __init__(self, value: "NoChangeEnd.Options"):
        super().__init__(value=value, xml_name="a:noChangeEnd")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoMove(EnumAttribute):
    """Запрет перемещения"""

    def __init__(self, value: "NoMove.Options"):
        super().__init__(value=value, xml_name="a:noMove")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoResize(EnumAttribute):
    """Запрет изменения размера"""

    def __init__(self, value: "NoResize.Options"):
        super().__init__(value=value, xml_name="a:noResize")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoRotate(EnumAttribute):
    """Запрет вращения"""

    def __init__(self, value: "NoRotate.Options"):
        super().__init__(value=value, xml_name="a:noRotate")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoSelect(EnumAttribute):
    """Запрет выделения"""

    def __init__(self, value: "NoSelect.Options"):
        super().__init__(value=value, xml_name="a:noSelect")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoCrop(EnumAttribute):
    """Запрет обрезки"""

    def __init__(self, value: "NoCrop.Options"):
        super().__init__(value=value, xml_name="a:noCrop")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeBullet(EnumAttribute):
    """Запрет изменения маркеров (для списков)"""

    def __init__(self, value: "NoChangeBullet.Options"):
        super().__init__(value=value, xml_name="a:noChangeBullet")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoGrp(EnumAttribute):
    """Запрет группировки"""

    def __init__(self, value: "NoGrp.Options"):
        super().__init__(value=value, xml_name="a:noGrp")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoUngrp(EnumAttribute):
    """Запрет разгруппировки"""

    def __init__(self, value: "NoUngrp.Options"):
        super().__init__(value=value, xml_name="a:noUngrp")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoDrilldown(EnumAttribute):
    """Запрет детализации (SmartArt)"""

    def __init__(self, value: "NoDrilldown.Options"):
        super().__init__(value=value, xml_name="a:noDrilldown")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoTextEdit(EnumAttribute):
    """Запрет редактирования текста"""

    def __init__(self, value: "NoTextEdit.Options"):
        super().__init__(value=value, xml_name="a:noTextEdit")

    class Options(Enum):
        access = "0"
        restrict = "1"
