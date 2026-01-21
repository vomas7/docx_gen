from copy import deepcopy, copy

import pytest
from core.ui_objects.section import Section
from core.ui_objects.section import PageSize, PageMargin, Cols,  DocGrid
from core.ui_objects.paragraph import Paragraph
from core.ui_objects.run import Run

@pytest.fixture
def section():
    return Section()

@pytest.fixture
def filled_section(section):
    p = Paragraph()
    p1 = Paragraph()
    r = Run()
    return Section(objects=[p, p1, r])

def test_init(section):
    assert isinstance(section, Section)
    test_access_prop = [PageSize,
                   PageMargin,
                   Cols,
                   DocGrid]
    assert len(section.access_property) == len(test_access_prop)
    for prop in section.access_property:
        assert prop["class"] in test_access_prop

    for prop in section.property:
        assert prop["class"].__class__ in test_access_prop

    assert len(section.objects) == 0

    assert section.tag == "w:sectPr"

def test_provide_init():
    elems = [Paragraph(), Run()]
    section = Section(objects=elems)
    assert section.tag == "w:sectPr"
    assert section.objects == elems
    prop = [PageSize(), PageMargin(), Cols(), DocGrid()]
    section = Section(property=prop)
    assert section.tag == "w:sectPr"
    assert section.property == prop


def test_add_object(section):
    p = Paragraph()
    r = Run()
    section.add(p)
    assert len(section.objects) == 1
    assert section.objects[0] == p
    section.add(r)
    assert section.objects[1] == r


def test_remove_object(filled_section):
    cur_sec = copy(filled_section)
    assert cur_sec.objects == filled_section.objects
    for item in reversed(filled_section.objects):
        cur_sec.remove(item)
        assert item not in filled_section.objects
    assert len(cur_sec.objects) == 0

def test_pop_object(filled_section):
    objects = copy(filled_section.objects)
    deleted = list(map(lambda x: filled_section.objects.pop(x),
                       range(len(filled_section.objects) - 1, -1, -1)))
    deleted.reverse()
    assert deleted == objects
    assert len(filled_section.objects) == 0

def test_find_object(filled_section):
    founds = filled_section.find(Paragraph)
    assert all([isinstance(i, Paragraph) for i in founds])

def test_remove_children_object(filled_section):
    cur_sec = deepcopy(filled_section)
    cur_sec.remove_children(Paragraph)
    assert cur_sec.find(Paragraph) == []


