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

    # Существующий атрибут
    attr1 = tag.get_attribute("attr1")
    assert attr1 is not None
    assert attr1.value == "value1"

    # Несуществующий атрибут (в слоте, но не установлен)
    attr2 = tag.get_attribute("attr2")
    assert attr2 is None

    # Атрибут не в слоте
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
