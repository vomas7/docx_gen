from typing import cast
from typing import Union
from typing import overload
from collections import UserString

from docx.text.run import Run
from docx.oxml.text.run import CT_R
from docx.parts.story import StoryPart

from core.styles.text import TextStyle
from core.styles.stylist import set_style
from docx.oxml import CT_RPr, OxmlElement
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.oxml.ns import qn
from core.constant import LangTag


class Text(Run):
    """
        A class representing formatted text in a document.
    """

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, elem: str | UserString | Run | CT_R):
        ...

    @overload
    def __init__(self,
                 elem: str | UserString | Run | CT_R,
                 linked_objects: list):
        ...

    def __init__(self,
                 elem: str | UserString | Run | CT_R | None = None,
                 linked_objects: list | None = None):

        if not isinstance(elem, self.__init__.__annotations__["elem"]):
            raise AttributeError(
                f"Creating Text object failed: Unknown source {type(elem)}!"
            )

        elem = elem or self._create_run_pr()
        self._linked_objects = linked_objects or []

        if isinstance(elem, Run):
            elem = elem._r

        elif isinstance(elem, (str, UserString)):
            elem = self._create_run_pr(elem)

        super().__init__(elem, StoryPart.part)
        self._linked_objects.extend(self._grab_children(self._r))

    def _create_run_pr(self, text: str = "") -> CT_R:
        _r = cast('CT_R', OxmlElement('w:r'))
        _rPr = _r.get_or_add_rPr()
        _lang = OxmlElement('w:lang')
        _lang.set(qn("w:val"), LangTag.ru)
        _rPr.append(_lang)
        _r.append(_rPr)
        _r.text = text
        return _r

    def _grab_children(self, _r_elem: CT_R) -> list[BaseOxmlElement]:
        lst_children = _r_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_RPr)]

    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    def insert_linked_objects(self, new, index: int = -1):
        self._linked_objects.insert(index, new)

    def __str__(self):
        return "<DOC.TEXT object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: TextStyle):
        set_style(self._r, dc_style)
