import random
from typing import overload, cast, Union
from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml, CT_P, CT_PPr, CT_R, OxmlElement, CT_Inline, CT_SectPr
from docx.oxml.xmlchemy import BaseOxmlElement
from core.constant import PARAGRAPH_STANDARD
from core.doc_objects.base import BaseContainerDOC
from core.doc_objects.Text import Text
from docx.text.run import Run


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

    @staticmethod
    def convert_to_linked_object(elem: BaseOxmlElement | str):
        """converts all possible cases for this object"""
        if isinstance(elem, Text):
            return elem
        elif isinstance(elem, (CT_R, str)):
            return Text(elem)
        elif isinstance(elem, CT_Inline):
            return None  # todo soon!
        return None

    def __convert_to_element(self, elem):
        """converts and validates with inserting to self._linked_objects"""

        elem = elem or self.__create_default_paragraph()
        if isinstance(elem, (Paragraph, CT_P)):
            elem = elem._p if isinstance(elem, Paragraph) else elem
            self.__from_paragraph(elem)

        elif isinstance(elem, (Text, str)):
            self.insert_linked_object(self.convert_to_linked_object(elem))
            elem = cast("CT_P", OxmlElement("w:p"))
        return elem

    def __from_paragraph(self, elem: CT_P):
        for ch in self.__grab_children(elem):
            self.insert_linked_object(self.convert_to_linked_object(ch))

    def __create_default_paragraph(self) -> CT_P:
        """Creates standard paragraph settings"""
        default_paragraph = parse_xml(
            PARAGRAPH_STANDARD.format(
                random_paragraph_id=self.__gen_random_paragraph_id(8)
            )
        )
        return cast("CT_P", default_paragraph)

    @staticmethod
    def __grab_children(_p_elem: CT_P) -> list[BaseOxmlElement]:
        # todo улучшить типы (сделать динамичесскую подставку) + во всём объекте + для других чуваков тоже
        return [ch for ch in _p_elem if isinstance(ch, (CT_R, CT_Inline, CT_SectPr))]

    @staticmethod
    def __gen_random_paragraph_id(length: int = 8) -> str:
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

    def __str__(self):
        return "<DOC.PARAGRAPH object>"

    def __repr__(self):
        return self.__str__()
