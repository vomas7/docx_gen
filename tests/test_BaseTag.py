import pytest
from unittest.mock import Mock
from core.ui_objects.base.BaseTag import BaseTag
from core.ui_objects.base.BaseAttribute import BaseAttribute


def test_base_tag_is_abstract():
    """Test that BaseTag cannot be instantiated directly"""

    assert hasattr(BaseTag, '__abstractmethods__')
    assert 'tag' in BaseTag.__abstractmethods__

    with pytest.raises(TypeError) as exc_info:
        BaseTag()

    assert "Can't instantiate abstract class" in str(exc_info.value)


def test_base_tag_without_slots():
    """Test that class without __slots__ raises AttributeError"""

    class InvalidTag(BaseTag):
        @property
        def tag(self):
            return "invalid"

    tag = InvalidTag()

    with pytest.raises(AttributeError) as exc_info:
        _ = tag.attrs

    assert "must define non-empty __slots__" in str(exc_info.value)


def test_concrete_tag_implementation():
    """Test a properly implemented concrete tag"""

    class ConcreteTag(BaseTag):
        __slots__ = ('align', 'color')

        def __init__(self, align_value='left', color_value='red'):
            self.align = Mock(spec=BaseAttribute)
            self.align.xml_name = 'w:align'
            self.align.value = align_value
            self.color = Mock(spec=BaseAttribute)
            self.color.xml_name = 'w:color'
            self.color.value = color_value

        @property
        def tag(self):
            return "w:paragraph"

    tag = ConcreteTag()

    assert tag.tag == "w:paragraph"

    attrs = tag.attrs
    assert len(attrs) == 2
    assert attrs['w:align'] == 'left'
    assert attrs['w:color'] == 'red'


def test_concrete_tag_with_none_attribute():
    """Test tag with None attribute value"""

    class TagWithNone(BaseTag):
        __slots__ = ('align', 'size')

        def __init__(self):
            self.align = Mock(spec=BaseAttribute)
            self.align.xml_name = 'w:align'
            self.align.value = None

            self.size = Mock(spec=BaseAttribute)
            self.size.xml_name = 'w:size'
            self.size.value = 12

        @property
        def tag(self):
            return "w:text"

    tag = TagWithNone()
    attrs = tag.attrs

    assert 'w:align' in attrs
    assert attrs['w:align'] is None
    assert attrs['w:size'] == 12


def test_concrete_tag_with_missing_attribute():
    """Test tag where some slot attribute is not set"""

    class TagWithMissingAttr(BaseTag):
        __slots__ = ('align', 'color', 'size')

        def __init__(self):
            self.align = Mock(spec=BaseAttribute)
            self.align.xml_name = 'w:align'
            self.align.value = 'center'

        @property
        def tag(self):
            return "w:run"

    tag = TagWithMissingAttr()

    assert tag.get_attribute('align') is not None
    assert tag.get_attribute('color') is None
    assert tag.get_attribute('size') is None

    attrs = tag.attrs
    assert len(attrs) == 1
    assert attrs['w:align'] == 'center'


def test_get_attribute_method():
    """Test the get_attribute method"""

    class TestTag(BaseTag):
        __slots__ = ('attr1', 'attr2')

        def __init__(self):
            self.attr1 = Mock(spec=BaseAttribute)
            self.attr1.xml_name = 'w:attr1'
            self.attr1.value = 'value1'

        @property
        def tag(self):
            return "test"

    tag = TestTag()

    # Существующий атрибут
    attr1 = tag.get_attribute('attr1')
    assert attr1 is not None
    assert attr1.value == 'value1'

    # Несуществующий атрибут (в слоте, но не установлен)
    attr2 = tag.get_attribute('attr2')
    assert attr2 is None

    # Атрибут не в слоте
    non_existent = tag.get_attribute('non_existent')
    assert non_existent is None


def test_str_representation():
    """Test string representation of tag"""

    class StringTag(BaseTag):
        __slots__ = ('align', 'bold')

        def __init__(self):
            self.align = Mock(spec=BaseAttribute)
            self.align.xml_name = 'w:align'
            self.align.value = 'center'

            self.bold = Mock(spec=BaseAttribute)
            self.bold.xml_name = 'w:bold'
            self.bold.value = True

        @property
        def tag(self):
            return "w:paragraph"

    tag = StringTag()
    str_repr = str(tag)

    assert str_repr.startswith("StringTag: <w:paragraph")
    assert 'w:align="center"' in str_repr
    assert 'w:bold="True"' in str_repr
    assert str_repr.endswith("/>")


