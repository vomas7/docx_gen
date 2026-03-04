import pytest

from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import Objects, Property


class ConcreteTag(BaseTag):
    __slots__ = ("_some_attr",)

    def __init__(self):
        super().__init__()
        self._some_attr = "some_attr"

    def tag(self):
        return "w:Tag"

    @property
    def some_attr(self):
        return self._some_attr

    @some_attr.setter
    def some_attr(self, value):
        self._some_attr = value


class ConcreteContainer(BaseContainerTag):
    __slots__ = ()

    def __init__(self, obj=None, prop=None):
        super().__init__(obj, prop)

    @property
    def tag(self) -> str:
        return "concrete-container"

    @property
    def access_children(self):
        return [{"class": ConcreteTag}, {"class": ConcreteContainer}]

    @property
    def access_property(self):
        return [{"class": ConcreteTag}, {"class": ConcreteContainer}]


def test_init_with_linked_objects_instance():
    """Test initialization with LinkedObjects instance"""
    container = ConcreteContainer()
    lo = Objects(container, [])

    container_with_lo = ConcreteContainer(lo)

    assert container_with_lo.objects is not lo
    assert isinstance(container_with_lo._objects, Objects)
    assert container_with_lo._objects.linked_parent is container_with_lo


def test_init_with_list_of_base_tags():
    """Test initialization with list of BaseTag objects"""
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()

    container = ConcreteContainer([tag1, tag2])

    assert isinstance(container._objects, Objects)
    assert len(container._objects) == 2
    assert container.objects.linked_parent is container


def test_init_with_empty_list():
    """Test initialization with empty list"""
    container = ConcreteContainer([])

    assert isinstance(container._objects, Objects)
    assert len(container.objects) == 0
    assert container.objects.linked_parent is container


def test_init_with_none():
    """Test initialization with None"""
    container = ConcreteContainer(None)

    assert isinstance(container._objects, Objects)
    assert len(container._objects) == 0
    assert container._objects.linked_parent is container


def test_init_with_invalid_type():
    """Test initialization with invalid type raises TypeError"""
    with pytest.raises(TypeError) as exc_info:
        ConcreteContainer("invalid")

    assert "is not an instance of BaseTag" in str(exc_info.value)


def test_linked_objects_setter_with_linked_objects_instance():
    """Test objects setter with LinkedObjects instance"""
    container = ConcreteContainer()

    lo = Objects(container, [ConcreteTag()])
    container.objects = lo

    assert container.objects.linked_parent is container


def test_linked_objects_setter_with_list():
    """Test objects setter with list"""
    container = ConcreteContainer()

    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    container.objects = [tag1, tag2]

    assert isinstance(container._objects, Objects)
    assert len(container._objects) == 2
    assert container._objects.linked_parent is container


def test_linked_objects_setter_with_empty_list():
    """Test objects setter with empty list"""
    container = ConcreteContainer()

    container.objects = []

    assert isinstance(container._objects, Objects)
    assert len(container._objects) == 0


def test_linked_objects_setter_replaces_existing():
    """Test that setter replaces existing objects"""
    tag1 = ConcreteTag()
    container = ConcreteContainer([tag1])

    original_lo = container._objects

    tag2 = ConcreteTag()
    tag3 = ConcreteTag()
    container.objects = [tag2, tag3]

    assert container._objects is not original_lo
    assert len(container.objects) == 2


def test_linked_objects_setter_with_invalid_type():
    """Test objects setter with invalid type raises TypeError"""
    container = ConcreteContainer()

    with pytest.raises(TypeError) as exc_info:
        container.objects = "invalid"

    assert "is not an instance of BaseTag" in str(exc_info.value)


def test_linked_objects_setter_with_invalid_list():
    """Test objects setter with list containing non-BaseTag"""
    container = ConcreteContainer()

    with pytest.raises(TypeError):
        container.objects = [ConcreteTag("Tag1"), "invalid"]


def test_tag_property_is_abstract():
    """Test that tag property is abstract and must be implemented"""
    with pytest.raises(TypeError) as exc_info:
        BaseContainerTag()

    assert "Can't instantiate abstract class" in str(exc_info.value)
    assert "tag" in str(exc_info.value)


