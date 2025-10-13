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
from core.doc_objects.base import BaseContainerDOC
from typing import Union


class Text(BaseContainerDOC):
    """
        A class representing formatted text in a document.
    """

    # todo Нужно реализоать свои объекты
    CONTAIN_TYPES = Union[CT_Text, CT_Br, CT_TabStop]

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
        super().__init__()
        self.validate_annotation(elem=elem, linked_objects=linked_objects)
        self._element = self.__convert_to_element(elem)
        self._linked_objects = linked_objects or []

        self._linked_objects.extend(self.__grab_children(self._element))
        # todo унифицировать обработку детей элемента и наполнение linked_objects

    def __convert_to_element(self, elem):
        """converts and validates with inserting to self._linked_objects"""

        elem = elem or self.__create_run()
        if isinstance(elem, Run):
            elem = elem._r
        elif isinstance(elem, (str, UserString)):
            elem = self.__create_run(elem)
        return elem

    @staticmethod
    def __create_run(text: str = "") -> CT_R:
        _r = cast('CT_R', OxmlElement('w:r'))
        _rPr = _r.get_or_add_rPr()
        _lang = OxmlElement('w:lang')
        _lang.set(qn("w:val"), LangTag.ru)
        _rPr.append(_lang)
        _r.append(_rPr)
        _r.text = text
        return _r

    @staticmethod
    def __grab_children(_r_elem: CT_R) -> list[BaseOxmlElement]:
        lst_children = _r_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_RPr)]

    def add_style(self, dc_style: TextStyle):
        set_style(self._element, dc_style)

    def __str__(self):
        return "<DOC.TEXT object>"

    def __repr__(self):
        return self.__str__()