def test_str_with_empty_attrs():
    """Test string representation when no attributes are set"""

    class EmptyAttrTag(BaseTag):
        __slots__ = ('attr1', 'attr2')

        def __init__(self):
            pass

        @property
        def tag(self):
            return "w:empty"

    tag = EmptyAttrTag()
    str_repr = str(tag)

    assert str_repr == "EmptyAttrTag: <w:empty />"


def test_inheritance_with_slots():
    """Test that slots work correctly with inheritance"""

    class ParentTag(BaseTag):
        __slots__ = ('parent_attr',)

        def __init__(self):
            self.parent_attr = Mock(spec=BaseAttribute)
            self.parent_attr.xml_name = 'w:parent'
            self.parent_attr.value = 'parent_value'

        @property
        def tag(self):
            return "w:parent"

    class ChildTag(ParentTag):
        __slots__ = ('child_attr',)

        def __init__(self):
            super().__init__()
            self.child_attr = Mock(spec=BaseAttribute)
            self.child_attr.xml_name = 'w:child'
            self.child_attr.value = 'child_value'

        @property
        def tag(self):
            return "w:child"

    tag = ChildTag()

    assert 'parent_attr' not in tag.__slots__
    assert 'child_attr' in tag.__slots__

    attrs = tag.attrs
    assert len(attrs) == 1
    assert attrs['w:child'] == 'child_value'


def test_attrs_property_performance():
    """Test that attrs property correctly filters None attributes"""

    class PerformanceTag(BaseTag):
        __slots__ = ('attr1', 'attr2', 'attr3')

        def __init__(self):
            self.attr1 = Mock(spec=BaseAttribute)
            self.attr1.xml_name = 'w:attr1'
            self.attr1.value = 'value1'

        @property
        def tag(self):
            return "w:perf"

    tag = PerformanceTag()

    attrs = tag.attrs
    assert len(attrs) == 1
    assert 'w:attr1' in attrs
    assert 'w:attr2' not in attrs
    assert 'w:attr3' not in attrs


def test_attrs_with_false_values():
    """Test attrs with False, 0, empty string values"""

    class FalseValuesTag(BaseTag):
        __slots__ = ('bool_attr', 'int_attr', 'str_attr')

        def __init__(self):
            self.bool_attr = Mock(spec=BaseAttribute)
            self.bool_attr.xml_name = 'w:bool'
            self.bool_attr.value = False

            self.int_attr = Mock(spec=BaseAttribute)
            self.int_attr.xml_name = 'w:int'
            self.int_attr.value = 0

            self.str_attr = Mock(spec=BaseAttribute)
            self.str_attr.xml_name = 'w:str'
            self.str_attr.value = ''

        @property
        def tag(self):
            return "w:values"

    tag = FalseValuesTag()
    attrs = tag.attrs

    assert len(attrs) == 3
    assert attrs['w:bool'] is False
    assert attrs['w:int'] == 0
    assert attrs['w:str'] == ''


def test_mixed_attribute_types():
    """Test tag with different types of attribute values"""

    class MixedTypesTag(BaseTag):
        __slots__ = (
            'str_attr', 'int_attr', 'float_attr', 'bool_attr', 'list_attr'
        )

        def __init__(self):
            self.str_attr = Mock(spec=BaseAttribute)
            self.str_attr.xml_name = 'w:str'
            self.str_attr.value = 'text'

            self.int_attr = Mock(spec=BaseAttribute)
            self.int_attr.xml_name = 'w:int'
            self.int_attr.value = 42

            self.float_attr = Mock(spec=BaseAttribute)
            self.float_attr.xml_name = 'w:float'
            self.float_attr.value = 3.14

            self.bool_attr = Mock(spec=BaseAttribute)
            self.bool_attr.xml_name = 'w:bool'
            self.bool_attr.value = True

            self.list_attr = Mock(spec=BaseAttribute)
            self.list_attr.xml_name = 'w:list'
            self.list_attr.value = [1, 2, 3]

        @property
        def tag(self):
            return "w:mixed"

    tag = MixedTypesTag()
    attrs = tag.attrs
    str_repr = str(tag)

    assert attrs['w:str'] == 'text'
    assert attrs['w:int'] == 42
    assert attrs['w:float'] == 3.14
    assert attrs['w:bool'] is True
    assert attrs['w:list'] == [1, 2, 3]

    assert 'w:str="text"' in str_repr
    assert 'w:int="42"' in str_repr
    assert 'w:float="3.14"' in str_repr
    assert 'w:bool="True"' in str_repr
    assert 'w:list="[1, 2, 3]"' in str_repr
