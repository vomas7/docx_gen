from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import Objects
from core.ui_objects.atrib.margins import DistTop, DistRight, DistLeft, DistBottom
from core.ui_objects.atrib.ids import AnchorId, EditId
import uuid
from core.ui_objects.atrib.size import CX, CY
from core.ui_objects.atrib.size import EffectLeft, EffectRight, EffectTop, EffectBottom
from core.ui_objects.atrib.image.xfrm import (
    OffX,
    OffY,
    ExtCx,
    ExtCy,
    Rot,
    FlipH,
    FlipV,
    BwMode,
)
from core.ui_objects.atrib.image.PrstGeom import Prst
from core.ui_objects.atrib.offset import X, Y
from core.ui_objects.atrib.image.Ln import LineCap, LineCmpd, LineAlign, LineWidth

from core.ui_objects.atrib.image.image import (
    ImageName,
    ImageHidden,
    ImageDescr,
    ImageId,
    ImageTitle,
    Dpi,
    URIGraphicData,
    URIExt,
    UseLocalDpiVal,
    UseLocalDpiNS,
)
from core.ui_objects.atrib.image.graphic_frame_locks import (
    NoChangeAspect,
    NoChangeArrowheads,
    NoEditPoints,
    NoAdjustHandles,
    NoChangeShapeType,
    NoChangeStart,
    NoChangeEnd,
    NoMove,
    NoResize,
    NoRotate,
    NoSelect,
    NoCrop,
    NoChangeBullet,
    NoGrp,
    NoUngrp,
    NoDrilldown,
    NoTextEdit,
    GraphicFrameLocksNS,
)
from core.ui_objects.atrib.image.CNvPr import (
    ObjectName,
    ObjectHidden,
    ObjectId,
    ObjectDescr,
    ObjectTitle,
)
from core.ui_objects.atrib.image.blip import (
    Embed,
    CState,
    AlphaMod,
    AlphaModFix,
    Gain,
    BlackLevel,
    Gamma,
    Gray,
    Red,
    Green,
    GreenMod,
    BlueMod,
    Blue,
    RedMod,
    Hue,
    HueMod,
    Lum,
    LumMod,
    Sat,
    SatMod,
    Shade,
    Cont,
    ContMod,
    Sharp,
    Tint,
    BuClr,
    BuClrTx,
)


class Extent(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self):
        self._width = CX("0")
        self._height = CY("0")

    @property
    def width(self):
        return self._width.value

    @width.setter
    def width(self, value):
        """take value in centimeters"""

        self._width.value = value

    @property
    def height(self):
        return self._height.value

    @height.setter
    def height(self, value):
        """take value in centimeters"""

        self._height.value = value

    def set_distances(self, width=10, height=10):
        """Установить все отступы одновременно"""
        self.width = width
        self.height = height

    @property
    def tag(self) -> str:
        return "wp:extent"


class EffectExtent(BaseContentTag):
    """Класс для тега <wp:effectExtent>"""

    __slots__ = ("_left", "_top", "_right", "_bottom")

    def __init__(self):
        self._left = EffectLeft("0")
        self._top = EffectTop("0")
        self._right = EffectRight("0")
        self._bottom = EffectBottom("0")

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left.value = value

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top.value = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right.value = value

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        self._bottom.value = value

    @property
    def tag(self):
        return "wp:effectExtent"


class DocProperties(BaseContentTag):
    """Класс для тега <wp:docPr> (Document Properties)"""

    __slots__ = ("_id", "_name", "_description", "_title", "_hidden")

    def __init__(self):
        self._id = ImageId("0")
        self._name = ImageName("")
        self._description = ImageDescr("")
        self._title = ImageTitle("")
        self._hidden = ImageHidden(ImageHidden.Options.visible)

    @property
    def id(self) -> str:
        """Уникальный идентификатор объекта"""
        return self._id.value

    @id.setter
    def id(self, value: int):
        self._id.value = str(value)

    @property
    def name(self) -> str:
        """Отображаемое имя объекта"""
        return self._name.value

    @name.setter
    def name(self, value: str):
        self._name.value = str(value)

    @property
    def description(self) -> str:
        """Описание объекта (альтернативный текст)"""
        return self._description.value

    @description.setter
    def description(self, value: str):
        self._description.value = str(value)

    @property
    def title(self) -> str:
        """Заголовок (всплывающая подсказка)"""
        return self._title.value

    @title.setter
    def title(self, value: str):
        self._title.value = str(value)

    @property
    def hidden(self) -> bool:
        """Скрыт ли объект?"""
        return self._hidden.value

    @hidden.setter
    def hidden(self, value: bool):
        self._hidden.value = (
            ImageHidden.Options.hidden if value else ImageHidden.Options.visible
        )

    @property
    def tag(self):
        return "wp:docPr"

    def __str__(self):
        return f"DocPr(id={self.id}, name='{self.name}')"


