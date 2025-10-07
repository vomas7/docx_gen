from typing import cast
from typing import overload
from collections import UserString

from docx.text.run import Run
from docx.oxml.text.run import CT_R

from core.styles.text import TextStyle
from core.styles.stylist import set_style
from docx.oxml import CT_RPr, OxmlElement, CT_Text, CT_Br, CT_TabStop
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.oxml.ns import qn
from core.constant import LangTag
from core.doc_objects.base import BaseDOC
from typing import Union

CONTAIN_TYPES = Union[CT_Text, CT_Br, CT_TabStop]  # todo Нужно реализоать свои объекты


class Text(BaseDOC):
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

        BaseDOC.validate_annotation(
            self,
            elem=elem,
            linked_objects=linked_objects
        )

        self._element = self.__convert_to_element(elem)

        self._linked_objects = linked_objects or []

        self._linked_objects.extend(self.__grab_children(self._element))

    def __convert_to_element(self, elem):
        """converts and validates with inserting to self._linked_objects"""

        elem = elem or self.__create_run_pr()
        if isinstance(elem, Run):
            elem = elem._r

        elif isinstance(elem, (str, UserString)):
            elem = self.__create_run_pr(elem)

        return elem

    def __create_run_pr(self, text: str = "") -> CT_R:
        _r = cast('CT_R', OxmlElement('w:r'))
        _rPr = _r.get_or_add_rPr()
        _lang = OxmlElement('w:lang')
        _lang.set(qn("w:val"), LangTag.ru)
        _rPr.append(_lang)
        _r.append(_rPr)
        _r.text = text
        return _r

    def __grab_children(self, _r_elem: CT_R) -> list[BaseOxmlElement]:
        lst_children = _r_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_RPr)]

    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    # todo это будет повторяться у элементов, которые хранят объекты


    def insert_linked_object(self, value: CONTAIN_TYPES, index: int = - 1):
        if not isinstance(value, CONTAIN_TYPES):
            raise TypeError(f"linked_objects must be a {CONTAIN_TYPES}")
        value.parent = self
        self._linked_objects.insert(index, value)

    def remove_linked_object(self, index: int = - 1):
        _elem = self._linked_objects.pop(index)
        _elem.parent = None
        return _elem

    def add_style(self, dc_style: TextStyle):
        set_style(self._r, dc_style)

    def __str__(self):
        return "<DOC.TEXT object>"

    def __repr__(self):
        return self.__str__()
