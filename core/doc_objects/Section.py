from docx.oxml import parse_xml
from docx.section import Section
from typing import overload, cast
from docx.oxml.section import CT_SectPr

from core.styles.stylist import set_style
from core.styles.section_style import SectionStyle


class DOCSection(Section):
    """
        Document section, providing access to section and page setup.
        Also provides access to headers and footers.
    """

    @overload
    def __init__(self, section: Section):
        ...

    @overload
    def __init__(self, section: Section, linked_objects: list):
        ...

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        self._linked_objects = []
        if not args:
            from docx.api import Document
            super().__init__(self._create_default_sect_pr(), Document().part)
        else:
            source = args[0]
            linked_objects = None
            if len(args) == 2:
                linked_objects = args[1]
            if isinstance(source, Section):
                super().__init__(source._sectPr, source._document_part)
                if linked_objects:
                    self._linked_objects = linked_objects
            else:
                raise AttributeError(f"Creating Section object failed:"
                                     f"Unknown source {type(source)}!")

    @staticmethod
    def _create_default_sect_pr() -> CT_SectPr:
        """Creates standard section settings"""
        sect_pr = parse_xml(
            '<w:sectPr xmlns:w="http://schemas.openxmlformats.org'
            '/wordprocessingml/2006/main">'
            '  <w:pgSz w:w="12240" w:h="15840"/>'  # A4 размер в twips (8.5×11 дюймов)
            '  <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
            '           w:header="720" w:footer="720" w:gutter="0"/>'
            '  <w:cols w:space="720"/>'
            '  <w:docGrid w:linePitch="360"/>'
            '</w:sectPr>'
        )
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
