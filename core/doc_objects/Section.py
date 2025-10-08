from typing import overload, cast, Union
from docx.oxml import parse_xml, OxmlElement, CT_SectPr, CT_P
from docx.section import Section
from core.constant import SECTION_STANDARD
from core.styles.stylist import set_style
from core.styles.section import SectionStyle
from core.doc_objects.base import BaseContainerDOC
from core.doc_objects.Paragraph import DOCParagraph


class DOCSection(BaseContainerDOC):
    """
        Document section, providing access to section and page setup.
        Also provides access to headers and footers.
    """

    CONTAIN_TYPES = Union[DOCParagraph, None]

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
        super().__init__()
        self.validate_annotation(elem=elem, linked_objects=linked_objects)
        self._linked_objects = linked_objects or []
        self._element = self.__convert_to_element(elem)

    def __convert_to_element(self, elem):
        """convert element with validate"""
        elem = elem or self.__create_default_sect_pr()
        if isinstance(elem, Section):
            elem = elem._sectPr
        return elem

    @staticmethod
    def __create_default_sect_pr() -> CT_SectPr:
        """Creates standard section settings"""
        sect_pr = parse_xml(SECTION_STANDARD)
        return cast("CT_SectPr", sect_pr)

    def wrap_to_paragraph(self):
        if self._element.xpath("./w:pPr"):
            return
        _p = cast("CT_P", OxmlElement('w:p'))
        _p.set_sectPr(self._element)
        self._element = _p

    def __str__(self):
        return "<DOC.SECTION object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: SectionStyle):
        set_style(self._element, dc_style)
