from docx.oxml import parse_xml
from docx.section import Section
from typing import overload, cast
from docx.oxml.section import CT_SectPr
from core.constant import SECTION_STANDARD
from core.styles.stylist import set_style
from core.styles.section import SectionStyle
from core.doc_objects.base import BaseDOC



class DOCSection(BaseDOC, Section):
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
                 elem: Section | CT_SectPr = None,
                 linked_objects: list | None = None):


        BaseDOC.validate_annotation(self,
                                    elem=elem,
                                    linked_objects=linked_objects)

        self._linked_objects = linked_objects or []

        elem = elem or self._create_default_sect_pr()

        if isinstance(elem, Section):
            elem = elem._sectPr

        #todo не работает, как передать document part?
        Section.__init__(self, elem, self.part)


    @staticmethod
    def _create_default_sect_pr() -> CT_SectPr:
        """Creates standard section settings"""
        sect_pr = parse_xml(SECTION_STANDARD)
        return cast("CT_SectPr", sect_pr)

    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    def insert_linked_objects(self, new, index: int = -1):
        self._linked_objects.insert(index, new)

    def __str__(self):
        return "<DOC.SECTION object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: SectionStyle):
        set_style(self._sectPr, dc_style)