class GraphicFrameLocks(BaseContentTag):
    """
    DrawingML Graphic Frame Locks
    Блокировки для графического фрейма
    """

    __slots__ = (
        "_no_change_aspect",
        "_no_change_arrowheads",
        "_no_change_start",
        "_no_change_end",
        "_no_edit_points",
        "_no_adjust_handles",
        "_no_change_shape_type",
        "_no_move",
        "_no_resize",
        "_no_rotate",
        "_no_select",
        "_no_crop",
        "_no_change_bullet",
        "_no_grp",
        "_no_ungrp",
        "_no_drill_down",
        "_no_text_edit",
        "_xmlns",
    )

    def __init__(self):
        """Блокировка изменения пропорций (1 = да, 0 = нет)"""

        self._no_change_aspect = NoChangeAspect(NoChangeAspect.Options.access)
        self._no_change_arrowheads = NoChangeArrowheads(
            NoChangeArrowheads.Options.access
        )
        self._no_change_start = NoChangeStart(NoChangeStart.Options.access)
        self._no_change_end = NoChangeEnd(NoChangeEnd.Options.access)
        self._no_edit_points = NoEditPoints(NoEditPoints.Options.access)
        self._no_adjust_handles = NoAdjustHandles(NoAdjustHandles.Options.access)
        self._no_change_shape_type = NoChangeShapeType(NoChangeShapeType.Options.access)
        self._no_move = NoMove(NoMove.Options.access)
        self._no_resize = NoResize(NoResize.Options.access)
        self._no_rotate = NoRotate(NoRotate.Options.access)
        self._no_select = NoSelect(NoSelect.Options.access)
        self._no_crop = NoCrop(NoCrop.Options.access)
        self._no_change_bullet = NoChangeBullet(NoChangeBullet.Options.access)
        self._no_grp = NoGrp(NoGrp.Options.access)
        self._no_ungrp = NoUngrp(NoUngrp.Options.access)
        self._no_drill_down = NoDrilldown(NoDrilldown.Options.access)
        self._no_text_edit = NoTextEdit(NoTextEdit.Options.access)
        self._xmlns = GraphicFrameLocksNS("")

    @property
    def no_change_aspect(self):
        return self._no_change_aspect.value

    @no_change_aspect.setter
    def no_change_aspect(self, value: bool):
        self._no_change_aspect.value = (
            NoChangeAspect.Options.restrict
            if value
            else (NoChangeAspect.Options.access)
        )

    @property
    def no_change_arrowheads(self):
        return self._no_change_arrowheads.value

    @no_change_arrowheads.setter
    def no_change_arrowheads(self, value: bool):
        self._no_change_arrowheads.value = (
            NoChangeArrowheads.Options.restrict
            if value
            else NoChangeArrowheads.Options.access
        )

    @property
    def no_change_start(self):
        """Блокировка изменения начальной точки"""
        return self._no_change_start.value

    @no_change_start.setter
    def no_change_start(self, value: bool):
        self._no_change_start.value = (
            NoChangeStart.Options.restrict if value else NoChangeStart.Options.access
        )

    @property
    def no_change_end(self):
        """Блокировка изменения конечной точки"""
        return self._no_change_end.value

    @no_change_end.setter
    def no_change_end(self, value: bool):
        self._no_change_end.value = (
            NoChangeEnd.Options.restrict if value else NoChangeEnd.Options.access
        )

    @property
    def no_edit_points(self):
        """Запрет редактирования точек"""
        return self._no_edit_points.value

    @no_edit_points.setter
    def no_edit_points(self, value: bool):
        self._no_edit_points.value = (
            NoEditPoints.Options.restrict if value else NoEditPoints.Options.access
        )

    @property
    def no_adjust_handles(self):
        """Запрет изменения ручек настройки"""
        return self._no_adjust_handles

    @no_adjust_handles.setter
    def no_adjust_handles(self, value: bool):
        self._no_adjust_handles.value = (
            NoAdjustHandles.Options.restrict
            if value
            else NoAdjustHandles.Options.access
        )

    @property
    def no_change_shape_type(self):
        """Запрет изменения типа фигуры"""
        return self._no_change_shape_type.value

    @no_change_shape_type.setter
    def no_change_shape_type(self, value: bool):
        self._no_change_shape_type.value = (
            NoChangeShapeType.Options.restrict
            if value
            else NoChangeShapeType.Options.access
        )

    @property
    def no_move(self):
        """Запрет перемещения"""
        return self._no_move.value

    @no_move.setter
    def no_move(self, value: bool):
        self._no_move.value = (
            NoMove.Options.restrict if value else (NoMove.Options.access)
        )

    @property
    def no_resize(self):
        """Запрет изменения размера"""
        return self._no_resize.value

    @no_resize.setter
    def no_resize(self, value: bool):
        self._no_resize.value = (
            NoResize.Options.restrict if value else NoResize.Options.access
        )

    @property
    def no_rotate(self):
        """Запрет вращения"""
        return self._no_rotate.value

    @no_rotate.setter
    def no_rotate(self, value: bool):
        self._no_rotate.value = (
            NoRotate.Options.restrict if value else (NoRotate.Options.access)
        )

    @property
    def no_select(self):
        """Запрет выделения"""
        return self._no_select.value

    @no_select.setter
    def no_select(self, value: bool):
        self._no_select.value = (
            NoSelect.Options.restrict if value else (NoSelect.Options.access)
        )

    @property
    def no_crop(self):
        """Запрет обрезки"""
        return self._no_crop.value

    @no_crop.setter
    def no_crop(self, value: bool):
        self._no_crop.value = (
            NoCrop.Options.restrict if value else (NoCrop.Options.access)
        )

    @property
    def no_change_bullet(self):
        """Запрет обрезки"""
        return self._no_change_bullet.value

    @no_change_bullet.setter
    def no_change_bullet(self, value: bool):
        self._no_change_bullet.value = (
            NoChangeBullet.Options.restrict if value else NoChangeBullet.Options.access
        )

    @property
    def no_grp(self):
        """Запрет обрезки"""
        return self._no_grp.value

    @no_grp.setter
    def no_grp(self, value: bool):
        self._no_grp.value = NoGrp.Options.restrict if value else NoGrp.Options.access

    @property
    def no_ungrp(self):
        """Запрет обрезки"""
        return self._no_ungrp.value

    @no_ungrp.setter
    def no_ungrp(self, value: bool):
        self._no_ungrp.value = (
            NoUngrp.Options.restrict if value else NoUngrp.Options.access
        )

    @property
    def no_drill_down(self):
        """Запрет обрезки"""
        return self._no_drill_down.value

    @no_drill_down.setter
    def no_drill_down(self, value: bool):
        self._no_drill_down.value = (
            NoDrilldown.Options.restrict if value else (NoDrilldown.Options.access)
        )

    @property
    def no_text_edit(self):
        """Запрет обрезки"""
        return self._no_text_edit.value

    @no_text_edit.setter
    def no_text_edit(self, value: bool):
        self._no_text_edit.value = (
            NoTextEdit.Options.restrict if value else (NoTextEdit.Options.access)
        )

    @property
    def xmlns(self):
        """Запрет обрезки"""
        return self._xmlns.value

    @xmlns.setter
    def xmlns(self, value: str):
        self._xmlns.value = value

    @property
    def tag(self) -> str:
        return "a:graphicFrameLocks"


