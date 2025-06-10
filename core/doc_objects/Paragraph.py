import random
from typing import overload

from docx.text.paragraph import Paragraph
from docx.oxml import parse_xml

from core.doc_objects.styles import ParagraphStyle


class DOCParagraph(Paragraph):
    """
        Document paragraph
    """

    @overload
    def __init__(self, paragraph: Paragraph):
        ...

    @overload
    def __init__(self, paragraph: Paragraph, style: ParagraphStyle):
        ...

    @overload
    def __init__(self, paragraph: Paragraph, linked_objects: list):
        ...

    @overload
    def __init__(self, paragraph: Paragraph, style: ParagraphStyle, linked_objects: list):
        ...

    @overload
    def __init__(self):
        ...

    def __init__(self, *args):
        if not args:
            from docx.parts.story import StoryPart
            def_p = self._create_default_paragraph()
            super().__init__(def_p, StoryPart.part)
        else:
            source = args[0]
            style = None
            linked_objects = None
            if len(args) == 2:
                if isinstance(args[1], list):
                    linked_objects = args[0]
                elif isinstance(args[1], ParagraphStyle):
                    style = args[1]
            elif len(args) == 3:
                linked_objects = args[0]
                style = args[1]
            if isinstance(source, Paragraph):
                super().__init__(source._p)
                self._linked_objects = linked_objects
                self._style = style
            else:
                raise AttributeError (f"Creating Paragraph object failed:"
                                      f"Unknown source {type(source)}!")


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
    def _gen_random_paragraph_id(length:int = 8):
        """Generate random id for attributes in paragraph"""
        return f"{random.getrandbits(32 * length):0{length}x}"

    def __str__(self):
        return "<DOC.PARAGRAPH object>"
    
    def __repr__(self):
        return self.__str__()
