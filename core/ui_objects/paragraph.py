from typing import List

from core.ui_objects.base import (
    BaseContainerDocx,
    BaseNonContainerDocx
)
from core.oxml_magic.parser import OxmlElement


class Paragraph(BaseContainerDocx):

    #todo нет проверки на отсутсвие текста, поэтому может создать ненужные ran и text
    def __init__(self):

        self.linked_objects = []

    @property
    def tag(self):
        return "w:p"

class Run(BaseContainerDocx):
    def __init__(self):
        self.linked_objects = []

    @property
    def tag(self):
        return "w:r"


class Text(BaseNonContainerDocx):
    def __init__(self):
        pass

    @property
    def tag(self):
        return "w:t"