class CNvGraphicFramePr(BaseContainerTag):
    """
    Non-Visual Properties for a Graphic Frame
    Содержит свойства, которые не влияют на отображение графического фрейма
    """

    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "wp:cNvGraphicFramePr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": GraphicFrameLocks}]


class Pic(BaseContainerTag):
    """
    Picture element - основной контейнер для изображения
    Содержит все компоненты изображения
    """

    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:pic"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": NvPicPr}, {"class": BlipFill}, {"class": SpPr}]


class GraphicData(BaseContainerTag):
    """
    DrawingML Graphic Data element
    Содержит графические данные с указанием типа
    """

    __slots__ = ("_uri",)

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._uri = URIGraphicData(
            "http://schemas.openxmlformats.org/drawingml/2006/picture"
        )

    @property
    def uri(self) -> str:
        """URI типа графических данных"""
        return self._uri.value

    @uri.setter
    def uri(self, value: str):
        self._uri.value = str(value)

    @property
    def tag(self):
        return "a:graphicData"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": Pic}
            # todo here should be another tags
        ]


class Graphic(BaseContainerTag):
    """
    DrawingML Graphic element
    Основной контейнер для графических данных
    """

    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:graphic"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": GraphicData}]


class CNvPr(BaseContentTag):
    """
    Common Non-Visual Drawing Properties
    Общие свойства для всех графических объектов
    """

    __slots__ = ("_id", "_name", "_description", "_title", "_hidden")

    def __init__(self):
        self._id = ObjectId("0")
        self._name = ObjectName("")
        self._description = ObjectDescr("")
        self._title = ObjectTitle("")
        self._hidden = ObjectHidden(ObjectHidden.Options.hidden)

    @property
    def id(self) -> str:
        """Идентификатор объекта"""
        return self._id.value

    @id.setter
    def id(self, value: str):
        self._id.value = str(value)

    @property
    def name(self) -> str:
        """Имя объекта"""
        return self._name.value

    @name.setter
    def name(self, value: str):
        self._name.value = str(value)

    @property
    def description(self) -> str:
        """Описание (альтернативный текст)"""
        return self._description.value

    @description.setter
    def description(self, value: str):
        self._description.value = str(value)

    @property
    def title(self) -> str:
        """Заголовок (всплывающая подсказка)"""
        return self._title.value

    @title.setter
    def title(self, value: str):
        self._title.value = str(value)

    @property
    def hidden(self) -> bool:
        """Скрыт ли объект?"""
        return self._hidden.value

    @hidden.setter
    def hidden(self, value: bool):
        self._hidden.value = (
            ObjectHidden.Options.hidden if value else (ObjectHidden.Options.visible)
        )

    @property
    def tag(self) -> str:
        return "pic:cNvPr"


class CNvPicPr(BaseContainerTag):
    """
    Non-Visual Picture Properties
    Специфические свойства для изображений
    """

    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:cNvPicPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": PicLocks}, {"class": ExtLst}]


