from core.ui_objects.base.linked_objects import LinkedObjects
from core.ui_objects.base.base_container_tag import BaseContainerTag
from typing import IO
from core.oxml_magic.parser import make_xml_tree


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
    __slots__ = ("some", "_part")

    def __init__(self, linked_objects: LinkedObjects | list = None):
        self._part = None
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

        self._part = parse_document_part(file)
        [_body] = self._part._element.getchildren()
        self.add(convert_xml_to_cls(_body))

    def save(self, filename: str):
        self._part._element = make_xml_tree(self)
        self._part.save(filename)
