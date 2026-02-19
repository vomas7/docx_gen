import pytest

from core.ui_objects.image.image import Drawing
from core.ui_objects.run import Break, Run, RunProperty, Tab, Text


@pytest.fixture
def run():
    return Run()


def test_run_tag(run):
    assert run.tag == "w:r"


def test_run_access_children(run):
    assert run.access_children == [
        {"class": Break},
        {"class": Text},
        {"class": Tab},
        {"class": Drawing},
    ]


def test_run_init_with_objects(run):
    assert run.objects == []


def test_run_init_with_list():
    test_list = [Text("style1"), Text("style2")]
    run = Run(test_list)
    assert run.objects
    assert run.objects[0].text == "style1"
    assert run.objects[1].text == "style2"


def test_add_page_break(run):
    run.add_break("page")

    assert len(run.objects) == 1
    assert isinstance(run.objects[0], Break)
    assert run.objects[0].type == "page"


def test_add_column_break(run):
    run.add_break("column")

    assert len(run.objects) == 1
    assert isinstance(run.objects[0], Break)
    assert run.objects[0].type == "column"


def test_add_text_with_string(run):
    run.add_text("test string")

    assert len(run.objects) == 1
    assert isinstance(run.objects[0], Text)
    assert run.objects[0].text == "test string"


def test_add_text_with_text_object(run):
    text_obj = Text("test content")
    run.add_text(text_obj)

    assert len(run.objects) == 1
    assert isinstance(run._objects[0], Text)
    assert run._objects[0].text == text_obj.text


def test_add_text_with_empty_string(run):
    run.add_text("")

    assert len(run.objects) == 1
    assert isinstance(run.objects[0], Text)
    assert run.objects[0].text == ""


def test_run_inherits_from_base_container(run):
    assert hasattr(run, "add")


def test_run_with_multiple_children(run):
    run.add_text("First part ")
    run.add_break("page")
    run.add_text("After page break")

    assert len(run.objects) == 3
    assert isinstance(run.objects[0], Text)
    assert isinstance(run.objects[1], Break)
    assert isinstance(run.objects[2], Text)
    assert run.objects[0].text == "First part "
    assert run.objects[1].type == "page"
    assert run.objects[2].text == "After page break"


def test_add_text_directly(run):
    text_obj = Text("direct text")
    run.add(text_obj)

    assert text_obj in run._objects


def test_run_with_only_breaks(run):
    run.add_break("page")
    run.add_break("column")
    run.add_break("page")

    assert len(run.objects) == 3
    assert all(isinstance(child, Break) for child in run.objects)
    assert run.objects[0].type == "page"
    assert run.objects[1].type == "column"
    assert run.objects[2].type == "page"


def test_add_text_with_special_characters(run):
    special_text = "Text with <>&\"' symbols"
    run.add_text(special_text)

    assert len(run.objects) == 1
    text_child = run.objects[0]
    assert text_child.text == special_text


def test_add_method_works(run):
    run.objects = []
    text = Text("test")
    run.add(text)

    assert text in run._objects
    assert len(run.objects) == 1


def test_add_break(run):
    run.add_break("textwrapping")
    assert len(run.objects) == 1
    assert isinstance(run._objects[0], Break)
    assert run.objects[0].type == "textWrapping"

    run.add_break(Break("page"))
    assert len(run.objects) == 2
    assert isinstance(run._objects[1], Break)
    assert run.objects[1].type == "page"

    with pytest.raises(TypeError):
        run.add_break(False)


def test_add_tab(run):
    run.add_tab()
    assert isinstance(run.objects[0], Tab)


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
    assert run.bold is None

    run.bold = True
    assert run.bold is True

    run.bold = False
    assert run.bold is None


def test_run_set_italic_property():
    """Test setting italic property on existing Run"""
    run = Run()
    assert run.italic is None

    run.italic = True
    assert run.italic is True

    run.italic = False
    assert run.italic is None


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
    assert len(run.objects) == 0

    # Add bold property - should add RunProperty
    run.bold = True
    assert len(run.property) == 1
    assert isinstance(run.property[0], RunProperty)

    # Remove bold property - should remove RunProperty
    run.bold = False
    assert len(run.property) == 0


def test_run_multiple_properties():
    """Test Run with multiple properties set"""
    run = Run(bold=True, italic=True, font="Times New Roman")
    assert run.bold is True
    assert run.italic is True
    assert run.font == "Times New Roman"
    assert len(run.property) == 1  # Only one RunProperty


