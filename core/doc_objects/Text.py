from typing import overload, Union, cast
from collections import UserString
from docx.oxml import parse_xml
from docx.text.run import Run

from core.styles.stylist import set_style
from core.styles.text import TextStyle


class Text(UserString, Run):

    @overload
    def __init__(self, text: Union [str| Run]):
        ...

    @overload
    def __init__(self, text: Union [str| Run], linked_objects: list):
        ...

    def _create_default_run_pr(self):
        r = parse_xml(
            '<w:r>'
                '<w:rPr>'
                    '<w:lang w:val="en-US"/>'
                '</w:rPr>'
                '<w:t> xml:space="preserve"> </w:t>'
            '</w:r>'
        )
        return cast()
        


    @property
    def linked_objects(self) -> list:
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, new: list):
        self._linked_objects = new

    def __str__(self):
        return "<DOC.TEXT object>"
    
    def __repr__(self):
        return self.__str__()
    
    def add_style(self, dc_style: TextStyle):
        set_style()


    # @property
    # def text(self):
    #     return self.data

    # @text.setter
    # def text(self, value: str):
    #     if not isinstance(value, str):
    #         raise AttributeError(f"value must be str not {type(value)}!")
    #     self.data = value


t = Text(text="hello")
