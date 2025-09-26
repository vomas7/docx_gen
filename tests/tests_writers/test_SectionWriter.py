import pytest
from docx.shared import Emu
from docx.api import Document
from core.doc import DOC
from core.styles.section import SectionStyle
from core.doc_objects.Section import DOCSection


@pytest.fixture
def test_doc():
    return DOC()


def test_add_section_to_the_end(test_doc):
    test_section = DOCSection()
    style = SectionStyle(left_margin=10, page_width=30, page_height=60)
    # check count of sections before adding
    assert len(test_doc.sections) == 1
    # add new section
    test_doc.writer.add_section(test_section)
    test_section.add_style(style)
    assert len(test_doc.sections) == 2
    existed_section = test_doc.sections[0]
    appended_section = test_doc.sections[1]
    assert round(existed_section.left_margin.cm, 2) == 3.17
    assert round(appended_section.left_margin.cm, 2) == 10.00
    test_doc.save(r'C:\Users\Balabanov.DA\PycharmProjects\docx_gen\test.docx')
