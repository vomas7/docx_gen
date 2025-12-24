import pytest

from core.ui_objects.base.linked_objects import LinkedObjects


class BaseContainerTag:
    @property
    def access_children(self):
        return None


class TextTag(BaseContainerTag):
    @property
    def access_children(self):
        return {}

    @property
    def tag(self):
        return "w:t"


class ImageTag(BaseContainerTag):
    @property
    def access_children(self):
        return ()

    @property
    def tag(self):
        return "w:drawing"


class ParagraphTag(BaseContainerTag):
    @property
    def access_children(self):
        return {TextTag, ImageTag, str}

    @property
    def tag(self):
        return "w:p"


class TableTag(BaseContainerTag):
    @property
    def access_children(self):
        return ()

    @property
    def tag(self):
        return "w:tbl"


def test_linked_objects_initialization():
    """Test basic initialization with linked_parent"""
    parent = BaseContainerTag()

    lo = LinkedObjects(parent, [1, 2, 3])

    assert lo.linked_parent == parent
    assert len(lo) == 3
    assert lo[0] == 1
    assert lo[1] == 2
    assert lo[2] == 3


def test_linked_objects_with_container_tags():
    """Test with actual container tags"""
    paragraph = ParagraphTag()

    lo = LinkedObjects(paragraph, [TextTag(), ImageTag()])

    assert lo.linked_parent == paragraph
    assert lo.linked_parent.access_children == {TextTag, ImageTag, str}


def test_validate_access_child_allowed():
    """Test validation with allowed child"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [TextTag()])

    text_tag = TextTag()
    try:
        lo.validate_access_child(text_tag)
    except TypeError:
        pytest.fail("TextTag should be allowed for Paragraph")


def test_validate_access_child_prohibited():
    """Test validation with prohibited child"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    table_tag = TableTag()

    with pytest.raises(TypeError) as exc_info:
        lo.validate_access_child(table_tag)

    assert "It is prohibited to add" in str(exc_info.value)
    assert "TableTag" in str(exc_info.value)
    assert "ParagraphTag" in str(exc_info.value)


def test_append_with_validation():
    """Test that append validates before adding"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = TextTag()

    lo.append(text_tag)
    assert len(lo) == 1
    assert lo[0] == text_tag

    table_tag = TableTag()

    with pytest.raises(TypeError):
        lo.append(table_tag)

    assert len(lo) == 1


def test_insert_with_validation():
    """Test that insert validates before adding"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, ["item1", "item3"])

    text_tag = TextTag()

    lo.insert(1, text_tag)
    assert len(lo) == 3
    assert lo[0] == "item1"
    assert lo[1] == text_tag
    assert lo[2] == "item3"

    table_tag = TableTag()

    with pytest.raises(TypeError):
        lo.insert(0, table_tag)

    assert len(lo) == 3


def test_extend_with_list_validation():
    """Test that extend validates list items"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = TextTag()

    image_tag = ImageTag()

    lo.extend([text_tag, image_tag])
    assert len(lo) == 2
    assert lo[0] == text_tag
    assert lo[1] == image_tag


def test_extend_with_mixed_list():
    """Test extend with mixed allowed/prohibited items"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = TextTag()

    table_tag = TableTag()

    image_tag = ImageTag()

    with pytest.raises(TypeError):
        lo.extend([text_tag, table_tag, image_tag])

    assert len(lo) == 0


def test_extend_with_linked_objects():
    """Test extend with another LinkedObjects"""
    paragraph = ParagraphTag()
    lo1 = LinkedObjects(paragraph, [])
    lo2 = LinkedObjects(paragraph, [])

    text_tag = TextTag()

    lo2.append(text_tag)

    lo1.extend(lo2)
    assert len(lo1) == 1
    assert lo1[0] == text_tag


def test_setitem_with_validation():
    """Test that __setitem__ validates"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [TextTag()])

    text_tag = TextTag()

    lo[0] = text_tag
    assert lo[0] == text_tag

    table_tag = TableTag()

    with pytest.raises(TypeError):
        lo[1] = table_tag


def test_initialization_validation():
    """Test that initialization validates items"""
    paragraph = ParagraphTag()

    text_tag = TextTag()

    table_tag = TableTag()

    lo1 = LinkedObjects(paragraph, [text_tag])
    assert len(lo1) == 1

    try:
        LinkedObjects(paragraph, [table_tag])
        pytest.fail("Should have raised TypeError")
    except TypeError:
        pass


def test_empty_allowed_children():
    """Test when parent has no allowed children"""
    text = TextTag()
    lo = LinkedObjects(text, [])

    another_text = TextTag()

    lo.append(another_text)
    assert lo[0] == another_text


def test_none_item_validation():
    """Test validation with None item"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    try:
        lo.validate_access_child(None)
    except Exception as e:
        pytest.fail(f"None should not raise error: {e}")


def test_non_container_tag_validation():
    """Test validation with non-container item"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    with pytest.raises(TypeError):
        lo.validate_access_child(type("regular", (), {}))


def test_real_scenario_paragraph_children():
    """Test real scenario: paragraph containing text and image"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = TextTag()
    lo.append(text_tag)

    image_tag = ImageTag()
    lo.append(image_tag)

    assert len(lo) == 2
    assert isinstance(lo[0], TextTag)
    assert isinstance(lo[1], ImageTag)

    table_tag = TableTag()

    with pytest.raises(TypeError) as exc_info:
        lo.append(table_tag)

    assert "TableTag" in str(exc_info.value)
    assert "ParagraphTag" in str(exc_info.value)
