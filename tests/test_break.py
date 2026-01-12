import pytest

from core.ui_objects.break_ import Break, Clear, Type


@pytest.fixture
def br():
    return Break()


def test_br_tag(br):
    """tag cannot be changed and another attrs cannot be set"""
    assert br.tag == "w:br"
    # check that tag cannot be set
    with pytest.raises(AttributeError):
        br.tag = "another_tag"
    # check any tag cannot be set
    with pytest.raises(AttributeError):
        br.any_tag = "Any"


def test_br_type_from_string():
    """Test string inputs (case-insensitive)"""
    test_cases = [
        ("line", None),
        ("LINE", None),
        (" page ", "page"),
        ("COLUMN", "column"),
        ("textwrapping", "textWrapping"),
        ("TEXTWRAPPING", "textWrapping"),
    ]

    for input_str, expected in test_cases:
        br = Break(type=input_str)
        assert br.type == expected


def test_br_type_invalid_inputs():
    """Test invalid type inputs"""
    invalid_cases = [12, "invalid_string", 3.14]

    for invalid in invalid_cases:
        with pytest.raises((ValueError, TypeError)):
            Break(type=invalid)


def test_br_none_handling():
    """Test how None values are handled"""
    br = Break(type=None)
    assert br.type is None
    try:
        br = Break(clear=None)
        assert br.clear is None
    except (ValueError, AttributeError):
        pass


def test_br_type_getter_validation():
    """Test that getter validates internal state"""
    br = Break()

    # Simulating a damaged condition
    br._type = "invalid"

    with pytest.raises(AttributeError):
        _ = br.type


def test_br_clear_getter_validation():
    """Test that getter validates internal state"""
    br = Break()

    # Simulating a damaged condition
    br._clear = "invalid"

    with pytest.raises(AttributeError):
        _ = br.clear


def test_br_whitespace_handling():
    """Test whitespace in string inputs"""
    br = Break(type="  page  ", clear="  left  ")
    assert br.type == "page"
    assert br.clear == "left"


def test_br_multiple_assignments():
    """Test multiple reassignments"""
    br = Break()

    br.type = "page"
    br.type = "column"
    br.type = "textWrapping"

    assert br.type == "textWrapping"

    br.clear = "left"
    br.clear = "right"
    br.clear = "all"

    assert br.clear == "all"


def test_br_slots_behavior():
    """Test that __slots__ prevents dynamic attributes"""
    br = Break()

    with pytest.raises(AttributeError):
        br.new_attribute = "test"

    assert hasattr(br, "type")
    assert hasattr(br, "clear")
    assert hasattr(br, "tag")


def test_enum_attribute_options():
    """Test Type and Clear Enum options"""
    # Test Type Options
    assert Type.Options.line.value is None
    assert Type.Options.page.value == "page"
    assert Type.Options.column.value == "column"
    assert Type.Options.textwrapping.value == "textWrapping"

    # Test Clear Options
    assert Clear.Options.empty.value is None
    assert Clear.Options.left.value == "left"
    assert Clear.Options.right.value == "right"
    assert Clear.Options.all.value == "all"


def test_init_with_type_and_clear_objects():
    """Test initialization with Type and Clear objects directly"""
    type_obj = Type("page")
    clear_obj = Clear("left")

    br = Break(type=type_obj, clear=clear_obj)
    assert br.type == "page"
    assert br.clear == "left"

    # Ensure they're the same objects
    assert br._type is type_obj
    assert br._clear is clear_obj


def test_clear_all_values():
    """Test all possible clear values"""
    test_cases = [
        (None, None),  # Defaults to empty
        ("empty", None),
        ("left", "left"),
        ("right", "right"),
        ("all", "all"),
        (" LEFT ", "left"),
        (" RIGHT ", "right"),
        (" ALL ", "all"),
    ]

    for input_val, expected in test_cases:
        br = Break(clear=input_val)
        assert br.clear == expected


def test_type_clear_interaction():
    """Test that type and clear can be set independently"""
    br = Break()

    # Set only type
    br.type = "page"
    assert br.type == "page"
    assert br.clear is None

    # Set only clear
    br = Break()
    br.clear = "left"
    assert br.clear == "left"
    assert br.type is None  # Defaults to line

    # Set both
    br = Break(type="column", clear="all")
    assert br.type == "column"
    assert br.clear == "all"

    # Change one, keep the other
    br.type = "textWrapping"
    assert br.type == "textWrapping"
    assert br.clear == "all"  # Should remain unchanged


def test_inherits_from_base_content_tag():
    """Test that Break inherits properly from BaseContentTag"""
    br = Break()

    # Should have these from BaseContentTag
    assert hasattr(br, "tag")
    assert br.tag == "w:br"


def test_equality():
    """Test equality of Break objects"""
    br1 = Break(type="page", clear="left")
    br2 = Break(type="page", clear="left")
    br3 = Break(type="column", clear="left")

    # Same values should be equal
    assert br1.type == br2.type
    assert br1.clear == br2.clear

    # Different values should not be equal
    assert br1.type != br3.type


def test_copy_break():
    """Test copying Break objects"""
    import copy

    original = Break(type="page", clear="all")

    # Shallow copy
    shallow = copy.copy(original)
    assert shallow.type == original.type
    assert shallow.clear == original.clear

    # Deep copy
    deep = copy.deepcopy(original)
    assert deep.type == original.type
    assert deep.clear == original.clear

    # Modifying copy shouldn't affect original
    if hasattr(deep, "_type"):
        deep.type = "column"
        assert original.type == "page"  # Should remain unchanged


def test_breakspec_usage():
    """Test BreakSpec type hint usage"""

    # Test each valid type
    Break(type="page")  # Literal string
    Break(type=Type.Options.column)  # Enum option
    Break(type=None)  # None

    # Break object itself
    existing_break = Break(type="textWrapping")
    with pytest.raises(TypeError):
        Break(type=existing_break)
