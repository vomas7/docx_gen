import pytest
from core.ui_objects.base.BaseTag import BaseTag
from core.ui_objects.base.LinkedObjects import LinkedObjects
from core.ui_objects.base.BaseContainerTag import BaseContainerTag


class ConcreteTag(BaseTag):

    def __init__(self, name="TestTag"):
        self.name = name
        super().__init__()

    def tag(self):
        return "w:Tag"


class ConcreteContainer(BaseContainerTag):

    __slots__ = ("attr", )

    def __init__(self, lo=None):
        super().__init__(lo)

    @property
    def tag(self) -> str:
        return "concrete-container"

    @property
    def access_children(self):
        return {ConcreteTag, ConcreteContainer}


def test_init_with_linked_objects_instance():
    """Test initialization with LinkedObjects instance"""
    container = ConcreteContainer()
    lo = LinkedObjects(container, [])

    container_with_lo = ConcreteContainer(lo)

    assert container_with_lo.linked_objects is not lo
    assert isinstance(container_with_lo._linked_objects, LinkedObjects)
    assert container_with_lo._linked_objects.linked_parent is container_with_lo


def test_init_with_list_of_base_tags():
    """Test initialization with list of BaseTag objects"""
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")

    container = ConcreteContainer([tag1, tag2])

    assert isinstance(container._linked_objects, LinkedObjects)
    assert len(container._linked_objects) == 2
    assert container._linked_objects[0] is tag1
    assert container._linked_objects[1] is tag2
    assert container._linked_objects.linked_parent is container


def test_init_with_empty_list():
    """Test initialization with empty list"""
    container = ConcreteContainer([])

    assert isinstance(container._linked_objects, LinkedObjects)
    assert len(container._linked_objects) == 0
    assert container._linked_objects.linked_parent is container


def test_init_with_none():
    """Test initialization with None"""
    container = ConcreteContainer(None)

    assert isinstance(container._linked_objects, LinkedObjects)
    assert len(container._linked_objects) == 0
    assert container._linked_objects.linked_parent is container


def test_init_with_invalid_type():
    """Test initialization with invalid type raises TypeError"""
    with pytest.raises(TypeError) as exc_info:
        ConcreteContainer("invalid")

    assert "has not BaseTag objects" in str(exc_info.value)


def test_linked_objects_property_getter_returns_deepcopy():
    """Test that linked_objects getter returns deep copy"""
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")

    container = ConcreteContainer([tag1, tag2])

    lo_copy = container.linked_objects

    assert lo_copy is not container._linked_objects
    assert isinstance(lo_copy, LinkedObjects)

    lo_copy.append(ConcreteTag("Tag3"))
    assert len(container._linked_objects) == 2
    assert len(lo_copy) == 3


def test_linked_objects_setter_with_linked_objects_instance():
    """Test linked_objects setter with LinkedObjects instance"""
    container = ConcreteContainer()

    lo = LinkedObjects(container, [ConcreteTag("Tag1")])
    container.linked_objects = lo

    assert container._linked_objects is lo
    assert container._linked_objects.linked_parent is container


def test_linked_objects_setter_with_list():
    """Test linked_objects setter with list"""
    container = ConcreteContainer()

    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
    container.linked_objects = [tag1, tag2]

    assert isinstance(container._linked_objects, LinkedObjects)
    assert len(container._linked_objects) == 2
    assert container._linked_objects.linked_parent is container


def test_linked_objects_setter_with_empty_list():
    """Test linked_objects setter with empty list"""
    container = ConcreteContainer()

    container.linked_objects = []

    assert isinstance(container._linked_objects, LinkedObjects)
    assert len(container._linked_objects) == 0


def test_linked_objects_setter_replaces_existing():
    """Test that setter replaces existing linked_objects"""
    tag1 = ConcreteTag("Tag1")
    container = ConcreteContainer([tag1])

    original_lo = container._linked_objects

    tag2 = ConcreteTag("Tag2")
    tag3 = ConcreteTag("Tag3")
    container.linked_objects = [tag2, tag3]

    assert container._linked_objects is not original_lo
    assert len(container._linked_objects) == 2
    assert container._linked_objects[0] is tag2
    assert container._linked_objects[1] is tag3


def test_linked_objects_setter_with_invalid_type():
    """Test linked_objects setter with invalid type raises TypeError"""
    container = ConcreteContainer()

    with pytest.raises(TypeError) as exc_info:
        container.linked_objects = "invalid"

    assert "has not BaseTag objects" in str(exc_info.value)


def test_linked_objects_setter_with_invalid_list():
    """Test linked_objects setter with list containing non-BaseTag"""
    container = ConcreteContainer()

    with pytest.raises(TypeError) as exc_info:
        container.linked_objects = [ConcreteTag("Tag1"), "invalid"]


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
    """Test adding valid tag to linked_objects"""
    container = ConcreteContainer()
    tag = ConcreteTag("TestTag")

    container.add(tag)

    assert len(container._linked_objects) == 1
    assert container._linked_objects[0] is tag


