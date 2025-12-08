import pytest
from docx.enum.text import WD_BREAK_TYPE
from core.ui_objects.Break import Break, BreakTypes, ClearTypes


@pytest.fixture
def br():
    return Break()


def test_br_tag(br):
    """tag cannot be changed and another attrs cannot be set"""
    assert br.tag == 'w:br'
    # check that tag cannot be set
    with pytest.raises(AttributeError):
        br.tag = 'another_tag'
    # check any tag cannot be set
    with pytest.raises(AttributeError):
        br.any_tag = 'Any'


def test_br_type_from_int():
    """Test all integer values"""
    # Test 0-6 (all should be line break)
    for i in range(0, 7):
        br = Break(type=i)
        assert br.type is None
        assert br.clear is None  # clear should not be affected
    # Test page break
    br = Break(type=7)
    assert br.type == 'page'

    # Test column break
    br = Break(type=8)
    assert br.type == 'column'

    # Test textWrapping with clear values
    br = Break(type=9)
    assert br.type == 'textWrapping'
    assert br.clear == 'left'

    br = Break(type=10)
    assert br.type == 'textWrapping'
    assert br.clear == 'right'

    br = Break(type=11)
    assert br.type == 'textWrapping'
    assert br.clear == 'all'


def test_br_type_from_wd_break_type():
    """Test all WD_BREAK_TYPE values"""
    # Test LINE (0)
    br = Break(type=WD_BREAK_TYPE.LINE)
    assert br.type is None

    # Test PAGE (7)
    br = Break(type=WD_BREAK_TYPE.PAGE)
    assert br.type == 'page'

    # Test COLUMN (8)
    br = Break(type=WD_BREAK_TYPE.COLUMN)
    assert br.type == 'column'

    # Test text wrapping types
    br = Break(type=WD_BREAK_TYPE.LINE_CLEAR_LEFT)
    assert br.type == 'textWrapping'
    assert br.clear == 'left'

    br = Break(type=WD_BREAK_TYPE.LINE_CLEAR_RIGHT)
    assert br.type == 'textWrapping'
    assert br.clear == 'right'

    br = Break(type=WD_BREAK_TYPE.LINE_CLEAR_ALL)
    assert br.type == 'textWrapping'
    assert br.clear == 'all'


def test_br_type_from_string():
    """Test string inputs (case insensitive)"""
    test_cases = [
        ('line', None),
        ('LINE', None),
        (' page ', 'page'),
        ('COLUMN', 'column'),
        ('textwrapping', 'textWrapping'),
        ('TEXTWRAPPING', 'textWrapping'),
    ]

    for input_str, expected in test_cases:
        br = Break(type=input_str)
        assert br.type == expected


def test_br_type_from_enum():
    """Test BreakTypes enum inputs"""
    br = Break(type=BreakTypes.line)
    assert br.type is None

    br = Break(type=BreakTypes.page)
    assert br.type == 'page'

    br = Break(type=BreakTypes.column)
    assert br.type == 'column'

    br = Break(type=BreakTypes.textwrapping)
    assert br.type == 'textWrapping'


def test_br_type_invalid_inputs():
    """Test invalid type inputs"""
    invalid_cases = [12, 'invalid_string', 3.14]

    for invalid in invalid_cases:
        with pytest.raises((ValueError, AttributeError)):
            Break(type=invalid)


def test_br_combined_init():
    """Test initialization with both type and clear"""
    br = Break(type=6, clear='right')
    assert br.type is None
    assert br.clear == 'right'

    br = Break(type=9, clear='right')
    assert br.type == 'textWrapping'
    # because of type changes clear after its initial
    assert br.clear == 'left'


def test_br_reverse_combined_init():
    """Test that clear is overwritten when specified after type"""
    br = Break(type=WD_BREAK_TYPE.LINE_CLEAR_ALL)
    assert br.clear == 'all'

    br.clear = 'left'
    assert br.clear == 'left'


def test_br_empty_string_type():
    """Test empty string type"""
    br = Break(type='')
    assert br.type is None
    assert br.clear is None


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
    br._Break__type = 'invalid'

    with pytest.raises(AttributeError):
        _ = br.type


def test_br_clear_getter_validation():
    """Test that getter validates internal state"""
    br = Break()

    # Simulating a damaged condition
    br._Break__clear = 'invalid'

    with pytest.raises(AttributeError):
        _ = br.clear


def test_br_whitespace_handling():
    """Test whitespace in string inputs"""
    br = Break(type='  page  ', clear='  left  ')
    assert br.type == 'page'
    assert br.clear == 'left'


def test_br_multiple_assignments():
    """Test multiple reassignments"""
    br = Break()

    br.type = 'page'
    br.type = 'column'
    br.type = BreakTypes.textwrapping

    assert br.type == 'textWrapping'

    br.clear = 'left'
    br.clear = 'right'
    br.clear = ClearTypes.all

    assert br.clear == 'all'


def test_br_slots_behavior():
    """Test that __slots__ prevents dynamic attributes"""
    br = Break()

    with pytest.raises(AttributeError):
        br.new_attribute = 'test'

    assert hasattr(br, 'type')
    assert hasattr(br, 'clear')
    assert hasattr(br, 'tag')


def test_br_immutability_of_enums():
    """Test that we can't modify enum values through the class"""
    br1 = Break(type=BreakTypes.page)
    br2 = Break(type=BreakTypes.page)

    assert br1.type == br2.type == 'page'

    assert br1._Break__type is br2._Break__type is BreakTypes.page
