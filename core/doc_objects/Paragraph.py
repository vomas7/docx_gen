import random
from typing import overload
from typing import Optional
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
    def __init__(self): ...

    def __init__(self, paragraph: Optional[Paragraph] = None, linked_objects: Optional[list] = None):
        if paragraph is None:
            xml = self._create_default_p()
            super().__init__(xml, StoryPart.part)
        else:
            linked_objects = None
            if isinstance(paragraph, Paragraph):
                super().__init__(paragraph._p)
                self._linked_objects = linked_objects
            else:
                raise AttributeError (f"Creating Paragraph object failed:"
                                      f"Unknown source {type(paragraph)}!")
            
    def add_run(self, text: Text):
        return super().add_run(text)

    @staticmethod
    def _create_default_paragraph():
        """Creates standard paragraph settings"""
        default_paragraph = parse_xml(f"""
            <w:p 
                w14:paraId="{DOCParagraph._gen_random_paragraph_id(8)}" 
                w14:textId="{DOCParagraph._gen_random_paragraph_id(8)}" 
                w:rsidR="{DOCParagraph._gen_random_paragraph_id(8)}" 
                w:rsidRPr="{DOCParagraph._gen_random_paragraph_id(8)}" 
                w:rsidRDefault="{DOCParagraph._gen_random_paragraph_id(8)}" 
                w:rsidP="{DOCParagraph._gen_random_paragraph_id(8)}"
            >
                <w:r>
                    <w:t></w:t>
                </w:r>
            </w:p>
            """
        )
        return default_paragraph


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
