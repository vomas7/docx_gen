from typing import cast
from typing import Union
from typing import overload
from collections import UserString

from docx.text.run import Run
from docx.oxml import parse_xml
from docx.oxml.text.run import CT_R
from docx.parts.story import StoryPart

from core.styles.text import TextStyle
from core.styles.stylist import set_style


class Text(UserString, Run):
    """
        A class representing formatted text in a document.
    """

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, text: Union[str, UserString, Run]):
        ...

    @overload
    def __init__(self, text: Union[str, UserString, Run], linked_objects: list):
        ...

    def __init__(self, *args):
        if not args:
            xml = self._create_default_run_pr()
            Run().__init__(xml, StoryPart.part)
        else:
            source = args[0]
            linked_objects = None
            if len(args) == 2:
                linked_objects = args[1]
            if isinstance(source, Run):
                Run().__init__(source._r)
                self._linked_objects = linked_objects
            elif isinstance(source, str) or isinstance(source, UserString):
                xml = self._create_run_pr_with_text(source)
                Run().__init__(xml, StoryPart.part)
                self._linked_objects = linked_objects
            else:
                raise AttributeError(f"Creating Text object failed:"
                                     f"Unknown source {type(source)}!")

    def _create_run_pr_with_text(self, text: str) -> CT_R:
        r = parse_xml(
            '<w:r>'
            '<w:rPr>'
            '<w:lang w:val="ru-RU"/>'
            '</w:rPr>'
            f'<w:t xml:space="preserve">{text}</w:t>'
            '</w:r>'
        )
        return cast("CT_R", r)

    @staticmethod
    def _create_default_run_pr() -> CT_R:
        r = parse_xml(
            '<w:r>'
            '<w:rPr>'
            '<w:lang w:val="ru-RU"/>'
            '</w:rPr>'
            '<w:t xml:space="preserve"> </w:t>'
            '</w:r>'
        )
        return cast("CT_R", r)

    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    def __str__(self):
        return "<DOC.TEXT object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: TextStyle):
        set_style(self._r, dc_style)
