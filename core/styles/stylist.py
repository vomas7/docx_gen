from abc import abstractmethod
from typing import TYPE_CHECKING
from dataclasses import asdict
from core.styles.base import BaseStyle


class Stylist:
    """Mixin class to provide methods of applying and retrieve style for object."""

    @classmethod
    @abstractmethod
    def style(cls, dc_style: BaseStyle):
        attrs_dict = asdict(dc_style)
        attr = list(attrs_dict.keys())[0]
        setattr(cls, attr, attrs_dict[attr])

