from lxml import etree
import zipfile
from core.utils.constants import DOC_DEFAULT_PATH
import pytest
from core.ui_objects import Document

parser = etree.XMLParser(remove_blank_text=True)


@pytest.fixture
def default_document_xml():
    with (
        zipfile.ZipFile(DOC_DEFAULT_PATH, "r") as docx_zip,
        docx_zip.open("word/document.xml") as xml_file,
    ):
        xml_content = xml_file.read()
        return etree.fromstring(xml_content, parser=parser)


@pytest.fixture
def document_xml():
    doc = Document()
    return etree.fromstring(doc.to_xml(), parser=parser)


# def test_doc_to_xml(default_document_xml, document_xml):
#     assert etree.tostring(document_xml) == etree.tostring(default_document_xml)
