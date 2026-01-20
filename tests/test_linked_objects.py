import pytest

from core.ui_objects.base.linked_objects import Objects


class BaseContainerTag:
    @property
    def access_children(self):
        return [{"class": int}]


class TextTag(BaseContainerTag):
    @property
    def access_children(self):
        return [{"class": str}]

    @property
    def tag(self):
        return "w:t"

    def __str__(self):
        return "<TextTag>"


class ImageTag(BaseContainerTag):
    @property
    def access_children(self):
        return ()

    @property
    def tag(self):
        return "w:drawing"

    def __str__(self):
        return "<ImageTag>"


class ParagraphTag(BaseContainerTag):
    def __init__(self):
        self._access_children = [
            {"class": TextTag},
            {"class": ImageTag},
            {"class": str},
        ]

    @property
    def access_children(self):
        return self._access_children

    @property
    def tag(self):
        return "w:p"

    def __str__(self):
        return "<ParagraphTag>"


class TableTag(BaseContainerTag):
    def __init__(self):
        self._access_children = []

    @property
    def access_children(self):
        return self._access_children

    @property
    def tag(self):
        return "w:tbl"

    def __str__(self):
        return "<TableTag>"


def test_linked_objects_initialization():
    """Test basic initialization with linked_parent"""
    parent = BaseContainerTag()

    lo = Objects(parent, [1, 2, 3])

    assert lo.linked_parent == parent
    assert len(lo) == 3
    assert lo[0] == 1
    assert lo[1] == 2
    assert lo[2] == 3


def test_linked_objects_with_container_tags():
    """Test with actual container tags"""
    paragraph = ParagraphTag()

    lo = Objects(paragraph, [TextTag(), ImageTag()])

    assert lo.linked_parent == paragraph
    assert len(lo.linked_parent.access_children) == 3


def test_validate_access_child_allowed():
    """Test validation with allowed child"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    text_tag = TextTag()
    try:
        result = lo.validate_access_child(text_tag, 0)
        assert result is True
    except TypeError:
        pytest.fail("TextTag should be allowed for Paragraph")


def test_validate_access_child_prohibited():
    """Test validation with prohibited child"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    table_tag = TableTag()

    with pytest.raises(TypeError) as exc_info:
        lo.validate_access_child(table_tag, 0)

    assert "It is prohibited to add" in str(exc_info.value)
    assert "TableTag" in str(exc_info.value)
    assert "ParagraphTag" in str(exc_info.value)


def test_append_with_validation():
    """Test that append validates before adding"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

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
    lo = Objects(paragraph, ["item1", "item3"])

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
    lo = Objects(paragraph, [])

    text_tag = TextTag()
    image_tag = ImageTag()

    lo.extend([text_tag, image_tag])
    assert len(lo) == 2
    assert lo[0] == text_tag
    assert lo[1] == image_tag


def test_extend_with_mixed_list():
    """Test extend with mixed allowed/prohibited items"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    text_tag = TextTag()
    table_tag = TableTag()
    image_tag = ImageTag()

    with pytest.raises(TypeError):
        lo.extend([text_tag, table_tag, image_tag])

    assert len(lo) == 0


def test_extend_with_linked_objects():
    """Test extend with another LinkedObjects"""
    paragraph = ParagraphTag()
    lo1 = Objects(paragraph, [])
    lo2 = Objects(paragraph, [])

    text_tag = TextTag()

    lo2.append(text_tag)

    lo1.extend(lo2)
    assert len(lo1) == 1
    assert lo1[0] == text_tag


def test_setitem_with_validation():
    """Test that __setitem__ validates"""
    paragraph = ParagraphTag()
    text1 = TextTag()
    text2 = TextTag()
    lo = Objects(paragraph, [text1])

    lo[0] = text2
    assert lo[0] == text2

    table_tag = TableTag()

    with pytest.raises(TypeError):
        lo[0] = table_tag


def test_initialization_validation():
    """Test that initialization validates items"""
    paragraph = ParagraphTag()

    text_tag = TextTag()
    table_tag = TableTag()

    lo1 = Objects(paragraph, [text_tag])
    assert len(lo1) == 1

    with pytest.raises(TypeError):
        Objects(paragraph, [table_tag])


