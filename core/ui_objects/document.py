from typing import IO

from core.ui_objects.atrib.ignorable import Ignorable
from core.ui_objects.table.table import Table
from core.utils.constants import DOC_DEFAULT_PATH
from core.writer.recording_tools import create_docx, docx_to_xml
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.linked_objects import Objects
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.section import Section


class Body(BaseContainerTag):
    __slots__ = ("some",)

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "w:body"

    @property
    def access_children(self):
        return [{"class": Section}, {"class": Paragraph}, {"class": Table}]

    @property
    def access_property(self) -> list[dict]:
        return list()


class Document(BaseContainerTag):
    __slots__ = ("_ignorable",)

    def __init__(self, path: str = None, objects: Objects | list = None):
        super().__init__(objects)
        if not path:
            path = DOC_DEFAULT_PATH
        self.open(path)
        self._ignorable = Ignorable("w14 wp14")

    @property
    def tag(self):
        return "w:document"

    @property
    def access_children(self):
        return [{"class": Body}]

    @property
    def access_property(self) -> list[dict]:
        return list()

    @property
    def ignorable(self):
        return self._ignorable.value

    @ignorable.setter
    def ignorable(self, value):
        self._ignorable.value = value

    def open(self, file: str | IO[bytes]):
        from core.oxml_magic.parser import parse_document

        self.add(parse_document(file))

    def save(self, file_path: str):
        create_docx(self, file_path)

    @property
    def body(self) -> Body:
        return self.objects[0]

    @property
    def sections(self) -> list[Section]:
        return list(filter(lambda x: isinstance(x, Section), self.body.objects))

    def get_section(self, index: int = -1) -> Section:
        return self.sections[index]

    def to_xml(self):
        return docx_to_xml(self)