class PicLocks(BaseContentTag):
    __slots__ = (
        "_no_change_aspect",
        "_no_change_arrowheads",
        "_no_change_start",
        "_no_change_end",
        "_no_edit_points",
        "_no_adjust_handles",
        "_no_change_shape_type",
        "_no_move",
        "_no_resize",
        "_no_rotate",
        "_no_select",
        "_no_crop",
        "_no_change_bullet",
        "_no_grp",
        "_no_ungrp",
        "_no_drill_down",
        "_no_text_edit",
        "_xmlns",
    )

    def __init__(self):
        """Блокировка изменения пропорций (1 = да, 0 = нет)"""

        self._no_change_aspect = NoChangeAspect(NoChangeAspect.Options.access)
        self._no_change_arrowheads = NoChangeArrowheads(
            NoChangeArrowheads.Options.access
        )
        self._no_change_start = NoChangeStart(NoChangeStart.Options.access)
        self._no_change_end = NoChangeEnd(NoChangeEnd.Options.access)
        self._no_edit_points = NoEditPoints(NoEditPoints.Options.access)
        self._no_adjust_handles = NoAdjustHandles(NoAdjustHandles.Options.access)
        self._no_change_shape_type = NoChangeShapeType(NoChangeShapeType.Options.access)
        self._no_move = NoMove(NoMove.Options.access)
        self._no_resize = NoResize(NoResize.Options.access)
        self._no_rotate = NoRotate(NoRotate.Options.access)
        self._no_select = NoSelect(NoSelect.Options.access)
        self._no_crop = NoCrop(NoCrop.Options.access)
        self._no_change_bullet = NoChangeBullet(NoChangeBullet.Options.access)
        self._no_grp = NoGrp(NoGrp.Options.access)
        self._no_ungrp = NoUngrp(NoUngrp.Options.access)
        self._no_drill_down = NoDrilldown(NoDrilldown.Options.access)
        self._no_text_edit = NoTextEdit(NoTextEdit.Options.access)
        self._xmlns = GraphicFrameLocksNS("")

    @property
    def no_change_aspect(self):
        return self._no_change_aspect.value

    @no_change_aspect.setter
    def no_change_aspect(self, value: bool):
        self._no_change_aspect.value = (
            NoChangeAspect.Options.restrict
            if value
            else (NoChangeAspect.Options.access)
        )

    @property
    def no_change_arrowheads(self):
        return self._no_change_arrowheads.value

    @no_change_arrowheads.setter
    def no_change_arrowheads(self, value: bool):
        self._no_change_arrowheads.value = (
            NoChangeArrowheads.Options.restrict
            if value
            else NoChangeArrowheads.Options.access
        )

    @property
    def no_change_start(self):
        """Блокировка изменения начальной точки"""
        return self._no_change_start.value

    @no_change_start.setter
    def no_change_start(self, value: bool):
        self._no_change_start.value = (
            NoChangeStart.Options.restrict if value else (NoChangeStart.Options.access)
        )

    @property
    def no_change_end(self):
        """Блокировка изменения конечной точки"""
        return self._no_change_end.value

    @no_change_end.setter
    def no_change_end(self, value: bool):
        self._no_change_end.value = (
            NoChangeEnd.Options.restrict if value else (NoChangeEnd.Options.access)
        )

    @property
    def no_edit_points(self):
        """Запрет редактирования точек"""
        return self._no_edit_points.value

    @no_edit_points.setter
    def no_edit_points(self, value: bool):
        self._no_edit_points.value = (
            NoEditPoints.Options.restrict if value else (NoEditPoints.Options.access)
        )

    @property
    def no_adjust_handles(self):
        """Запрет изменения ручек настройки"""
        return self._no_adjust_handles

    @no_adjust_handles.setter
    def no_adjust_handles(self, value: bool):
        self._no_adjust_handles.value = (
            NoAdjustHandles.Options.restrict
            if value
            else (NoAdjustHandles.Options.access)
        )

    @property
    def no_change_shape_type(self):
        """Запрет изменения типа фигуры"""
        return self._no_change_shape_type.value

    @no_change_shape_type.setter
    def no_change_shape_type(self, value: bool):
        self._no_change_shape_type.value = (
            NoChangeShapeType.Options.restrict
            if value
            else NoChangeShapeType.Options.access
        )

    @property
    def no_move(self):
        """Запрет перемещения"""
        return self._no_move.value

    @no_move.setter
    def no_move(self, value: bool):
        self._no_move.value = (
            NoMove.Options.restrict if value else (NoMove.Options.access)
        )

    @property
    def no_resize(self):
        """Запрет изменения размера"""
        return self._no_resize.value

    @no_resize.setter
    def no_resize(self, value: bool):
        self._no_resize.value = (
            NoResize.Options.restrict if value else (NoResize.Options.access)
        )

    @property
    def no_rotate(self):
        """Запрет вращения"""
        return self._no_rotate.value

    @no_rotate.setter
    def no_rotate(self, value: bool):
        self._no_rotate.value = (
            NoRotate.Options.restrict if value else (NoRotate.Options.access)
        )

    @property
    def no_select(self):
        """Запрет выделения"""
        return self._no_select.value

    @no_select.setter
    def no_select(self, value: bool):
        self._no_select.value = (
            NoSelect.Options.restrict if value else (NoSelect.Options.access)
        )

    @property
    def no_crop(self):
        """Запрет обрезки"""
        return self._no_crop.value

    @no_crop.setter
    def no_crop(self, value: bool):
        self._no_crop.value = (
            NoCrop.Options.restrict if value else (NoCrop.Options.access)
        )

    @property
    def no_change_bullet(self):
        """Запрет обрезки"""
        return self._no_change_bullet.value

    @no_change_bullet.setter
    def no_change_bullet(self, value: bool):
        self._no_change_bullet.value = (
            NoChangeBullet.Options.restrict if value else NoChangeBullet.Options.access
        )

    @property
    def no_grp(self):
        """Запрет обрезки"""
        return self._no_grp.value

    @no_grp.setter
    def no_grp(self, value: bool):
        self._no_grp.value = NoGrp.Options.restrict if value else NoGrp.Options.access

    @property
    def no_ungrp(self):
        """Запрет обрезки"""
        return self._no_ungrp.value

    @no_ungrp.setter
    def no_ungrp(self, value: bool):
        self._no_ungrp.value = (
            NoUngrp.Options.restrict if value else (NoUngrp.Options.access)
        )

    @property
    def no_drill_down(self):
        """Запрет обрезки"""
        return self._no_drill_down.value

    @no_drill_down.setter
    def no_drill_down(self, value: bool):
        self._no_drill_down.value = (
            NoDrilldown.Options.restrict if value else (NoDrilldown.Options.access)
        )

    @property
    def no_text_edit(self):
        """Запрет обрезки"""
        return self._no_text_edit.value

    @no_text_edit.setter
    def no_text_edit(self, value: bool):
        self._no_text_edit.value = (
            NoTextEdit.Options.restrict if value else (NoTextEdit.Options.access)
        )

    @property
    def xmlns(self):
        """Запрет обрезки"""
        return self._xmlns.value

    @xmlns.setter
    def xmlns(self, value: str):
        self._xmlns.value = value

    @property
    def tag(self) -> str:
        return "a:picLocks"


