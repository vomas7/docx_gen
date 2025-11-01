#todo in the near future
# проблема в метаклассах, а именно в неунификации классов для метакласса + проблема с access и req атрибутами, проблема в последовательном использовании. но один из варантов:
# @classmethod
#     def _resolve_class_references(cls, class_set):
#         resolved = set()
#         for item in class_set:
#             if isinstance(item, str):
#                 # Ищем класс в текущем модуле
#                 import sys
#                 current_module = sys.modules[__name__]
#                 resolved_class = getattr(current_module, item, None)
#                 if resolved_class:
#                     resolved.add(resolved_class)
#             else:
#                 resolved.add(item)
#         return resolved

# from core.doc_objects.base import BaseMurkupElement, BaseContainElement, BaseNonContainElement
# from typing import Any, Set, Type
#
# # class MetaTagsElement(type):
# #     """
# #                 Initializes __init__ for each Tag class.
# #                 Restricts  | __required_attributes | attributes for class
# #                 and parent | __required_bases |
# #     """
# #
# #     __required_bases = (BaseMurkupElement,)
# #     __required_attributes = ("tag",)
# #
# #     # def __new__(cls, cls_name, bases, namespace):
# #     #     # super().__init__(cls_name, bases, namespace)
# #     #     # _original_init = getattr(cls, '__init__', None)
# #     #     # _check_bases = all(issubclass(cls, b) for b in cls.__required_bases)
# #     #     # _check_attr = all(a in namespace for a in cls.__required_attributes)
# #     #     # if not _check_bases:
# #     #     #     raise TypeError(
# #     #     #         f"Class must be a subclass of {cls.__required_bases}"
# #     #     #     )
# #     #     # if not _check_attr:
# #     #     #     raise TypeError(
# #     #     #         f"Class must contain a required attributes "
# #     #     #         f"{cls.__required_attributes}"
# #     #     #     )
# #     #
# #     #     tag = getattr(cls, "tag", None)
# #     #     def _init(self, *args, **kwargs):
# #     #         super(cls, self).__init__(tag=tag, *args, **kwargs)
# #     #
# #     #     # cls.__init__ = _original_init or _init
# #     #     namespace["__init__"] = _init
# #     #     return super().__new__(cls, cls_name, bases, namespace)
#
# class Run(BaseContainElement):
#     # ACCESS_CHILDREN: Set[Type[BaseMurkupElement]] = {}
#     # REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = {}
#     # ACCESS_ATTRIBUTES: Set[...] = set()
#     # REQUIRED_ATTRIBUTES: Set[...] = set()
#
#     tag = "w:r"
#
#
# class Text(BaseNonContainElement):
#     # ACCESS_CHILDREN: Set[Type[BaseMurkupElement]] = {}
#     # REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = {}
#     # ACCESS_ATTRIBUTES: Set[...] = set()
#     # REQUIRED_ATTRIBUTES: Set[...] = set()
#
#     tag = "w:t"
#
# class Paragraph(BaseContainElement):
#     ACCESS_CHILDREN: Set[Type[BaseMurkupElement]] = {Text, Run, }
#     REQUIRED_CHILDREN: Set[Type[BaseMurkupElement]] = {Run, }
#     ACCESS_ATTRIBUTES: Set[...] = set()
#     REQUIRED_ATTRIBUTES: Set[...] = set()
#
#     tag = "w:p"
