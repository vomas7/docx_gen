import pytest
from enum import Enum
from core.ui_objects.base.BaseAttribute import EnumAttribute, BaseAttribute


class EnumAttributeTest(EnumAttribute):
    """Test class attribute with enum"""

    def __init__(self, value: str):
        super().__init__(
            xml_name="test",
            value=value
        )

    class Options(Enum):
        value1 = 'value1'
        value2 = 'value2'
        value3 = 'value3'


class EnumWithSpaces(EnumAttribute):
    """Test class with spaces in values"""

    def __init__(self, value: str):
        super().__init__(
            xml_name="test",
            value=value
        )

    class Options(Enum):
        left = 'left'
        right = 'right'
        center = 'center'


def test_base_attribute_initialization():

    class TestAttr(BaseAttribute):
        @property
        def value(self):
            return self._value

        @value.setter
        def value(self, new_value):
            self._value = new_value

    attr = TestAttr('xml_name')
    attr.value = 'test_value'

    assert attr.xml_name == 'xml_name'
    assert attr.value == 'test_value'


def test_enum_attribute_subclass_requires_enum():
    with pytest.raises(TypeError) as exc_info:
        class InvalidEnumAttr(EnumAttribute):
            pass

    assert "must define an Enum class" in str(exc_info.value)


def test_enum_attribute_initialization():
    attr = EnumAttributeTest('value1')

    assert attr.xml_name == 'test'
    assert attr.value == 'value1'


def test_enum_attribute_initialization_with_enum_instance():
    with pytest.raises(AttributeError):
        EnumAttributeTest(EnumAttributeTest.Options.value2)


def test_enum_attribute_case_insensitive():
    attr = EnumAttributeTest('VALUE1')
    assert attr.value == 'value1'


def test_enum_attribute_trim_spaces():
    attr = EnumAttributeTest('  value2  ')
    assert attr.value == 'value2'


def test_enum_attribute_invalid_value():
    with pytest.raises(ValueError) as exc_info:
        EnumAttributeTest('invalid_value')
    assert "Invalid value" in str(exc_info.value)


def test_enum_attribute_setter_valid_value():
    attr = EnumAttributeTest('value1')
    attr.value = 'value2'
    assert attr.value == 'value2'
    attr.value = EnumAttributeTest.Options.value3
    assert attr.value == 'value3'


def test_enum_attribute_setter_with_enum_name():
    attr = EnumAttributeTest('value1')
    attr.value = 'VALUE2'
    assert attr.value == 'value2'


def test_enum_attribute_setter_invalid_value():
    attr = EnumAttributeTest('value1')
    with pytest.raises(AttributeError) as exc_info:
        attr.value = 'invalid_value'
        assert "Invalid value" in str(exc_info.value)


def test_enum_attribute_setter_wrong_enum_type():

    class WrongEnum(Enum):
        wrong = 'wrong'

    attr = EnumAttributeTest('value1')

    with pytest.raises(TypeError) as exc_info:
        attr.value = WrongEnum.wrong

    assert "Expected Options" in str(exc_info.value)


def test_enum_attribute_enum_class_assignment():
    assert EnumAttributeTest._enum_class == EnumAttributeTest.Options
    assert EnumWithSpaces._enum_class == EnumWithSpaces.Options


def test_multiple_enum_attribute_classes():
    attr1 = EnumAttributeTest('value1')
    attr2 = EnumWithSpaces('left')

    assert attr1.value == 'value1'
    assert attr2.value == 'left'

    with pytest.raises(AttributeError):
        attr2.value = 'value1'


def test_none_value_handling():

    class EnumWithNone(EnumAttribute):

        def __init__(self, value):
            super().__init__('', value)

        class Options(Enum):
            none = None
            value = 'value'

    attr = EnumWithNone(None)
    assert attr.value is None

    attr.value = 'value'
    assert attr.value == 'value'


def test_enum_attribute_repr_and_str():
    attr = EnumAttributeTest('value1')

    repr_str = repr(attr)
    assert 'TestEnumAttribute' in repr_str or 'object' in repr_str

    assert isinstance(str(attr.value), str)


def test_enum_attribute_value_persistence():
    attr = EnumAttributeTest('value1')

    original_value = attr.value
    assert original_value == 'value1'

    attr.value = 'value2'
    assert attr.value == 'value2'
    assert attr.value != original_value

    attr.value = 'value3'
    assert attr.value == 'value3'

    attr.value = 'value1'
    assert attr.value == 'value1'


def test_enum_attribute_with_complex_values():

    class ComplexEnumAttribute(EnumAttribute):

        def __init__(self, value):
            super().__init__('', value)

        class Options(Enum):
            with_spaces = 'with_spaces'
            with_special = 'special-chars_123'
            uppercase = 'UPPERCASE'

    attr = ComplexEnumAttribute('with_spaces')
    assert attr.value == 'with_spaces'

    with pytest.raises(AttributeError):
        attr.value = 'special-chars_123'

    attr.value = 'UPPERCASE'
    assert attr.value == 'UPPERCASE'
