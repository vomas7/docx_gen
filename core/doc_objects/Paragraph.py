import random
from typing import overload, cast
from core.constant import PARAGRAPH_STANDARD
from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml, CT_P, CT_PPr, CT_R
from core.styles.stylist import set_style
from core.styles.paragraph import ParagraphStyle
from docx.oxml.xmlchemy import BaseOxmlElement
from core.doc_objects.base import BaseDOC
from typing_extensions import TypeAlias
from core.doc_objects.Text import Text

CONTAIN_TYPES: TypeAlias = "Text"  # todo также должен уметь хранить картинки


class DOCParagraph(BaseDOC):
    """
        Document paragraph
    """

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, elem: Paragraph | str | Text | CT_P):
        ...

    @overload
    def __init__(self,
                 elem: Paragraph | str | Text | CT_P,
                 linked_objects: list):
        ...

    def __init__(self,
                 elem: Paragraph | str | Text | CT_P | None = None,
                 linked_objects: list | None = None):

        BaseDOC.validate_annotation(
            self,
            elem=elem,
            linked_objects=linked_objects
        )
        BaseDOC.__init__(self)

        self._linked_objects = linked_objects or []

        self._element = self.__convert_to_element(elem)

    def __from_paragraph(self, elem: CT_P):
        for ch in self.__grab_children(elem):
            if isinstance(ch, CT_R):
                self.insert_linked_object(Text(ch))
            # todo elif isinstance(ch, CT_tbl) and etc.

    def __convert_to_element(self, elem):
        """converts and validates with inserting to self._linked_objects"""

        elem = elem or self.__create_default_paragraph()
        if isinstance(elem, (Paragraph, CT_P)):
            elem = elem._p if isinstance(elem, Paragraph) else elem
            self.__from_paragraph(elem)
            return elem

        elif isinstance(elem, (Text, str)):
            elem = Text(elem) if isinstance(elem, str) else elem
            self.insert_linked_object(elem)
            return elem

    def __grab_children(self, _p_elem: CT_P) -> list[BaseOxmlElement]:
        lst_children = _p_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_PPr)]

    def __create_default_paragraph(self) -> CT_P:
        """Creates standard paragraph settings"""
        default_paragraph = parse_xml(
            PARAGRAPH_STANDARD.format(
                random_paragraph_id=self.__gen_random_paragraph_id(8)
            )
        )
        return cast("CT_P", default_paragraph)

    def __gen_random_paragraph_id(cls, length: int = 8) -> str:
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

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

    def add_style(self, dc_style: ParagraphStyle):
        set_style(self._r, dc_style)

    def __str__(self):
        return "<DOC.PARAGRAPH object>"

    def __repr__(self):
        return self.__str__()
