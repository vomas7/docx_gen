from docx.enum.section import WD_ORIENTATION, WD_SECTION_START
from docx.shared import Length
from docx.oxml.section import CT_PageMar, CT_PageSz, CT_OnOff, CT_SectType, CT_P
from core.styles.base import BaseStyle
from typing import Optional, Union


class SectionStyle(BaseStyle):
    _style_attrs = {
        "left_margin": ("_pgMar", "left"),
        "right_margin": ("_pgMar", "right"),
        "top_margin": ("_pgMar", "top"),
        "bottom_margin": ("_pgMar", "bottom"),
        "header_distance": ("_pgMar", "header"),
        "footer_distance": ("_pgMar", "footer"),
        "gutter": ("_pgMar", "gutter"),
        "page_width": ("_pgSz", "w"),
        "page_height": ("_pgSz", "h"),
        "orientation": ("_pgSz", "orient"),
        "different_first_page_header_footer": ("_titlePg", "val"),
        "start_type": ("_scType", "val")
    }

    left_margin: Optional[Union[Length, int]]
    right_margin: Optional[Union[Length, int]]
    top_margin: Optional[Union[Length, int]]
    bottom_margin: Optional[Union[Length, int]]
    header_distance: Optional[Union[Length, int]]
    footer_distance: Optional[Union[Length, int]]
    gutter: Optional[Union[Length, int]]
    page_width: Optional[Length]
    page_height: Optional[Length]
    orientation: Optional[WD_ORIENTATION]
    different_first_page_header_footer: bool
    start_type: Optional[WD_SECTION_START]

    NAMESPACE: str = 'w'

    def __init__(self, **kwargs):
        self._pgMar = CT_PageMar()
        self._pgSz = CT_PageSz()
        self._titlePg = CT_OnOff()
        self._scType = CT_SectType()

        super().__init__(**kwargs)


