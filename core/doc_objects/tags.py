from core.doc_objects.base import (
    BaseContainElement,
    BaseNonContainElement,
    BaseTagElement
)

# todo придумать как автоматически генерировать обязательные атрибуты (скорее всего просто добавить сторонний метод для middleware списка)


from typing import Type



# todo придумать как завести и адаптировать для атрибутов бляяяяяяяяяяяяяяяяяя
# todo не забыть про базовую иницилизацию
# todo как вариант сделать ещё один метакласс, котторый занимается отслеживанием элементов. тогда скорее всего понвдобится самый высокий базовый элемент.



def tag_factory(
        tag_name,
        is_container,
        **kwargs
) -> Type[BaseTagElement]:
    """
    Factory of attributes, returns a class with <tag_name> class name without prefix <w:>
    """
    _class_name = tag_name.replace('w:', 'SI_')
    _ParentCls = BaseContainElement if is_container else BaseNonContainElement

    class_attrs = {
        '__name__': _class_name,
        '__qualname__': _class_name,
        '__module__': __name__,
    }
    class_attrs.update(kwargs)

    if is_container:
        def __init__(self, attrs=None, children=None):
            super(type(self), self).__init__(tag_name, attrs, children)

    else:
        def __init__(self, attrs=None):
            super(type(self), self).__init__(tag_name, attrs)

    class_attrs['__init__'] = __init__

    TagClass = type(_class_name, (_ParentCls,), class_attrs)

    return TagClass
