import random
from typing import overload, cast, Union
from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml, CT_P, CT_PPr, CT_R, OxmlElement
from docx.oxml.xmlchemy import BaseOxmlElement
from core.constant import PARAGRAPH_STANDARD
from core.doc_objects.base import BaseContainerDOC
from core.doc_objects.Text import Text


class DOCParagraph(BaseContainerDOC):
    """
        Document paragraph
    """

    CONTAIN_TYPES = Union[Text]  # todo также должен уметь хранить картинки

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
        super().__init__()
        self.validate_annotation(elem=elem, linked_objects=linked_objects)
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

        elif isinstance(elem, (Text, str)):
            _text = Text(elem) if isinstance(elem, str) else elem
            self.insert_linked_object(_text)
            elem = cast("CT_P", OxmlElement("w:p"))
        return elem

    @staticmethod
    def __grab_children(_p_elem: CT_P) -> list[BaseOxmlElement]:
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

    @staticmethod
    def __gen_random_paragraph_id(length: int = 8) -> str:
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

    def __str__(self):
        return "<DOC.PARAGRAPH object>"

    def __repr__(self):
        return self.__str__()
