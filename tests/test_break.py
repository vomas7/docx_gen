import pytest

from core.ui_objects.break_ import Break


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
        with pytest.raises((ValueError, AttributeError)):
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