def test_run_clear_method():
    """Test clear method removes all objects"""
    run = Run()
    run.add_text("Text 1")
    run.add_break("page")
    run.add_text("Text 2")

    assert len(run.objects) == 3

    run.clear()
    assert len(run.objects) == 0


def test_run_with_objects_and_properties():
    """Test Run with both objects and properties"""
    run = Run([Text("First")], bold=True, italic=True)
    assert run.bold is True
    assert run.italic is True
    assert run.objects[0].text == "First"


def test_add_text_with_index():
    """Test adding text at specific index"""
    run = Run()
    run.add_text("End")
    run.add_text("Middle", 0)
    run.add_text("Start", 0)

    assert len(run.objects) == 3
    assert run.objects[0].text == "Start"
    assert run.objects[1].text == "Middle"
    assert run.objects[2].text == "End"


def test_add_tab_with_index():
    """Test adding tab at specific index"""
    run = Run()
    run.add_text("After tab")
    run.add_tab(0)  # Add tab at the beginning

    assert len(run.objects) == 2
    assert isinstance(run.objects[0], Tab)
    assert isinstance(run.objects[1], Text)


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
    # Should have RunProperty and Text in objects
    assert len(run.objects) >= 1


def test_update_objects():
    """Test _update_objects method"""
    run = Run()

    # Add property
    run.bold = True
    assert len(run.property) == 1  # RunProperty added

    # Remove property - should remove RunProperty
    run.bold = False
    run._update_properties()  # Явный вызов
    assert len(run.property) == 0

    # Test with multiple properties
    run.bold = True
    run.italic = True
    assert len(run.property) == 1

    run.bold = False  # Remove one property
    run._update_properties()
    assert len(run.property) == 1  # Should still have RunProperty (italic)

    run.italic = False  # Remove last property
    run._update_properties()
    assert len(run.property) == 0  # Should remove RunProperty


def test_set_run_property_edge_cases():
    """Test set_run_property with various scenarios"""
    run = Run()

    # Set property when no RunProperty exists
    run.set_run_property("bold", True)
    assert run.run_property is not None
    assert run.bold is True

    # Update existing property
    run.set_run_property("bold", False)
    assert run.bold is False  # После удаления bold=False → None

    # Set multiple properties
    run.set_run_property("font", "Arial")
    run.set_run_property("italic", True)
    assert run.font == "Arial"
    assert run.italic is True

    # Invalid property name - должен упасть
    with pytest.raises(AttributeError):
        run.set_run_property("invalid_property", "value")


def test_add_break_invalid_types():
    """Test add_break with various invalid inputs"""
    run = Run()

    # Already tested: False
    with pytest.raises(TypeError):
        run.add_break(False)

    # Other invalid types
    with pytest.raises(TypeError):
        run.add_break(None)

    with pytest.raises(TypeError):
        run.add_break(123)

    with pytest.raises(TypeError):
        run.add_break(["page"])

    # Empty string
    with pytest.raises(TypeError):
        run.add_break("")

    # Invalid break type string
    with pytest.raises(ValueError):
        run.add_break("invalid_break_type")


def test_clear_preserves_properties():
    run = Run(bold=True)
    run.add_text("Text 1")
    run.add_text("Text 2")

    assert len(run.objects) == 2

    run.clear()

    assert len(run.objects) == 0
    assert run.bold is True


def test_run_property_property():
    """Test run_property getter thoroughly"""
    run = Run()

    # Initially no run_property
    assert run.run_property is None

    # After adding bold
    run.bold = True
    assert run.run_property is not None
    assert isinstance(run.run_property, RunProperty)

    # After removing all properties
    run.bold = False
    assert run.run_property is None


def test_run_as_base_container():
    """Test that Run properly inherits from BaseContainerTag"""
    run = Run()

    # Inherited methods should work
    run.add(Text("test"))
    assert len(run.objects) == 1

    # find method
    texts = run.find(Text)
    assert len(texts) == 1

    # remove method
    run.remove(texts[0])
    assert len(run.objects) == 0

    # pop method
    run.add_text("text1")
    run.add_text("text2")
    popped = run.pop()
    assert isinstance(popped, Text)
    assert len(run.objects) == 1


def test_run_slots():
    """Test that Run uses __slots__ correctly"""
    run = Run()

    # Should have slots
    assert hasattr(run, "__slots__")
    assert "_bold" in run.__slots__
    assert "_italic" in run.__slots__
    assert "_font" in run.__slots__

    # Can't add new attributes
    with pytest.raises(AttributeError):
        run.new_attribute = "test"
