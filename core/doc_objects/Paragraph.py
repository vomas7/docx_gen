import random
from typing import overload, cast
from typing import Optional, Union
from core.constant import PARAGRAPH_STANDARD
from docx.parts.story import StoryPart
from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml
from core.doc_objects.Text import Text
from core.styles.stylist import set_style
from core.styles.paragraph import ParagraphStyle


class DOCParagraph(Paragraph):
    """
        Document paragraph
    """

    @overload
    def __init__(self, paragraph: Paragraph): ...

    @overload
    def __init__(self, paragraph: Paragraph, linked_objects: list): ...

    @overload
    def __init__(self, text: Union[str, Text]): ...

    @overload
    def __init__(self): ...

    def __init__(self,
                 paragraph: Optional[Paragraph] = None,
                 linked_objects: Optional[list] = None,
                 text: Union[str, Text] = None):
        self.linked_objects = []
        if paragraph is None:
            xml = self._create_default_paragraph()
            super().__init__(xml, StoryPart.part)
            if text:
                self.add_run(text)
        else:
            linked_objects = None
            if isinstance(paragraph, Paragraph):
                super().__init__(paragraph._p)
                self._linked_objects = linked_objects
            else:
                raise AttributeError (f"Creating Paragraph object failed:"
                                      f"Unknown source {type(paragraph)}!")

    @staticmethod
    def _create_default_paragraph():
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

    @staticmethod
    def _gen_random_paragraph_id(length:int = 8) -> str:
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

    def __str__(self):
        return "<DOC.PARAGRAPH object>"
    
    def __repr__(self):
        return self.__str__()
    
    def add_style(self, dc_style: ParagraphStyle):
        set_style(self._r, dc_style)
