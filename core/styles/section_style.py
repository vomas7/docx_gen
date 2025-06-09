from dataclasses import dataclass
from core.styles.base import BaseStyle


@dataclass
class SectionStyle(BaseStyle):
    left_margin: float = None