def test_add_multiple_tags():
    """Test adding multiple tags"""
    container = ConcreteContainer()
    tag1 = ConcreteTag("Tag1")
    tag2 = ConcreteTag("Tag2")
    tag3 = ConcreteTag("Tag3")

    container.add(tag1)
    container.add(tag2)
    container.add(tag3)

    assert len(container._linked_objects) == 3
    assert container._linked_objects[0] is tag1
    assert container._linked_objects[1] is tag2
    assert container._linked_objects[2] is tag3


def test_add_to_existing_linked_objects():
    """Test adding tag to existing linked_objects"""
    tag1 = ConcreteTag("Tag1")
    container = ConcreteContainer([tag1])

    tag2 = ConcreteTag("Tag2")
    container.add(tag2)

    assert len(container._linked_objects) == 2


def test_add_with_type_checking():
    """Test that add method respects type checking from LinkedObjects"""

    class RestrictedContainer(BaseContainerTag):
        @property
        def tag(self) -> str:
            return "restricted"

        @property
        def access_children(self):
            return {ConcreteTag}

    class OtherTag(BaseTag):

        @property
        def tag(self) -> str:
            return "test"

    container = RestrictedContainer()

    valid_tag = ConcreteTag("Valid")
    container.add(valid_tag)
    assert len(container._linked_objects) == 1

    invalid_tag = OtherTag()

    with pytest.raises(TypeError) as exc_info:
        container.add(invalid_tag)

    assert "It is prohibited to add" in str(exc_info.value)
    assert len(container._linked_objects) == 1


def test_slots_prevent_dynamic_attributes():
    """Test that __slots__ prevents creating dynamic attributes"""
    container = ConcreteContainer()

    with pytest.raises(AttributeError):
        container.new_attribute = "test"

    container._linked_objects = LinkedObjects(container, [])
    assert isinstance(container._linked_objects, LinkedObjects)


def test_slots_contains_linked_objects():
    """Test that _linked_objects is in __slots__"""
    assert '_linked_objects' in BaseContainerTag.__slots__


def test_deepcopy_with_nested_structure():
    """Test deepcopy with nested structure"""
    inner_tag1 = ConcreteTag("Inner1")
    inner_tag2 = ConcreteTag("Inner2")

    inner_container = ConcreteContainer([inner_tag1, inner_tag2])

    outer_tag = ConcreteTag("Outer")
    outer_container = ConcreteContainer([inner_container, outer_tag])

    copied_linked_objects = outer_container.linked_objects

    assert copied_linked_objects is not outer_container._linked_objects

    assert copied_linked_objects[0] is not inner_container
    assert isinstance(copied_linked_objects[0], ConcreteContainer)

    new_tag = ConcreteTag("NewTag")
    outer_container._linked_objects.append(new_tag)

    assert len(outer_container._linked_objects) == 3
    assert len(copied_linked_objects) == 2


def test_circular_reference_handling():
    """Test handling of circular references"""
    container1 = ConcreteContainer()
    container2 = ConcreteContainer()

    tag = ConcreteTag("Connector")
    container1.linked_objects = [container2, tag]
    container2.linked_objects = [container1]

    try:
        copied = container1.linked_objects
        assert isinstance(copied, LinkedObjects)
    except RecursionError:
        pytest.fail("Deepcopy should handle circular references")


def test_large_number_of_tags():
    """Test with large number of tags"""
    container = ConcreteContainer()

    for i in range(100):
        container.add(ConcreteTag(f"Tag{i}"))

    assert len(container._linked_objects) == 100

    copied = container.linked_objects
    assert len(copied) == 100


def test_memory_efficiency_with_slots():
    """Test memory efficiency with __slots__"""
    import sys

    container_with_slots = ConcreteContainer()
    container_without_slots = type('NoSlots', (), {})()

    slots_size = sys.getsizeof(container_with_slots)

    container_without_slots._linked_objects = LinkedObjects(
        container_with_slots, []
    )

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
            return {TextTag}

    paragraph = ParagraphContainer()

    text_tag = TextTag()
    paragraph.add(text_tag)
    assert len(paragraph._linked_objects) == 1

    image_tag = ImageTag()

    with pytest.raises(TypeError) as exc_info:
        paragraph.add(image_tag)

    assert "It is prohibited to add ImageTag" in str(exc_info.value)
    assert len(paragraph._linked_objects) == 1


def test_chaining_operations():
    """Test chaining of operations"""
    container = ConcreteContainer()

    tags = [ConcreteTag(f"Tag{i}") for i in range(5)]

    for tag in tags:
        container.add(tag)

    assert len(container._linked_objects) == 5

    new_tags = [ConcreteTag(f"NewTag{i}") for i in range(3)]
    container.linked_objects = new_tags

    assert len(container._linked_objects) == 3

    copied = container.linked_objects
    assert len(copied) == 3
    assert copied is not container._linked_objects
