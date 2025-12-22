from core.ui_objects import LinkedObjects, BaseContainerTag
from typing import IO

class Body(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:body"

    @property
    def access_children(self):
        return {}


class Document(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:document"


    @property
    def access_children(self):
        return {Body}

    def open(self, file: str | IO[bytes]):
        from core.io.api import parse_document_part
        from core.oxml_magic.parser import convert_xml_to_cls

        setattr(self.__class__, "_part", parse_document_part(file))
        [_body] = self._part._element.getchildren()
        self.add(convert_xml_to_cls(_body))

    def save(self, filename: str):
        self._part.save(filename)