def test_access_children_property_is_abstract():
    """
    Test that access_children property
    is abstract and must be implemented
    """

    class IncompleteContainer(BaseContainerTag):
        @property
        def tag(self) -> str:
            return "incomplete"

    with pytest.raises(TypeError) as exc_info:
        IncompleteContainer()

    assert "Can't instantiate abstract class" in str(exc_info.value)
    assert "access_children" in str(exc_info.value)


def test_add_valid_tag():
    """Test adding valid tag to objects"""
    container = ConcreteContainer()
    tag = ConcreteTag()

    container.add(tag)

    assert len(container._objects) == 1
    assert container._objects[0] is tag


def test_add_multiple_tags():
    """Test adding multiple tags"""
    container = ConcreteContainer()
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    tag3 = ConcreteTag()

    container.add(tag1)
    container.add(tag2)
    container.add(tag3)

    assert len(container._objects) == 3
    assert container._objects[0] is tag1
    assert container._objects[1] is tag2
    assert container._objects[2] is tag3


def test_add_to_existing_linked_objects():
    """Test adding tag to existing objects"""
    tag1 = ConcreteTag()
    container = ConcreteContainer([tag1])

    tag2 = ConcreteTag()
    container.add(tag2)

    assert len(container._objects) == 2


def test_add_with_type_checking():
    """Test that add method respects type checking from LinkedObjects"""

    class RestrictedContainer(BaseContainerTag):
        @property
        def tag(self) -> str:
            return "restricted"

        @property
        def access_children(self):
            return [{"class": ConcreteTag}]

        @property
        def access_property(self) -> list[dict]:
            return []

    class OtherTag(BaseTag):
        @property
        def tag(self) -> str:
            return "test"

    container = RestrictedContainer()

    valid_tag = ConcreteTag()
    container.add(valid_tag)
    assert len(container._objects) == 1

    invalid_tag = OtherTag()

    with pytest.raises(TypeError) as exc_info:
        container.add(invalid_tag)

    assert "It is prohibited to add" in str(exc_info.value)
    assert len(container._objects) == 1


def test_slots_prevent_dynamic_attributes():
    """Test that __slots__ prevents creating dynamic attributes"""
    container = ConcreteContainer()

    with pytest.raises(AttributeError):
        container.new_attribute = "test"

    container._objects = Objects(container, [])
    assert isinstance(container._objects, Objects)


def test_slots_contains_linked_objects():
    """Test that _objects is in __slots__"""
    assert "_objects" in BaseContainerTag.__slots__


def test_circular_reference_handling():
    """Test handling of circular references"""
    container1 = ConcreteContainer()
    container2 = ConcreteContainer()

    tag = ConcreteTag()
    container1.objects = [container2, tag]
    container2.objects = [container1]

    try:
        copied = container1.objects
        assert isinstance(copied, Objects)
    except RecursionError:
        pytest.fail("Deepcopy should handle circular references")


def test_large_number_of_tags():
    """Test with large number of tags"""
    container = ConcreteContainer()

    for _ in range(100):
        container.add(ConcreteTag())

    assert len(container._objects) == 100

    copied = container.objects
    assert len(copied) == 100


def test_memory_efficiency_with_slots():
    """Test memory efficiency with __slots__"""
    import sys

    container_with_slots = ConcreteContainer()
    container_without_slots = type("NoSlots", (), {})()

    slots_size = sys.getsizeof(container_with_slots)

    container_without_slots._objects = Objects(container_with_slots, [])

    no_slots_size = sys.getsizeof(container_without_slots)

    assert slots_size <= no_slots_size + 100


def test_integration_with_linked_objects_validation():
    """Test integration with LinkedObjects validation"""

    class TextTag(BaseTag):
        @property
        def tag(self) -> str:
            return "text"

    class ImageTag(BaseTag):
        @property
        def tag(self) -> str:
            return "image"

    class ParagraphContainer(BaseContainerTag):
        @property
        def tag(self) -> str:
            return "paragraph"

        @property
        def access_children(self):
            return [{"class": TextTag}]

        @property
        def access_property(self) -> list[dict]:
            return []

    paragraph = ParagraphContainer()

    text_tag = TextTag()
    paragraph.add(text_tag)
    assert len(paragraph._objects) == 1

    image_tag = ImageTag()

    with pytest.raises(TypeError) as exc_info:
        paragraph.add(image_tag)

    assert "It is prohibited to add ImageTag" in str(exc_info.value)
    assert len(paragraph._objects) == 1


