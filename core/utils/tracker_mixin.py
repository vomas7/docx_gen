from typing import Set, Dict, Type, Union, List, Any



class MetaRegister(type):
    _registry: Dict[str, Any] = {}

    def __new__(mcls, clsname, clsbases, namespace):
        cls = super().__new__(mcls, clsname, clsbases, namespace)
        mcls._registry[clsname] = cls
        setattr(cls, '_registry', cls._registry)
        return cls



# # === Реестр для отложенного разрешения строковых ссылок ===
# class Registry:
#     elements: Dict[str, Type['BaseMarkupElement']] = {}
#     attributes: Dict[str, Type['BaseAttributeElement']] = {}
#
#     @classmethod
#     def register_element(cls, klass):
#         cls.elements[klass.__name__] = klass
#
#     @classmethod
#     def register_attribute(cls, klass):
#         cls.attributes[klass.__name__] = klass
#
#     @classmethod
#     def resolve(cls, name: str):
#         return cls.elements.get(name) or cls.attributes.get(name)
#
#
# # === Базовые классы ===
# class BaseAttributeElement:
#     def __init_subclass__(cls, **kwargs):
#         super().__init_subclass__(**kwargs)
#         Registry.register_attribute(cls)
#
#     def __init__(self, name: str, value: str):
#         self.name = name
#         self.value = value
#
#
# class BaseMarkupElement:
#     REQUIRED_ATTRIBUTES: Set[Union[str, Type[BaseAttributeElement]]] = set()
#     ACCESS_ATTRIBUTES: Set[Union[str, Type[BaseAttributeElement]]] = set()
#
#     def __init_subclass__(cls, **kwargs):
#         super().__init_subclass__(**kwargs)
#         Registry.register_element(cls)
#
#     def __init__(self):
#         self.attributes: List[BaseAttributeElement] = []
#
#     def add_attribute(self, attr: BaseAttributeElement):
#         if type(attr) in self._resolve_set(self.ACCESS_ATTRIBUTES):
#             self.attributes.append(attr)
#         else:
#             raise ValueError(f"Attribute {type(attr).__name__} not allowed for {type(self).__name__}")
#
#     def _resolve_set(self, raw: Set[Union[str, Type]]):
#         resolved = set()
#         for item in raw:
#             if isinstance(item, str):
#                 resolved_class = Registry.resolve(item)
#                 if resolved_class:
#                     resolved.add(resolved_class)
#             else:
#                 resolved.add(item)
#         return resolved
#
#
# class BaseNonContainElement(BaseMarkupElement):
#     def __init__(self):
#         super().__init__()
#
#
# class BaseContainElement(BaseMarkupElement):
#     ACCESS_CHILDREN: Set[Union[str, Type['BaseMarkupElement']]] = set()
#     REQUIRED_CHILDREN: Set[Union[str, Type['BaseMarkupElement']]] = set()
#
#     def __init__(self):
#         super().__init__()
#         self.children: List[BaseMarkupElement] = []
#
#     def add_child(self, child: 'BaseMarkupElement'):
#         if type(child) in self._resolve_set(self.ACCESS_CHILDREN):
#             self.children.append(child)
#         else:
#             raise ValueError(f"Child {type(child).__name__} not allowed in {type(self).__name__}")
#
#
# # === Атрибуты ===
# class Bold(BaseAttributeElement):
#     pass
#
# class Italic(BaseAttributeElement):
#     pass
#
# # === Элементы ===
# class Text(BaseNonContainElement):
#     ACCESS_ATTRIBUTES = {"Bold", "Italic"}
#
# class Run(BaseContainElement):
#     ACCESS_CHILDREN = {"Text"}
#     ACCESS_ATTRIBUTES = {"Bold"}
#
# class Paragraph(BaseContainElement):
#     ACCESS_CHILDREN = {"Run"}
#     REQUIRED_ATTRIBUTES = set()
#
#
# # === Пример использования ===
# p = Paragraph()
# r = Run()
# t = Text()
# t.add_attribute(Bold("bold", "true"))
# r.add_child(t)
# p.add_child(r)
#
# print(f"Paragraph has {len(p.children)} children (e.g., Run)")