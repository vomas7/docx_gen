import pytest
from unittest.mock import Mock
from core.ui_objects.base.LinkedObjects import LinkedObjects


class BaseContainerTag:
    @property
    def allowed_children(self):
        raise NotImplementedError


class TextTag(BaseContainerTag):
    @property
    def allowed_children(self):
        return ()

    @property
    def tag(self):
        return "w:t"


class ImageTag(BaseContainerTag):
    @property
    def allowed_children(self):
        return ()

    @property
    def tag(self):
        return "w:drawing"


class ParagraphTag(BaseContainerTag):
    @property
    def allowed_children(self):
        return (TextTag, ImageTag)

    @property
    def tag(self):
        return "w:p"


class TableTag(BaseContainerTag):
    @property
    def allowed_children(self):
        return ()

    @property
    def tag(self):
        return "w:tbl"


def test_linked_objects_initialization():
    """Test basic initialization with linked_parent"""
    parent = Mock(spec=BaseContainerTag)
    parent.__class__.__name__ = 'TestParent'

    lo = LinkedObjects(parent, [1, 2, 3])

    assert lo.linked_parent == parent
    assert len(lo) == 3
    assert lo[0] == 1
    assert lo[1] == 2
    assert lo[2] == 3


def test_linked_objects_with_container_tags():
    """Test with actual container tags"""
    paragraph = ParagraphTag()

    lo = LinkedObjects(paragraph, [])

    assert lo.linked_parent == paragraph
    assert lo.linked_parent.allowed_children == (TextTag, ImageTag)


def test_validate_access_child_allowed():
    """Test validation with allowed child"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    # TextTag должен быть разрешен для Paragraph
    try:
        lo.validate_access_child(text_tag)
    except TypeError:
        pytest.fail("TextTag should be allowed for Paragraph")


def test_validate_access_child_prohibited():
    """Test validation with prohibited child"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    # TableTag НЕ должен быть разрешен для Paragraph
    with pytest.raises(TypeError) as exc_info:
        lo.validate_access_child(table_tag)

    assert "It is prohibited to add" in str(exc_info.value)
    assert "TableTag" in str(exc_info.value)
    assert "ParagraphTag" in str(exc_info.value)


def test_append_with_validation():
    """Test that append validates before adding"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    # Append должен работать для разрешенного тега
    lo.append(text_tag)
    assert len(lo) == 1
    assert lo[0] == text_tag

    # Append должен вызывать ошибку для запрещенного тега
    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    with pytest.raises(TypeError):
        lo.append(table_tag)

    # Проверяем, что запрещенный тег не был добавлен
    assert len(lo) == 1  # Все еще только text_tag


def test_insert_with_validation():
    """Test that insert validates before adding"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, ['item1', 'item3'])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    # Insert должен работать для разрешенного тега
    lo.insert(1, text_tag)
    assert len(lo) == 3
    assert lo[0] == 'item1'
    assert lo[1] == text_tag
    assert lo[2] == 'item3'

    # Insert должен вызывать ошибку для запрещенного тега
    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    with pytest.raises(TypeError):
        lo.insert(0, table_tag)

    # Проверяем, что запрещенный тег не был добавлен
    assert len(lo) == 3  # Оригинальные 2 + text_tag


def test_extend_with_list_validation():
    """Test that extend validates list items"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    image_tag = Mock(spec=ImageTag)
    image_tag.__class__.__name__ = 'ImageTag'

    # Extend должен работать для разрешенных тегов
    lo.extend([text_tag, image_tag])
    assert len(lo) == 2
    assert lo[0] == text_tag
    assert lo[1] == image_tag


def test_extend_with_mixed_list():
    """Test extend with mixed allowed/prohibited items"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    image_tag = Mock(spec=ImageTag)
    image_tag.__class__.__name__ = 'ImageTag'

    # Extend должен вызвать ошибку при первом запрещенном элементе
    with pytest.raises(TypeError):
        lo.extend([text_tag, table_tag, image_tag])

    # Проверяем, что ничего не было добавлено
    assert len(lo) == 0


