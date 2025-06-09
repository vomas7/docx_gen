from docx.shared import Length
from dataclasses import dataclass, field
from core.styles.base import BaseStyle
from typing import Optional


@dataclass
class PgMar:
    left: Optional[Length] = None
    top: Optional[Length] = None
    right: Optional[Length] = None
    bottom: Optional[Length] = None
    header: Optional[Length] = None
    footer: Optional[Length] = None
    gutter: Optional[Length] = None


@dataclass
class SectionStyle(BaseStyle):

    def __init__(self, **kwargs):
        self.pgMar = PgMar()
        self.pgMar.left = kwargs.get('left_margin')

    @property
    def left_margin(self):
        return self.pgMar.left

    @left_margin.setter
    def left_margin(self, left: Length):
        self.pgMar.left = left