class NvPicPr(BaseContainerTag):
    """
    Non-Visual Picture Properties
    Свойства изображения, не влияющие на отображение
    """

    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:nvPicPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": CNvPr}, {"class": CNvPicPr}]


class BlipFill(BaseContainerTag):
    """pic:blipFill"""

    __slots__ = ("_dpi",)

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._dpi = Dpi("0")  # По умолчанию 0

    @property
    def dpi(self) -> str:
        """DPI для fillRect (0 = использовать системный DPI)"""
        return str(self._dpi.value)

    @dpi.setter
    def dpi(self, value: int):
        self._dpi.value = str(value)

    @property
    def tag(self):
        return "pic:blipFill"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": Blip}, {"class": SrcRect}, {"class": Stretch}]


class Blip(BaseContainerTag):
    """a:blip - ссылка на изображение с эффектами"""

    __slots__ = (
        "_objects",
        "_property",
        "_embed",
        "_cstate",
        "_alpha_mod",
        "_alpha_mod_fix",
        "_gain",
        "_black_level",
        "_gamma",
        "_gray",
        "_red",
        "_green",
        "_blue",
        "_red_mod",
        "_green_mod",
        "_blue_mod",
        "_hue",
        "_hue_mod",
        "_lum",
        "_lum_mod",
        "_sat",
        "_sat_mod",
        "_shade",
        "_cont",
        "_cont_mod",
        "_sharp",
        "_tint",
        "_bu_clr",
        "_bu_clr_tx",
    )

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

        self._embed = Embed("")
        self._cstate = CState("print")
        self._alpha_mod = AlphaMod("100000")
        self._alpha_mod_fix = AlphaModFix("")
        self._gain = Gain("0")
        self._black_level = BlackLevel("0")
        self._gamma = Gamma("0")
        self._gray = Gray("0")
        self._red = Red("0")
        self._green = Green("0")
        self._blue = Blue("0")
        self._red_mod = RedMod("100000")
        self._green_mod = GreenMod("100000")
        self._blue_mod = BlueMod("100000")
        self._hue = Hue("0")
        self._hue_mod = HueMod("100000")
        self._lum = Lum("0")
        self._lum_mod = LumMod("100000")
        self._sat = Sat("0")
        self._sat_mod = SatMod("100000")
        self._shade = Shade("0")
        self._cont = Cont("0")
        self._cont_mod = ContMod("100000")
        self._sharp = Sharp("0")
        self._tint = Tint("0")
        self._bu_clr = BuClr("")
        self._bu_clr_tx = BuClrTx("")

    # ========== ОСНОВНЫЕ АТРИБУТЫ ==========

    @property
    def embed(self) -> str:
        return self._embed.value

    @embed.setter
    def embed(self, value: str):
        self._embed.value = str(value)

    @property
    def cstate(self) -> str:
        return self._cstate.value

    @cstate.setter
    def cstate(self, value: str):
        self._cstate.value = value

    # ========== ПРОЗРАЧНОСТЬ ==========

    @property
    def alpha_mod(self) -> str:
        return str(self._alpha_mod.value)

    @alpha_mod.setter
    def alpha_mod(self, value: int):
        self._alpha_mod.value = str(value)

    @property
    def alpha_mod_fix(self) -> str:
        return str(self._alpha_mod_fix.value) if self._alpha_mod_fix.value else ""

    @alpha_mod_fix.setter
    def alpha_mod_fix(self, value: int):
        if value is None:
            self._alpha_mod_fix.value = ""
        else:
            self._alpha_mod_fix.value = str(value)

    # ========== ЯРКОСТЬ И КОНТРАСТ ==========

    @property
    def gain(self) -> str:
        return str(self._gain.value)

    @gain.setter
    def gain(self, value: int):
        self._gain.value = str(value)

    @property
    def black_level(self) -> str:
        return str(self._black_level.value)

    @black_level.setter
    def black_level(self, value: int):
        self._black_level.value = str(value)

    @property
    def gamma(self) -> str:
        return str(self._gamma.value)

    @gamma.setter
    def gamma(self, value: int):
        self._gamma.value = str(value)

    @property
    def gray(self) -> str:
        return str(self._gray.value)

    @gray.setter
    def gray(self, value: int):
        self._gray.value = str(value)

    # ========== ОСНОВНЫЕ ЦВЕТА ==========

    @property
    def red(self) -> int:
        return int(self._red.value)

    @red.setter
    def red(self, value: int):
        self._red.value = str(value)

    @property
    def green(self) -> int:
        return int(self._green.value)

    @green.setter
    def green(self, value: int):
        self._green.value = str(value)

    @property
    def blue(self) -> int:
        return int(self._blue.value)

    @blue.setter
    def blue(self, value: int):
        self._blue.value = str(value)

    # ========== МОДИФИКАТОРЫ ЦВЕТОВ ==========

    @property
    def red_mod(self) -> str:
        return str(self._red_mod.value)

    @red_mod.setter
    def red_mod(self, value: int):
        self._red_mod.value = str(value)

    @property
    def green_mod(self) -> str:
        return str(self._green_mod.value)

    @green_mod.setter
    def green_mod(self, value: int):
        self._green_mod.value = str(value)

    @property
    def blue_mod(self) -> str:
        return str(self._blue_mod.value)

    @blue_mod.setter
    def blue_mod(self, value: int):
        self._blue_mod.value = str(value)

    # ========== HSL ==========

    @property
    def hue(self) -> str:
        return str(self._hue.value)

    @hue.setter
    def hue(self, value: int):
        self._hue.value = str(value)

    @property
    def hue_mod(self) -> str:
        return str(self._hue_mod.value)

    @hue_mod.setter
    def hue_mod(self, value: int):
        self._hue_mod.value = str(value)

    @property
    def sat(self) -> str:
        return str(self._sat.value)

    @sat.setter
    def sat(self, value: int):
        self._sat.value = str(value)

    @property
    def sat_mod(self) -> str:
        return str(self._sat_mod.value)

    @sat_mod.setter
    def sat_mod(self, value: int):
        self._sat_mod.value = str(value)

    @property
    def lum(self) -> str:
        return str(self._lum.value)

    @lum.setter
    def lum(self, value: int):
        self._lum.value = str(value)

    @property
    def lum_mod(self) -> str:
        return str(self._lum_mod.value)

    @lum_mod.setter
    def lum_mod(self, value: int):
        self._lum_mod.value = str(value)

    # ========== КОНТРАСТ И РЕЗКОСТЬ ==========

    @property
    def cont(self) -> str:
        return str(self._cont.value)

    @cont.setter
    def cont(self, value: int):
        self._cont.value = str(value)

    @property
    def cont_mod(self) -> str:
        return str(self._cont_mod.value)

    @cont_mod.setter
    def cont_mod(self, value: int):
        self._cont_mod.value = str(value)

    @property
    def sharp(self) -> str:
        return str(self._sharp.value)

    @sharp.setter
    def sharp(self, value: int):
        self._sharp.value = str(value)

    # ========== ДРУГИЕ ЭФФЕКТЫ ==========

    @property
    def shade(self) -> str:
        return str(self._shade.value)

    @shade.setter
    def shade(self, value: int):
        self._shade.value = str(value)

    @property
    def tint(self) -> str:
        return str(self._tint.value)

    @tint.setter
    def tint(self, value: int):
        self._tint.value = str(value)

    # ========== ЦВЕТА ЗАЛИВКИ ==========

    @property
    def bu_clr(self) -> str:
        return str(self._bu_clr.value)

    @bu_clr.setter
    def bu_clr(self, value: str):
        self._bu_clr.value = value

    @property
    def bu_clr_tx(self) -> str:
        return self._bu_clr_tx.value

    @bu_clr_tx.setter
    def bu_clr_tx(self, value: str):
        self._bu_clr_tx.value = value

    @property
    def tag(self):
        return "a:blip"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": ExtLst}]

    # ----- Удобные методы -----

    def set_transparency(self, percent: float):
        """Установить прозрачность в процентах (0-100)"""
        value = int(percent * 1000)  # 0-100000
        self._alpha_mod.value = str(value)

    def set_brightness(self, percent: float):
        """Установить яркость в процентах (-100..100)"""
        value = int(percent * 1000)  # -100000..100000
        self._lum.value = str(value)

    def set_contrast(self, percent: float):
        """Установить контрастность в процентах (-100..100)"""
        value = int(percent * 1000)
        self._cont.value = str(value)

    def enable_grayscale(self):
        """Включить оттенки серого"""
        self._gray.value = "1"

    def disable_grayscale(self):
        """Выключить оттенки серого"""
        self._gray.value = "0"