def test_extend_with_linked_objects():
    """Test extend with another LinkedObjects"""
    paragraph = ParagraphTag()
    lo1 = LinkedObjects(paragraph, [])
    lo2 = LinkedObjects(paragraph, [])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    lo2.append(text_tag)

    # Extend с другим LinkedObjects должен работать
    lo1.extend(lo2)
    assert len(lo1) == 1
    assert lo1[0] == text_tag


def test_setitem_with_validation():
    """Test that __setitem__ validates"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, ['old1', 'old2'])

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    # Замена разрешенным тегом
    lo[0] = text_tag
    assert lo[0] == text_tag
    assert lo[1] == 'old2'

    # Замена запрещенным тегом
    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    with pytest.raises(TypeError):
        lo[1] = table_tag

    # Проверяем, что запрещенный тег не заменил элемент
    assert lo[1] == 'old2'


def test_initialization_validation():
    """Test that initialization validates items"""
    paragraph = ParagraphTag()

    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'

    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    # Инициализация с разрешенным тегом - должно работать
    lo1 = LinkedObjects(paragraph, [text_tag])
    assert len(lo1) == 1

    # Инициализация с запрещенным тегом - должна вызывать ошибку
    # Но! Твой текущий код сначала добавляет через super().__init__(initlist)
    # а потом валидирует. Это может привести к тому, что элемент добавится,
    # а потом вызовется исключение.
    try:
        lo2 = LinkedObjects(paragraph, [table_tag])
        # Если мы здесь, значит ошибка не возникла
        # Но в реальности она должна возникнуть в validate_access_children
        pytest.fail("Should have raised TypeError")
    except TypeError:
        # Это ожидаемое поведение
        pass


def test_empty_allowed_children():
    """Test when parent has no allowed children"""
    text = TextTag()
    lo = LinkedObjects(text, [])

    # TextTag не должен принимать никакие контейнерные теги
    another_text = Mock(spec=TextTag)
    another_text.__class__.__name__ = 'TextTag'

    with pytest.raises(TypeError):
        lo.validate_access_child(another_text)


def test_none_item_validation():
    """Test validation with None item"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    # None не должен вызывать ошибку
    try:
        lo.validate_access_child(None)
    except Exception as e:
        pytest.fail(f"None should not raise error: {e}")


def test_non_container_tag_validation():
    """Test validation with non-container item"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    # Обычный объект (не BaseContainerTag)
    regular_obj = Mock()
    regular_obj.__class__.__name__ = 'RegularObject'

    # Должен вызывать TypeError в isinstance(item, BaseContainerTag)
    # Но твой код проверяет это условие
    with pytest.raises(TypeError):
        lo.validate_access_child(regular_obj)


def test_real_scenario_paragraph_children():
    """Test real scenario: paragraph containing text and image"""
    paragraph = ParagraphTag()
    lo = LinkedObjects(paragraph, [])

    # Добавляем текст
    text_tag = Mock(spec=TextTag)
    text_tag.__class__.__name__ = 'TextTag'
    lo.append(text_tag)

    # Добавляем изображение
    image_tag = Mock(spec=ImageTag)
    image_tag.__class__.__name__ = 'ImageTag'
    lo.append(image_tag)

    # Проверяем содержимое
    assert len(lo) == 2
    assert isinstance(lo[0], Mock) and lo[0].__class__.__name__ == 'TextTag'
    assert isinstance(lo[1], Mock) and lo[1].__class__.__name__ == 'ImageTag'

    # Пытаемся добавить таблицу - должно быть запрещено
    table_tag = Mock(spec=TableTag)
    table_tag.__class__.__name__ = 'TableTag'

    with pytest.raises(TypeError) as exc_info:
        lo.append(table_tag)

    assert "TableTag" in str(exc_info.value)
    assert "ParagraphTag" in str(exc_info.value)
