from lxml import etree
from core.oxml_magic.ns import XmlString
import pytest
from core.io.api import parse_document_part
from core.ui_objects import Document
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.run import Run
from core.ui_objects.section import Section


@pytest.fixture
def default_xml() -> etree.Element:
    return parse_document_part()._element

def document():
    doc = Document()
    doc.open()
    return doc

@pytest.fixture()
def any_objects(document):
    r = Run()
    r.add_text("test1")
    nested_elem = Section(objects=[Paragraph(objects=[r])])
    return [document, Section(), Paragraph(), Run(), nested_elem]


def test_convert_to_xml(any_objects):
    ...


def test_from_xml_to_cls(default_xml):
    doc = parse_document_part(default_xml)
    # pass