class ExtLst(BaseContainerTag):
    """a:extLst - список расширений для элементов Office Open XML"""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:extLst"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": Ext}]


class Ext(BaseContainerTag):
    """a:ext - отдельное расширение с уникальным URI"""

    __slots__ = ("_uri",)

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._uri = URIExt("")

    @property
    def uri(self) -> str:
        return self._uri.value

    @uri.setter
    def uri(self, value: str):
        self._uri.value = value

    @property
    def tag(self):
        return "a:ext"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": UseLocalDpi}]


class UseLocalDpi(BaseContentTag):
    """a14:useLocalDpi - использовать локальный DPI (Office 2010+)"""

    __slots__ = ("_dpi", "_xmlns")

    def __init__(self):
        self._dpi = UseLocalDpiVal(UseLocalDpiVal.Options.use_system)
        self._xmlns = UseLocalDpiNS("")

    @property
    def dpi(self):
        """Значение атрибута val"""
        return self._dpi.value

    @dpi.setter
    def dpi(self, value: bool):
        self._dpi.value = (
            UseLocalDpiVal.Options.use_local
            if value
            else (UseLocalDpiVal.Options.use_system)
        )

    @property
    def xmlns(self):
        return self._xmlns.value

    @xmlns.setter
    def xmlns(self, value: str):
        self._xmlns.value = value

    @property
    def tag(self) -> str:
        return "a14:useLocalDpi"


