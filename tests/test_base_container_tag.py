import pytest

from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import Objects


class ConcreteTag(BaseTag):
    def __init__(self, name="TestTag"):
        self.name = name
        super().__init__()

    def tag(self):
        return "w:Tag"


class ConcreteContainer(BaseContainerTag):
    __slots__ = ("attr",)

    def __init__(self, lo=None):
        super().__init__(lo)

    @property
    def tag(self) -> str:
        return "concrete-container"

    @property
    def access_children(self):
        return [{"class": ConcreteTag}, {"class": ConcreteContainer}]

    @property
    def access_property(self):
        return list()


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
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")

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

    lo = Objects(container, [ConcreteTag("Tag1")])
    container.objects = lo

    assert container.objects.linked_parent is container


def test_linked_objects_setter_with_list():
    """Test objects setter with list"""
    container = ConcreteContainer()

    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
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
    tag1 = ConcreteTag("Tag1")
    container = ConcreteContainer([tag1])

    original_lo = container._objects

    tag2 = ConcreteTag("Tag2")
    tag3 = ConcreteTag("Tag3")
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
    tag = ConcreteTag("TestTag")

    container.add(tag)

    assert len(container._objects) == 1
    assert container._objects[0] is tag


def test_add_multiple_tags():
    """Test adding multiple tags"""
    container = ConcreteContainer()
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
    tag3 = ConcreteTag("Tag3")

    container.add(tag1)
    container.add(tag2)
    container.add(tag3)

    assert len(container._objects) == 3
    assert container._objects[0] is tag1
    assert container._objects[1] is tag2
    assert container._objects[2] is tag3


def test_add_to_existing_linked_objects():
    """Test adding tag to existing objects"""
    tag1 = ConcreteTag("Tag1")
    container = ConcreteContainer([tag1])

    tag2 = ConcreteTag("Tag2")
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

    valid_tag = ConcreteTag("Valid")
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

    tag = ConcreteTag("Connector")
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

    for i in range(100):
        container.add(ConcreteTag(f"Tag{i}"))

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

    tags = [ConcreteTag(f"Tag{i}") for i in range(5)]

    for tag in tags:
        container.add(tag)

    assert len(container._objects) == 5

    new_tags = [ConcreteTag(f"NewTag{i}") for i in range(3)]
    container.objects = new_tags

    assert len(container._objects) == 3

    copied = container.objects
    assert len(copied) == 3
    assert copied is container.objects


def test_remove_method():
    """Test remove method"""
    container = ConcreteContainer()
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")

    container.objects = [tag1, tag2]
    container.remove(tag1)

    assert len(container.objects) == 1
    assert container.objects[0] is tag2


def test_remove_nonexistent():
    """Test removing non-existent tag"""
    container = ConcreteContainer()
    tag = ConcreteTag("Tag")

    with pytest.raises(ValueError):
        container.remove(tag)  # Should raise ValueError


def test_pop_method():
    """Test pop method"""
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
    tag3 = ConcreteTag("Tag3")
    container = ConcreteContainer([tag1, tag2, tag3])

    popped = container.pop(1)
    assert popped is tag2
    assert len(container.objects) == 2
    assert container.objects[0] is tag1
    assert container.objects[1] is tag3


def test_pop_default():
    """Test pop with default index"""
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
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
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
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
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
    subtag = ConcreteContainer()
    tag3 = ConcreteTag("Tag3")

    container.objects = [tag1, subtag, tag2, tag3]
    container.remove_children(ConcreteTag)

    assert len(container.objects) == 1
    assert container.objects[0] is subtag