def test_none_item_validation():
    """Test validation with None item"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    result = lo.validate_access_child(None, 0)
    assert result is None


def test_non_container_tag_validation():
    """Test validation with non-container item"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    class RegularClass:
        pass

    regular_obj = RegularClass()

    with pytest.raises(TypeError):
        lo.validate_access_child(regular_obj, 0)


def test_real_scenario_paragraph_children():
    """Test real scenario: paragraph containing text and image"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

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


def test_validate_access_child_string_allowed():
    """Test that string is allowed for ParagraphTag"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    result = lo.validate_access_child("test string", 0)
    assert result is True

    lo.append("test")
    assert lo[0] == "test"


def test_validate_access_child_with_position_validation():
    """Test validation with required_position"""

    class StrictTag(BaseContainerTag):
        def __init__(self):
            self._access_children = [
                {"class": TextTag, "required_position": 0},
                {"class": ImageTag, "required_position": 1},
            ]

        @property
        def access_children(self):
            return self._access_children

    strict_parent = StrictTag()
    lo = Objects(strict_parent, [])

    text_tag = TextTag()
    # TextTag должен быть на позиции 0
    lo.validate_access_child(text_tag, 0)
    lo.append(text_tag)
    assert lo[0] == text_tag

    image_tag = ImageTag()
    # ImageTag должен быть на позиции 1
    with pytest.raises(IndexError) as exc_info:
        lo.validate_access_child(image_tag, 0)  # Пытаемся поставить на позицию 0
    assert "must be on position" in str(exc_info.value)

    # Правильно - на позицию 1
    lo.validate_access_child(image_tag, 1)
    lo.append(image_tag)
    assert lo[1] == image_tag


def test_insert_with_required_position():
    """Test insert with required position validation"""

    class StrictTag(BaseContainerTag):
        def __init__(self):
            self._access_children = [{"class": TextTag, "required_position": 0}]

        @property
        def access_children(self):
            return self._access_children

    strict_parent = StrictTag()
    lo = Objects(strict_parent, [])

    text_tag = TextTag()
    # Вставка на правильную позицию
    lo.insert(0, text_tag)
    assert lo[0] == text_tag

    # Попытка вставить на неправильную позицию
    another_text = TextTag()
    with pytest.raises(IndexError):
        lo.insert(1, another_text)


def test_setitem_with_required_position():
    """Test __setitem__ with required position validation"""

    class StrictTag(BaseContainerTag):
        def __init__(self):
            self._access_children = [
                {"class": TextTag, "required_position": 0},
                {"class": ImageTag, "required_position": 1},
            ]

        @property
        def access_children(self):
            return self._access_children

    strict_parent = StrictTag()
    text_tag = TextTag()
    image_tag = ImageTag()
    lo = Objects(strict_parent, [text_tag, image_tag])

    # Правильная замена
    new_text = TextTag()
    lo[0] = new_text
    assert lo[0] == new_text

    # Неправильная замена - пытаемся поставить TextTag на позицию 1
    with pytest.raises(IndexError):
        lo[1] = TextTag()


def test_validate_access_children():
    """Test validate_access_children method"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    items = [TextTag(), ImageTag(), "string"]
    lo.validate_access_children(items)

    with pytest.raises(TypeError):
        lo.validate_access_children([TextTag(), TableTag()])


def test_multiple_allowed_classes():
    """Test with multiple allowed classes including non-container"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    # Все три типа должны быть разрешены
    text_tag = TextTag()
    image_tag = ImageTag()
    string_val = "test"

    lo.append(text_tag)
    lo.append(image_tag)
    lo.append(string_val)

    assert len(lo) == 3
    assert isinstance(lo[0], TextTag)
    assert isinstance(lo[1], ImageTag)
    assert isinstance(lo[2], str)


def test_generator_exhaustion():
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    text_tag = TextTag()
    result1 = lo.validate_access_child(text_tag, 0)
    result2 = lo.validate_access_child(text_tag, 1)

    assert result1 is True
    assert result2 is True


def test_validate_access_child_str_representation():
    """Test error messages include proper string representations"""
    paragraph = ParagraphTag()
    lo = Objects(paragraph, [])

    table_tag = TableTag()

    with pytest.raises(TypeError) as exc_info:
        lo.validate_access_child(table_tag, 0)

    error_msg = str(exc_info.value)
    assert "TableTag" in error_msg
    assert "ParagraphTag" in error_msg