class SrcRect(BaseContentTag):
    """a:srcRect - область обрезки изображения"""

    __slots__ = ("_left", "_top", "_right", "_bottom")

    def __init__(self):
        self._left = EffectLeft("0")
        self._top = EffectTop("0")
        self._right = EffectRight("0")
        self._bottom = EffectBottom("0")

    @property
    def left(self):
        return int(self._left.value)

    @left.setter
    def left(self, value: int):
        self._left.value = str(max(0, min(1000, value)))

    @property
    def top(self):
        return str(self._top.value)

    @top.setter
    def top(self, value: int):
        self._top.value = str(max(0, min(1000, value)))

    @property
    def right(self):
        return str(self._right.value)

    @right.setter
    def right(self, value: int):
        self._right.value = str(max(0, min(1000, value)))

    @property
    def bottom(self):
        return str(self._bottom.value)

    @bottom.setter
    def bottom(self, value: int):
        self._bottom.value = str(max(0, min(1000, value)))

    @property
    def tag(self):
        return "a:srcRect"


class Stretch(BaseContainerTag):
    """a:stretch - растяжение изображения"""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:stretch"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": FillRect}]


class FillRect(BaseContentTag):
    """a:fillRect - прямоугольник заливки"""

    __slots__ = ()

    @property
    def tag(self) -> str:
        return "a:fillRect"


class SpPr(BaseContainerTag):
    """pic:spPr - свойства фигуры (обводка, заливка, эффекты)"""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._bwMode = BwMode("auto")

    @property
    def bwMode(self):
        return self._bwMode.value

    @bwMode.setter
    def bwMode(self, value: str):
        self._bwMode.value = value

    @property
    def tag(self):
        return "pic:spPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": Xfrm},
            {"class": PrstGeom},
            {"class": NoFill},
            {"class": BlipFill},
            {"class": Ln},
            {"class": ExtLst},
        ]


class Xfrm(BaseContainerTag):
    """a:xfrm - трансформации фигуры (позиция, размер, вращение)"""

    __slots__ = ("_off_x", "_off_y", "_ext_cx", "_ext_cy", "_rot", "_flip_h", "_flip_v")

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._off_x = OffX("0")
        self._off_y = OffY("0")

        self._ext_cx = ExtCx("0")
        self._ext_cy = ExtCy("0")

        self._rot = Rot("")
        self._flip_h = FlipH(FlipH.Options.no_flip)
        self._flip_v = FlipV(FlipV.Options.no_flip)

    @property
    def off_x(self) -> str:
        """Позиция X (в EMU)"""
        return str(self._off_x.value)

    @off_x.setter
    def off_x(self, value: int):
        self._off_x.value = str(value)

    @property
    def off_y(self) -> str:
        """Позиция Y (в EMU)"""
        return str(self._off_y.value)

    @off_y.setter
    def off_y(self, value: int):
        self._off_y.value = str(value)

    @property
    def ext_cx(self) -> str:
        """Ширина (в EMU)"""
        return str(self._ext_cx.value)

    @ext_cx.setter
    def ext_cx(self, value: int):
        self._ext_cx.value = str(value)

    @property
    def ext_cy(self) -> str:
        """Высота (в EMU)"""
        return str(self._ext_cy.value)

    @ext_cy.setter
    def ext_cy(self, value: int):
        self._ext_cy.value = str(value)

    @property
    def rot(self) -> str:
        """Угол вращения (в 60000-х долях градуса)"""
        return str(self._rot.value)

    @rot.setter
    def rot(self, value: int):
        self._rot.value = str(value)

    @property
    def flip_h(self) -> str:
        """Отражение по горизонтали"""
        return str(self._flip_h.value)

    @flip_h.setter
    def flip_h(self, value: bool):
        self._flip_h.value = "1" if value else "0"

    @property
    def flip_v(self) -> str:
        """Отражение по вертикали"""
        return str(self._flip_v.value)

    @flip_v.setter
    def flip_v(self, value: bool):
        self._flip_v.value = "1" if value else "0"

    @property
    def tag(self):
        return "a:xfrm"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": Off}, {"class": Ext}]