def test_chaining_operations():
    """Test chaining of operations"""
    container = ConcreteContainer()

    tags = [ConcreteTag() for i in range(5)]

    for tag in tags:
        container.add(tag)

    assert len(container._objects) == 5

    new_tags = [ConcreteTag() for i in range(3)]
    container.objects = new_tags

    assert len(container._objects) == 3

    copied = container.objects
    assert len(copied) == 3
    assert copied is container.objects


def test_remove_method():
    """Test remove method"""
    container = ConcreteContainer()
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()

    container.objects = [tag1, tag2]
    container.remove(tag1)

    assert len(container.objects) == 1
    assert container.objects[0] is tag2


def test_remove_nonexistent():
    """Test removing non-existent tag"""
    container = ConcreteContainer()
    tag = ConcreteTag()

    with pytest.raises(ValueError):
        container.remove(tag)  # Should raise ValueError


def test_pop_method():
    """Test pop method"""
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    tag3 = ConcreteTag()
    container = ConcreteContainer([tag1, tag2, tag3])

    popped = container.pop(1)
    assert popped is tag2
    assert len(container.objects) == 2
    assert container.objects[0] is tag1
    assert container.objects[1] is tag3


def test_pop_default():
    """Test pop with default index"""
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    container = ConcreteContainer([tag1, tag2])

    popped = container.pop()
    assert popped is tag2
    assert len(container.objects) == 1


def test_pop_empty():
    """Test pop from empty container"""
    container = ConcreteContainer()

    with pytest.raises(IndexError):
        container.pop()


def test_find_method():
    """Test find method"""
    container = ConcreteContainer()
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    subtag = ConcreteContainer()

    container.objects = [tag1, subtag, tag2]

    tags = container.find(ConcreteTag)
    assert len(tags) == 2
    assert tag1 in tags
    assert tag2 in tags
    assert subtag not in tags

    containers = container.find(ConcreteContainer)
    assert len(containers) == 1
    assert containers[0] is subtag


def test_remove_children():
    """Test remove_children method"""
    container = ConcreteContainer()
    tag1 = ConcreteTag()
    tag2 = ConcreteTag()
    subtag = ConcreteContainer()
    tag3 = ConcreteTag()

    container.objects = [tag1, subtag, tag2, tag3]
    container.remove_children(ConcreteTag)

    assert len(container.objects) == 1
    assert container.objects[0] is subtag


def test_init_with_property_instance():
    """Test initialization with Property instance"""
    container = ConcreteContainer()
    prop = Property(container, [])

    container_with_prop = ConcreteContainer(prop=prop)

    assert container_with_prop.property is not prop
    assert isinstance(container_with_prop._property, Property)
    assert container_with_prop._property.linked_parent is container_with_prop


def test_init_with_list_of_properties():
    """Test initialization with list of property objects"""
    prop1 = ConcreteTag()
    prop2 = ConcreteContainer()

    container = ConcreteContainer(prop=[prop1, prop2])

    assert isinstance(container._property, Property)
    assert len(container._property) == 2
    assert container.property.linked_parent is container


def test_init_with_empty_list_property():
    """Test initialization with empty list for property"""
    container = ConcreteContainer(prop=[])

    assert isinstance(container._property, Property)
    assert len(container.property) == 0
    assert container.property.linked_parent is container


def test_init_with_none_property():
    """Test initialization with None for property"""
    container = ConcreteContainer(prop=None)

    assert isinstance(container._property, Property)
    assert len(container._property) == 0
    assert container._property.linked_parent is container


def test_init_with_invalid_property_type():
    """Test initialization with invalid property type raises TypeError"""
    with pytest.raises(TypeError) as exc_info:
        ConcreteContainer(prop="invalid")

    assert "is not an instance of BaseTag" in str(exc_info.value)


def test_property_setter_with_property_instance():
    """Test property setter with Property instance"""
    container = ConcreteContainer()
    prop = Property(container, [ConcreteTag()])

    container.property = prop

    assert container.property.linked_parent is container


