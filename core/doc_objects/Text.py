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


class Text(Run):
    """
        A class representing formatted text in a document.
    """

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, r_elem: str | UserString | Run):
        ...

    @overload
    def __init__(self, r_elem: str | UserString | Run,
                 linked_objects: list):
        ...

    def __init__(self,
                 r_elem: str | UserString | Run = None,
                 linked_objects: list = None):

        r_elem = r_elem or ""

        self._linked_objects = linked_objects or []

        if isinstance(r_elem, Run):
            super().__init__(r_elem._r, StoryPart.part)

        elif isinstance(r_elem, (str, UserString)):
            _r = self._create_run_pr(r_elem)
            super().__init__(_r, StoryPart.part)

        else:
            raise AttributeError(
                f"Creating Text object failed: Unknown source {type(r_elem)}!"
            )

    def _create_run_pr(self, text: str = "") -> CT_R:
        """
        создаём объект run и учитываем
        что он может создать несколько объектов за раз
        """

        _r = cast('CT_R', OxmlElement('w:r'))
        _rPr = _r.get_or_add_rPr()
        _lang = OxmlElement('w:lang')
        _lang.set(qn("w:val"), "ru-RU")
        _rPr.append(_lang)
        _r.append(_rPr)
        _r.text = text
        self._linked_objects.extend(self._grab_objects(_r))
        return _r

    def _grab_objects(self, _r_elem: CT_R) -> list[BaseOxmlElement]:
        lst_children = _r_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_RPr)]

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
