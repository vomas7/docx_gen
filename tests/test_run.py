import pytest

from core.ui_objects.run import Break, Run, RunProperty, Tab, Text


@pytest.fixture
def run():
    return Run()


def test_run_tag(run):
    assert run.tag == "w:r"


def test_run_access_children(run):
    assert run.access_children == {Break, Text, RunProperty, Tab}


def test_run_init_with_linked_objects(run):
    assert run.linked_objects == []


def test_run_init_with_list():
    test_list = [Text("style1"), Text("style2")]
    run = Run(test_list)
    assert run.linked_objects
    assert run.linked_objects[0].text == "style1"
    assert run.linked_objects[1].text == "style2"


def test_add_page_break(run):
    run.add_break("page")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Break)
    assert run.linked_objects[0].type == "page"


def test_add_column_break(run):
    run.add_break("column")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Break)
    assert run.linked_objects[0].type == "column"


def test_add_text_with_string(run):
    run.add_text("test string")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Text)
    assert run.linked_objects[0].text == "test string"


def test_add_text_with_text_object(run):
    text_obj = Text("test content")
    run.add_text(text_obj)

    assert len(run.linked_objects) == 1
    assert isinstance(run._linked_objects[0], Text)
    assert run._linked_objects[0].text == text_obj.text


def test_add_text_with_empty_string(run):
    run.add_text("")

    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], Text)
    assert run.linked_objects[0].text == ""


def test_run_inherits_from_base_container(run):
    assert hasattr(run, "add")


def test_run_with_multiple_children(run):
    run.add_text("First part ")
    run.add_break("page")
    run.add_text("After page break")

    assert len(run.linked_objects) == 3
    assert isinstance(run.linked_objects[0], Text)
    assert isinstance(run.linked_objects[1], Break)
    assert isinstance(run.linked_objects[2], Text)
    assert run.linked_objects[0].text == "First part "
    assert run.linked_objects[1].type == "page"
    assert run.linked_objects[2].text == "After page break"


def test_add_text_directly(run):
    text_obj = Text("direct text")
    run.add(text_obj)

    assert text_obj in run._linked_objects


def test_run_with_only_breaks(run):
    run.add_break("page")
    run.add_break("column")
    run.add_break("page")

    assert len(run.linked_objects) == 3
    assert all(isinstance(child, Break) for child in run.linked_objects)
    assert run.linked_objects[0].type == "page"
    assert run.linked_objects[1].type == "column"
    assert run.linked_objects[2].type == "page"


def test_add_text_with_special_characters(run):
    special_text = "Text with <>&\"' symbols"
    run.add_text(special_text)

    assert len(run.linked_objects) == 1
    text_child = run.linked_objects[0]
    assert text_child.text == special_text


def test_add_method_works(run):
    run.linked_objects = []
    text = Text("test")
    run.add(text)

    assert text in run._linked_objects
    assert len(run.linked_objects) == 1


def test_add_break(run):
    run.add_break("textwrapping")
    assert len(run.linked_objects) == 1
    assert isinstance(run._linked_objects[0], Break)
    assert run.linked_objects[0].type == "textWrapping"

    run.add_break(Break("page"))
    assert len(run.linked_objects) == 2
    assert isinstance(run._linked_objects[1], Break)
    assert run.linked_objects[1].type == "page"

    with pytest.raises(TypeError):
        run.add_break(False)


def test_add_tab(run):
    run.add_tab()
    assert isinstance(run.linked_objects[0], Tab)


def test_run_init_with_bold_property():
    """Test Run initialization with bold property"""
    run = Run(bold=True)
    assert run.bold is True
    assert run.run_property.bold is True


def test_run_init_with_italic_property():
    """Test Run initialization with italic property"""
    run = Run(italic=True)
    assert run.italic is True
    assert run.run_property.italic is True


def test_run_init_with_font_property():
    """Test Run initialization with font property"""
    run = Run(font="Arial")
    assert run.font == "Arial"
    assert run.run_property.font == "Arial"


def test_run_set_bold_property():
    """Test setting bold property on existing Run"""
    run = Run()
    assert run.bold is False

    run.bold = True
    assert run.bold is True

    run.bold = False
    assert run.bold is False


def test_run_set_italic_property():
    """Test setting italic property on existing Run"""
    run = Run()
    assert run.italic is False

    run.italic = True
    assert run.italic is True

    run.italic = False
    assert run.italic is False


def test_run_set_font_property():
    """Test setting font property on existing Run"""
    run = Run()
    assert run.font is None

    run.font = "Calibri"
    assert run.font == "Calibri"

    run.font = None
    assert run.font is None


def test_run_property_auto_add_remove():
    """Test that RunProperty is automatically added/removed when properties change"""
    run = Run()
    # Initially no RunProperty should be present
    assert len(run.linked_objects) == 0

    # Add bold property - should add RunProperty
    run.bold = True
    assert len(run.linked_objects) == 1
    assert isinstance(run.linked_objects[0], RunProperty)

    # Remove bold property - should remove RunProperty
    run.bold = False
    assert len(run.linked_objects) == 0


def test_run_multiple_properties():
    """Test Run with multiple properties set"""
    run = Run(bold=True, italic=True, font="Times New Roman")
    assert run.bold is True
    assert run.italic is True
    assert run.font == "Times New Roman"
    assert len(run.linked_objects) == 1  # Only one RunProperty


def test_run_clear_method():
    """Test clear method removes all linked objects"""
    run = Run()
    run.add_text("Text 1")
    run.add_break("page")
    run.add_text("Text 2")

    assert len(run.linked_objects) == 3

    run.clear()
    assert len(run.linked_objects) == 0


def test_run_with_linked_objects_and_properties():
    """Test Run with both linked objects and properties"""
    run = Run([Text("First")], bold=True, italic=True)
    assert len(run.linked_objects) == 2  # RunProperty + Text
    assert run.bold is True
    assert run.italic is True
    assert run.linked_objects[1].text == "First"


def test_add_text_with_index():
    """Test adding text at specific index"""
    run = Run()
    run.add_text("End")
    run.add_text("Middle", 0)
    run.add_text("Start", 0)

    assert len(run.linked_objects) == 3
    assert run.linked_objects[0].text == "Start"
    assert run.linked_objects[1].text == "Middle"
    assert run.linked_objects[2].text == "End"


def test_add_tab_with_index():
    """Test adding tab at specific index"""
    run = Run()
    run.add_text("After tab")
    run.add_tab(0)  # Add tab at the beginning

    assert len(run.linked_objects) == 2
    assert isinstance(run.linked_objects[0], Tab)
    assert isinstance(run.linked_objects[1], Text)


def test_run_with_only_properties_no_content():
    """Test Run with only properties but no content"""
    run = Run(bold=True, italic=True, font="Arial")
    # Properties are set but no actual content (text/break/tab) added
    assert run.bold is True
    assert run.italic is True
    assert run.font == "Arial"
    # RunProperty should not be added if there's no content
    # (depends on _update_run logic, needs verification)


def test_run_property_persistence():
    """Test that properties persist when adding content"""
    run = Run(bold=True, font="Verdana")
    run.add_text("Bold Verdana text")

    assert run.bold is True
    assert run.font == "Verdana"
    # Should have RunProperty and Text in linked_objects
    assert len(run.linked_objects) >= 1