def test_property_setter_with_list():
    """Test property setter with list"""
    container = ConcreteContainer()
    prop1 = ConcreteTag()

    container.property = [prop1]

    assert isinstance(container._property, Property)
    assert len(container._property) == 1
    assert container._property.linked_parent is container


def test_property_setter_replaces_existing():
    """Test that property setter replaces existing properties"""
    prop1 = ConcreteTag()
    container = ConcreteContainer(prop=[prop1])

    original_prop = container._property

    prop2 = ConcreteTag()
    prop3 = ConcreteTag()
    container.property = [prop2, prop3]

    assert container._property is not original_prop
    assert len(container.property) == 2
    assert container.property[0] is prop2
    assert container.property[1] is prop3


def test_property_setter_with_invalid_type():
    """Test property setter with invalid type raises TypeError"""
    container = ConcreteContainer()

    with pytest.raises(TypeError) as exc_info:
        container.property = "invalid"

    assert "is not an instance of BaseTag" in str(exc_info.value)


def test_property_setter_with_invalid_list():
    """Test property setter with list containing non-BaseTag"""
    container = ConcreteContainer()

    with pytest.raises(TypeError):
        container.property = [ConcreteTag(), "invalid"]


def test_get_property_by_name():
    """Test get_property method with string name"""
    prop_tag = ConcreteTag()
    prop_container = ConcreteContainer()
    container = ConcreteContainer(prop=[prop_tag, prop_container])

    result = container.get_property("ConcreteTag")
    assert result is prop_tag

    result = container.get_property("ConcreteContainer")
    assert result is prop_container


def test_get_property_by_class():
    """Test get_property method with class type"""
    prop_tag = ConcreteTag()
    prop_container = ConcreteContainer()
    container = ConcreteContainer(prop=[prop_tag, prop_container])

    result = container.get_property(ConcreteTag)
    assert result is prop_tag

    result = container.get_property(ConcreteContainer)
    assert result is prop_container


def test_get_property_nonexistent_name():
    """Test get_property with nonexistent name returns None"""
    container = ConcreteContainer(prop=[ConcreteTag()])

    result = container.get_property("NonExistent")
    assert result is None


def test_get_property_nonexistent_class():
    """Test get_property with nonexistent class returns None"""
    container = ConcreteContainer(prop=[ConcreteTag()])

    class AnotherTag(BaseTag):
        pass

    result = container.get_property(AnotherTag)
    assert result is None


def test_get_property_empty_property():
    """Test get_property when property is empty"""
    container = ConcreteContainer()

    result = container.get_property("ConcreteTag")
    assert result is None

    result = container.get_property(ConcreteTag)
    assert result is None


def test_assign_property():
    """Test assign_property method"""
    container = ConcreteContainer()
    prop_tag = ConcreteTag()

    container.assign_property(prop_tag)

    assert len(container.property) == 1
    assert container.property[0] is prop_tag


def test_assign_property_at_correct_position():
    """Test assign_property places property at required position"""
    container = ConcreteContainer()
    prop_tag = ConcreteTag()
    prop_container = ConcreteContainer()

    container.assign_property(prop_container)
    container.assign_property(prop_tag)

    assert len(container.property) == 2
    assert container.property[0] is prop_container
    assert container.property[1] is prop_tag


def test_assign_property_invalid_class():
    """Test assign_property with invalid class raises AttributeError"""
    container = ConcreteContainer()
    invalid_prop = object()

    with pytest.raises(AttributeError) as exc_info:
        container.assign_property(invalid_prop)

    assert "The class of the object" in str(exc_info.value)
    assert "being modified must be in access_property" in str(exc_info.value)


def test_allowed_property_names():
    """Test allowed_property_names property"""
    container = ConcreteContainer()

    assert container.allowed_property_names == ["ConcreteTag", "ConcreteContainer"]


def test_allowed_property_classes():
    """Test allowed_property_classes property"""
    container = ConcreteContainer()

    assert container.allowed_property_classes == [ConcreteTag, ConcreteContainer]


def test_get_property_attr():
    """Test _get_property_attr method"""
    proper = ConcreteTag()
    container = ConcreteContainer(prop=[proper])

    result = container._get_property_attr(ConcreteTag, "some_attr")
    assert result == "some_attr"


