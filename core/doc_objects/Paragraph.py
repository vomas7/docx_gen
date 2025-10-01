import random
from typing import overload, cast
from typing import Optional, Union
from core.constant import PARAGRAPH_STANDARD
from docx.parts.story import StoryPart
from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml, CT_P, CT_PPr, CT_R
from core.doc_objects.Text import Text
from core.styles.stylist import set_style
from core.styles.paragraph import ParagraphStyle
from docx.oxml.xmlchemy import BaseOxmlElement


class DOCParagraph(Paragraph):
    """
        Document paragraph
    """

    @overload
    def __init__(self):
        ...

    @overload
    def __init__(self, elem: Paragraph | str | Text):
        ...

    @overload
    def __init__(self, elem: Paragraph | str | Text, linked_objects: list):
        ...

    def __init__(self,
                 elem: Paragraph | str | Text | None = None,
                 linked_objects: list | None = None):

        if not isinstance(elem, self.__init__.__annotations__["elem"]):
            raise AttributeError(
                f"Creating Paragraph object failed: "
                f"Unknown source {type(elem)}!"
            )

        self._linked_objects = linked_objects or []

        p = self._create_default_paragraph()

        if isinstance(elem, Paragraph):
            p = elem._p
            uniform_text = [Text(ch)
                            for ch in self._grab_children(p)
                            if isinstance(ch, CT_R)]
            self._linked_objects.extend(uniform_text)

        elif isinstance(elem, (Text, str)):
            uniform_text = Text(elem) if isinstance(elem, str) else elem
            self._linked_objects.append(uniform_text)
            p.append(uniform_text._r)

        super().__init__(p, StoryPart.part)

    def _grab_children(self, _p_elem: CT_P) -> list[BaseOxmlElement]:
        lst_children = _p_elem.getchildren()
        return [ch for ch in lst_children if not isinstance(ch, CT_PPr)]

    @staticmethod
    def _create_default_paragraph() -> CT_P:
        """Creates standard paragraph settings"""
        default_paragraph = parse_xml(
            PARAGRAPH_STANDARD.format(
                random_paragraph_id=DOCParagraph._gen_random_paragraph_id(8)
            )
        )
        return cast("CT_P", default_paragraph)

    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    def insert_linked_objects(self, new, index: int = -1):
        self._linked_objects.insert(index, new)

    @staticmethod
    def _gen_random_paragraph_id(length: int = 8) -> str:
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

    def __str__(self):
        return "<DOC.PARAGRAPH object>"

    def __repr__(self):
        return self.__str__()

    def add_style(self, dc_style: ParagraphStyle):
        set_style(self._r, dc_style)
