from typing import IO
import zipfile
from lxml import etree

from core.oxml_magic.parser import make_xml_tree, to_xml_str
from core.writer.recording_tools import create_tmp_dir
from core.writer.recording_tools import folder_to_docx
from core.writer.recording_tools import put_document_xml
from core.writer.recording_tools import clean_temp_dir

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
        return [{"class": Section}, {"class": Paragraph}]

    @property
    def access_property(self) -> list[dict]:
        return list()


class Document(BaseContainerTag):
    def __init__(self, path: str = "default.docx", objects: Objects | list = None):
        super().__init__(objects)
        self.open(path)

    @property
    def tag(self):
        return "w:document"

    @property
    def access_children(self):
        return [{"class": Body}]

    @property
    def access_property(self) -> list[dict]:
        return list()

    def open(self, file: str | IO[bytes]):
        from core.oxml_magic.parser import convert_xml_to_cls

        with (
            zipfile.ZipFile(file, "r") as docx_zip,
            docx_zip.open("word/document.xml") as xml_file,
        ):
            xml_content = xml_file.read()
            xml = etree.fromstring(xml_content)
        [_body] = xml.getchildren()
        self.add(convert_xml_to_cls(_body))

    def save(self, filename: str):
        document_folder_template = create_tmp_dir()
        xml_str = to_xml_str(make_xml_tree(self))
        put_document_xml(document_folder_template, xml_str)
        folder_to_docx(filename, document_folder_template)
        clean_temp_dir(document_folder_template)
