from core.ui_objects import LinkedObjects
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.run import Run, RunProperty


class ParagraphProperty(BaseContainerTag):
    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self) -> str:
        return "w:pPr"

    @property
    def access_children(self):
        return {RunProperty}


class Paragraph(BaseContainerTag):
    """Paragraph assignment <w:p>"""

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)
        self.paragraph_property = ParagraphProperty()

    @property
    def tag(self) -> str:
        return "w:p"

    @property
    def access_children(self):
        return {Run}

    def add_run(self, run: Run, index: int = -1):
        self.add(run, index)
