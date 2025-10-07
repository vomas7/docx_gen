from docx.oxml import parse_xml
from docx.section import Section
from typing import overload, cast
from docx.oxml.section import CT_SectPr
from core.constant import SECTION_STANDARD
from core.styles.stylist import set_style
from core.styles.section import SectionStyle
from core.doc_objects.base import BaseDOC
from typing import TYPE_CHECKING
from typing_extensions import TypeAlias
from typing import Union
from docx.oxml import OxmlElement, CT_P

from core.doc_objects.Paragraph import DOCParagraph

CONTAIN_TYPES = Union[DOCParagraph, None]


class DOCSection(BaseDOC):
    """
        Document section, providing access to section and page setup.
        Also provides access to headers and footers.
    """

    @overload
    def __init__(self, section: Section | CT_SectPr):
        ...

    @overload
    def __init__(self, section: Section | CT_SectPr, linked_objects: list):
        ...

    @overload
    def __init__(self):
        ...

    def __init__(self,
                 elem: Section | CT_SectPr | None = None,
                 linked_objects: list | None = None):

        BaseDOC.validate_annotation(self,
                                    elem=elem,
                                    linked_objects=linked_objects)

        BaseDOC.__init__(self)
        self._linked_objects = linked_objects or []

        self._element = self.__convert_to_element(elem)

    def __convert_to_element(self, elem):
        """convert element with validate"""
        elem = elem or self.__create_default_sect_pr()
        if isinstance(elem, Section):
            elem = elem._sectPr
        return elem

    def __create_default_sect_pr(self) -> CT_SectPr:
        """Creates standard section settings"""
        sect_pr = parse_xml(SECTION_STANDARD)
        return cast("CT_SectPr", sect_pr)

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

    def wrap_to_paragraph(self):
        if self._element.xpath("./w:pPr"):
            return
        _p: CT_P = OxmlElement('w:p')
        _p.set_sectPr(self._element)
        self._element = _p

    def __str__(self):
        return "<DOC.SECTION object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: SectionStyle):
        set_style(self._sectPr, dc_style)
