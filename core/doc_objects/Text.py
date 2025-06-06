from collections import UserString
from core.doc_objects.dataclasses import TextStyle
from docx.text.paragraph import Paragraph
from docx.text.run import Run
from typing import Union


class Text(UserString):
    def __init__(self, text: str, style: TextStyle=None):
        super().__init__(text)
        self._style = style
        self._iid = None

    def apply_style(self, text: Union[Paragraph | Run]):
        pass

    @property
    def text(self):
        return self.data
    
    @property
    def iid(self):
        return self._iid
    
    @iid.setter
    def iid(self, value: int):
        if not isinstance(value, int):
            raise ValueError("IID must be integer")
        self._iid = value

    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise AttributeError(f"value must be str not {type(value)}!")
        self.data = value

    def __str__(self):
        return str(self.data)


t = Text(text="hello")