class Off(BaseContentTag):
    """Позиция X для элемента off"""

    __slots__ = ("_x", "_y")

    def __init__(self):
        self._x = X("0")
        self._y = Y("0")

    @property
    def x(self) -> str:
        """Позиция X в EMU"""
        return str(self._x.value)

    @x.setter
    def x(self, value: int):
        self._x.value = str(value)

    @property
    def y(self) -> str:
        """Позиция Y в EMU"""
        return str(self._y.value)

    @y.setter
    def y(self, value: int):
        self._y.value = str(value)

    def set_position(self, x: int, y: int):
        """Установить позицию"""
        self.x = x
        self.y = y

    def get_position(self) -> tuple[int, int]:
        """Получить позицию"""
        return (int(self.x), int(self.y))

    @property
    def tag(self) -> str:
        return "a:off"


class PrstGeom(BaseContainerTag):
    """a:prstGeom - предустановленная геометрическая форма"""

    __slots__ = ("_prst",)

    def __init__(self, objects: Objects | list = None, prst: str = "rect"):
        super().__init__(objects)

        self._prst = Prst(prst)

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": AvLst},
        ]

    @property
    def prst(self) -> str:
        """Тип предустановленной формы"""
        return self._prst.value

    @prst.setter
    def prst(self, value: str):
        self._prst.value = value

    @property
    def tag(self):
        return "a:prstGeom"


class AvLst(BaseContentTag):
    """a:avLst - список регулировок для предустановленных форм"""

    __slots__ = ()

    @property
    def tag(self) -> str:
        return "a:avLst"


class NoFill(BaseContentTag):
    """a:noFill - отсутствие заливки фигуры"""

    __slots__ = ()

    @property
    def tag(self) -> str:
        return "a:noFill"


class Ln(BaseContainerTag):
    """a:ln - обводка (контур) фигуры"""

    __slots__ = ("_width", "_cap", "_cmpd", "_align")

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._width = LineWidth("9525")
        self._cap = LineCap("flat")
        self._cmpd = LineCmpd("sng")
        self._align = LineAlign("ctr")

    @property
    def width(self) -> str:
        """Ширина линии в EMU (1 pt = 9525 EMU)"""
        return str(self._width.value)

    @width.setter
    def width(self, value: int):
        self._width.value = str(value)

    @property
    def cap(self) -> str:
        """Тип окончания линии: flat, round, square"""
        return self._cap.value

    @cap.setter
    def cap(self, value: str):
        self._cap.value = value

    @property
    def cmpd(self) -> str:
        """Составная линия: sng, dbl, thickThin, thinThick, tri"""
        return self._cmpd.value

    @cmpd.setter
    def cmpd(self, value: str):
        self._cmpd.value = value

    @property
    def align(self) -> str:
        """Выравнивание: ctr, in, out"""
        return self._align.value

    @align.setter
    def align(self, value: str):
        self._align.value = value

    @property
    def tag(self):
        return "a:ln"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": NoFill},
            {"class": ExtLst},
        ]


class Inline(BaseContainerTag):
    _slots__ = ("_objects", "_property", "_distT", "_distB", "_distL", "_distR", "_")

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._distT = DistTop("0")
        self._distB = DistBottom("0")
        self._distL = DistLeft("0")
        self._distR = DistRight("0")
        self._anchorId = AnchorId(self.generate_random_id())
        self._editId = EditId(self.generate_random_id())

    @property
    def dist_top(self):
        return self._distT.value

    @dist_top.setter
    def dist_top(self, value):
        """take value in centimeters"""

        self._distT.value = value

    @property
    def dist_bottom(self):
        return self._distB.value

    @dist_bottom.setter
    def dist_bottom(self, value):
        """take value in centimeters"""

        self._distB.value = value

    @property
    def dist_left(self):
        return self._distL.value

    @dist_left.setter
    def dist_left(self, value):
        """take value in centimeters"""

        self._distL.value = value

    @property
    def dist_right(self):
        return self._distR.value

    @dist_right.setter
    def dist_right(self, value):
        """take value in centimeters"""

        self._distR.value = value

    @property
    def anchor_id(self):
        """wp14:anchorId"""
        return self._anchorId.value

    @anchor_id.setter
    def anchor_id(self, value):
        self._anchorId.value = value

    @property
    def edit_id(self):
        """wp14:editId"""

        return self._editId.value

    @edit_id.setter
    def edit_id(self, value):
        self._editId.value = value

    def set_distances(self, top=0, bottom=0, left=0, right=0):
        """Установить все отступы одновременно"""

        self.dist_top = top
        self.dist_bottom = bottom
        self.dist_left = left
        self.dist_right = right

    def set_all_distances(self, value):
        """Установить одинаковые отступы со всех сторон"""

        self.dist_top = value
        self.dist_bottom = value
        self.dist_left = value
        self.dist_right = value

    @staticmethod
    def generate_random_id():
        """Сгенерировать случайный Id"""

        return uuid.uuid4().hex[:8].upper()

    @property
    def tag(self):
        return "wp:inline"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": Extent},
            {"class": EffectExtent},
            {"class": DocProperties},
            {"class": CNvGraphicFramePr},
            {"class": Graphic},
        ]


class Drawing(BaseContainerTag):
    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "w:drawing"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return [
            {"class": Inline},
        ]
