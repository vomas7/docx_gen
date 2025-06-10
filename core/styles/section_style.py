from docx.enum.section import WD_ORIENTATION, WD_SECTION_START
from docx.shared import Length
from dataclasses import dataclass
from core.styles.base import BaseStyle
from typing import Optional


@dataclass
class PgMar:
    w_left: Optional[Length] = None
    w_top: Optional[Length] = None
    w_right: Optional[Length] = None
    w_bottom: Optional[Length] = None
    w_header: Optional[Length] = None
    w_footer: Optional[Length] = None
    w_gutter: Optional[Length] = None


@dataclass
class TitlePg:
    w_titlePg: bool = True


@dataclass
class PageSz:
    w_w: Optional[Length] = None
    w_h: Optional[Length] = None
    w_orient: Optional[WD_ORIENTATION] = WD_ORIENTATION.PORTRAIT


@dataclass
class SectType:
    w_type: WD_SECTION_START = None


class SectionStyle(BaseStyle):

    def __init__(self, **kwargs):
        self.pgMar = PgMar()
        self.pgSz = PageSz()
        self.titlePg = TitlePg()
        self.scType = SectType()
        self.pgMar.w_left = kwargs.get('left_margin')

    @property
    def left_margin(self):
        return self.pgMar.w_left

    @left_margin.setter
    def left_margin(self, value: Length):
        self.pgMar.w_left = value

    @property
    def bottom_margin(self) -> Length | None:
        return self.pgMar.w_bottom

    @bottom_margin.setter
    def bottom_margin(self, value: int | Length | None):
        self.pgMar.w_bottom = value

    @property
    def different_first_page_header_footer(self) -> bool:
        return self.titlePg.w_titlePg

    @different_first_page_header_footer.setter
    def different_first_page_header_footer(self, value: bool):
        self.titlePg.w_titlePg = value

    @property
    def footer_distance(self) -> Length | None:
        return self.pgMar.w_footer

    @footer_distance.setter
    def footer_distance(self, value: int | Length | None):
        self.pgMar.w_footer = value

    @property
    def gutter(self) -> Length | None:
        return self.pgMar.w_gutter

    @gutter.setter
    def gutter(self, value: int | Length | None):
        self.pgMar.w_gutter = value

    @property
    def header_distance(self) -> Length | None:
        return self.pgMar.w_header

    @header_distance.setter
    def header_distance(self, value: int | Length | None):
        self.pgMar.w_header = value

    @property
    def orientation(self) -> WD_ORIENTATION:
        return self.pgSz.w_orient

    @orientation.setter
    def orientation(self, value: WD_ORIENTATION | None):
        self.pgSz.w_orient = value

    @property
    def page_height(self) -> Length | None:
        return self.pgSz.w_h

    @page_height.setter
    def page_height(self, value: Length | None):
        self.pgSz.w_h = value

    @property
    def page_width(self) -> Length | None:
        return self.pgSz.w_w

    @page_width.setter
    def page_width(self, value: Length | None):
        self.pgSz.w_w = value

    @property
    def right_margin(self) -> Length | None:
        return self.pgMar.w_right

    @right_margin.setter
    def right_margin(self, value: Length | None):
        self.pgMar.w_right = value

    @property
    def start_type(self) -> WD_SECTION_START:
        return self.scType.w_type

    @start_type.setter
    def start_type(self, value: WD_SECTION_START | None):
        self.scType.w_type = value

    @property
    def top_margin(self) -> Length | None:
        return self.pgMar.w_top

    @top_margin.setter
    def top_margin(self, value: Length | None):
        self.pgMar.w_top = value
