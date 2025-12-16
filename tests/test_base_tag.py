from unittest.mock import Mock

import pytest

from core.ui_objects.base.base_attribute import BaseAttribute
from core.ui_objects.base.base_tag import BaseTag


def test_base_tag_is_abstract():
    """Test that BaseTag cannot be instantiated directly"""

    assert hasattr(BaseTag, "__abstractmethods__")
    assert "tag" in BaseTag.__abstractmethods__

    with pytest.raises(TypeError) as exc_info:
        BaseTag()

    assert "Can't instantiate abstract class" in str(exc_info.value)


def test_get_attribute_method():
    """Test the get_attribute method"""

    class TestTag(BaseTag):
        __slots__ = ("attr1", "attr2")

        def __init__(self):
            self.attr1 = Mock(spec=BaseAttribute)
            self.attr1.xml_name = "w:attr1"
            self.attr1.value = "value1"

        @property
        def tag(self):
            return "test"

    tag = TestTag()

    attr1 = tag.get_attribute("attr1")
    assert attr1 is not None
    assert attr1.value == "value1"

    attr2 = tag.get_attribute("attr2")
    assert attr2 is None

    non_existent = tag.get_attribute("non_existent")
    assert non_existent is None


def test_str_with_empty_attrs():
    """Test string representation when no attributes are set"""

    class EmptyAttrTag(BaseTag):
        __slots__ = ("attr1", "attr2")

        def __init__(self):
            pass

        @property
        def tag(self):
            return "w:empty"

    tag = EmptyAttrTag()
    str_repr = str(tag)

    assert str_repr == "EmptyAttrTag: <w:empty />"


def test_attrs_property_with_values():
    """Test attrs property when attributes have values"""

    class TestTag(BaseTag):
        __slots__ = ("attr1", "attr2")

        def __init__(self):
            mock_attr1 = Mock(spec=BaseAttribute)
            mock_attr1.xml_name = "w:attr1"
            mock_attr1.value = "value1"

            mock_attr2 = Mock(spec=BaseAttribute)
            mock_attr2.xml_name = "xml:attr2"
            mock_attr2.value = "value2"

            self.attr1 = mock_attr1
            self.attr2 = mock_attr2

        @property
        def tag(self):
            return "w:test"

    tag = TestTag()
    attrs = tag.attrs

    assert len(attrs) == 2
    assert attrs[("{http://schemas.openxmlformats.org/wordprocessingml/2006"
                  "/main}attr1")] == "value1"
    assert attrs["{http://www.w3.org/XML/1998/namespace}attr2"] == "value2"


def test_attrs_property_with_none_values():
    """Test attrs property when attributes have None values"""

    class TestTag(BaseTag):
        __slots__ = ("attr1", "attr2")

        def __init__(self):
            mock_attr1 = Mock(spec=BaseAttribute)
            mock_attr1.xml_name = "w:attr1"
            mock_attr1.value = None

            mock_attr2 = Mock(spec=BaseAttribute)
            mock_attr2.xml_name = "w:attr2"
            mock_attr2.value = "actual_value"

            self.attr1 = mock_attr1
            self.attr2 = mock_attr2

        @property
        def tag(self):
            return "w:test"

    tag = TestTag()
    attrs = tag.attrs

    assert len(attrs) == 1
    assert "w:attr1" not in attrs
    assert attrs[("{http://schemas.openxmlformats.org/wordprocessingml/2006/"
                  "main}attr2")] == "actual_value"


def test_attrs_property_with_missing_attributes():
    """Test attrs property when some slot attributes are not set"""

    class TestTag(BaseTag):
        __slots__ = ("attr1", "attr2", "attr3")

        def __init__(self):
            mock_attr1 = Mock(spec=BaseAttribute)
            mock_attr1.xml_name = "w:attr1"
            mock_attr1.value = "value1"
            self.attr1 = mock_attr1

        @property
        def tag(self):
            return "w:test"

    tag = TestTag()
    attrs = tag.attrs

    assert len(attrs) == 1
    assert attrs[("{http://schemas.openxmlformats.org/wordprocessingml/2006/"
                  "main}attr1")] == "value1"


def test_str_representation():
    """Test string representation with multiple attributes"""

    class TestTag(BaseTag):
        __slots__ = ("attr1", "attr2", "attr3")

        def __init__(self):
            mock_attr1 = Mock(spec=BaseAttribute)
            mock_attr1.xml_name = "w:attr1"
            mock_attr1.value = "value1"

            mock_attr2 = Mock(spec=BaseAttribute)
            mock_attr2.xml_name = "r:attr2"
            mock_attr2.value = "value2"

            mock_attr3 = Mock(spec=BaseAttribute)
            mock_attr3.xml_name = "xsi:attr3"
            mock_attr3.value = "value3 with spaces"

            self.attr1 = mock_attr1
            self.attr2 = mock_attr2
            self.attr3 = mock_attr3

        @property
        def tag(self):
            return "w:testTag"

    tag = TestTag()
    str_repr = str(tag)

    assert "TestTag: <w:testTag " in str_repr
    assert 'attr1="value1"' in str_repr
    assert 'attr2="value2"' in str_repr
    assert 'attr3="value3 with spaces"' in str_repr
    assert str_repr.endswith("/>")


def test_slots_empty():
    """Test BaseTag with empty slots"""

    class EmptySlotsTag(BaseTag):
        __slots__ = ()

        @property
        def tag(self):
            return "w:empty"

        def __init__(self):
            pass

    tag = EmptySlotsTag()

    # Should work without errors
    assert tag.attrs == {}
    assert str(tag) == "EmptySlotsTag: <w:empty />"


def test_slots_not_defined():
    """Test BaseTag when __slots__ is not defined in subclass"""

    class NoSlotsTag(BaseTag):
        # No __slots__ defined
        @property
        def tag(self):
            return "w:noSlots"

        def __init__(self):
            pass

    tag = NoSlotsTag()

    # attrs should handle missing __slots__ gracefully
    assert tag.attrs == {}
    assert str(tag) == "NoSlotsTag: <w:noSlots />"


def test_get_attribute_with_non_attribute_object():
    """Test get_attribute when slot contains non-BaseAttribute object"""

    class TestTag(BaseTag):
        __slots__ = ("not_an_attribute",)

        def __init__(self):
            # This is not a BaseAttribute, just a regular string
            self.not_an_attribute = "just a string"

        @property
        def tag(self):
            return "w:test"

    tag = TestTag()

    # get_attribute should return the object
    result = tag.get_attribute("not_an_attribute")
    assert result == "just a string"

    # attrs should handle this gracefully (no xml_name attribute)
    attrs = tag.attrs
    assert attrs == {}  # Should be empty since it's not a BaseAttribute


def test_multiple_instances_different_values():
    """Test that different instances have independent attribute values"""

    class TestTag(BaseTag):
        __slots__ = ("attr1",)

        def __init__(self, value):
            mock_attr = Mock(spec=BaseAttribute)
            mock_attr.xml_name = "w:attr"
            mock_attr.value = value
            self.attr1 = mock_attr

        @property
        def tag(self):
            return "w:test"

    tag1 = TestTag("value1")
    tag2 = TestTag("value2")

    assert tag1.attrs != tag2.attrs
    assert tag1.get_attribute("attr1").value == "value1"
    assert tag2.get_attribute("attr1").value == "value2"