def test_get_property_attr_nonexistent():
    """Test _get_property_attr with nonexistent property"""
    container = ConcreteContainer()

    result = container._get_property_attr(ConcreteTag, "value")
    assert result is None


def test_set_property_attr_existing():
    """Test _set_property_attr with existing property"""
    prop_tag = ConcreteTag()
    container = ConcreteContainer(prop=[prop_tag])

    container._set_property_attr(ConcreteTag, "some_attr", "new")

    assert prop_tag.some_attr == "new"


def test_has_active_property_true():
    """Test _has_active_property returns True when property has active attributes"""
    prop_tag = ConcreteTag()
    container = ConcreteContainer(prop=[prop_tag])

    assert container._has_active_property() is True


def test_has_active_property_false():
    """Test _has_active_property returns False when all attributes are None/False"""
    container = ConcreteContainer()
    assert container._has_active_property() is False


def test_cleanup_inactive_property():
    """Test _cleanup_inactive_property removes inactive properties"""
    active_prop = ConcreteTag()
    container = ConcreteContainer(prop=[active_prop])
    container._set_property_attr(ConcreteTag, "some_attr", False)
    container._cleanup_inactive_property()

    assert len(container.property) == 0


def test_autoclean_decorator():
    """Test autoclean decorator cleans up after method execution"""

    class TestContainer(ConcreteContainer):
        def __init__(self):
            super().__init__()
            self._attr = False

        @property
        def attr(self):
            return self._attr

        @attr.setter
        @BaseContainerTag.autoclean
        def attr(self, _):
            self._attr = _

        def add_temp_prop(self):
            self._attr = False

    container = TestContainer()
    container.add_temp_prop()

    # Property should be cleaned up after method execution
    assert len(container.property) == 0


def test_get_property_config():
    """Test _get_property_config returns correct config"""
    container = ConcreteContainer()

    config = container._get_property_config(ConcreteTag)
    assert config == {"class": ConcreteTag}

    config = container._get_property_config(ConcreteContainer)
    assert config == {"class": ConcreteContainer}


def test_get_property_config_invalid():
    """Test _get_property_config with invalid class raises AttributeError"""
    container = ConcreteContainer()

    class AnotherTag:
        pass

    with pytest.raises(AttributeError) as exc_info:
        container._get_property_config(AnotherTag)

    assert "The class of the object" in str(exc_info.value)


def test_get_property_required_position():
    """Test _get_property_required_position returns correct position"""

    class ContainerReq(BaseContainerTag):
        def __init__(self):
            super().__init__()

        @property
        def tag(self) -> str:
            return "test"

        @property
        def access_children(self) -> list[dict]:
            return []

        @property
        def access_property(self):
            return [
                {"class": ConcreteTag, "required_position": 0},
                {"class": ConcreteContainer},
            ]

    container = ContainerReq()

    assert container._get_property_required_position(ConcreteTag) == 0
    assert container._get_property_required_position(ConcreteContainer) is None


def test_is_prop_class():
    """Test is_prop_class static method"""
    config = {"class": ConcreteTag, "required_position": 0}

    class AnotherTag:
        pass

    assert BaseContainerTag.is_prop_class(config, ConcreteTag) is True
    assert BaseContainerTag.is_prop_class(config, ConcreteContainer) is False
    assert BaseContainerTag.is_prop_class(config, AnotherTag) is False


def test_both_objects_and_property_initialization():
    """Test initialization with both objects and property"""
    obj1 = ConcreteTag()
    prop1 = ConcreteTag()

    container = ConcreteContainer(obj=[obj1], prop=[prop1])

    assert len(container.objects) == 1
    assert len(container.property) == 1
    assert container.objects[0] is obj1
    assert container.property[0] is prop1


def test_independence_of_objects_and_property():
    """Test that objects and property are independent collections"""
    container = ConcreteContainer()

    obj = ConcreteTag()
    prop = ConcreteTag()

    container.objects = [obj]
    container.property = [prop]

    assert len(container.objects) == 1
    assert len(container.property) == 1
    assert container.objects[0] is obj
    assert container.property[0] is prop

    # Modifying one shouldn't affect the other
    container.objects.clear()
    assert len(container.objects) == 0
    assert len(container.property) == 1
