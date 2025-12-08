import dataclasses

from typing import List, FrozenSet, Type
from core.ui_objects.base import BaseDocx
from core.oxml_magic.parser import OxmlElement
from core.ui_objects.base import BaseContainerDocx
from core.ui_objects.base import BaseNonContainerDocx



# from dataclasses import asdict
# @dataclasses.dataclass
# class BreakAttributes:
#     type: str
#     clear: str
#
# class Break(BaseContainerDocx, BreakAttributes):
#     def __init__(self): super().__init__(si_element=OxmlElement("w:br"))
#
#     # @property
#     # def type(self):
#     #     return self.type
#     #
#     # @type.setter
#     # def type(self, new_type: str | int):
#
#
#
# # class Breaks:
# #     LINE = (None, None)
# #     PAGE = ("page", None)
# #     COLUMN = ("column", None)
# #     LINE_CLEAR_LEFT = ("textWrapping", "left")
# #     LINE_CLEAR_RIGHT = ("textWrapping", "right")
# #     LINE_CLEAR_ALL = ("textWrapping", "all"),
# #
#
# # class RunStyle:
# #     type: Breaks
# #
#
# class Run:
#
#     ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({Text, Break})
#     type_: str
#     attrs: {}
#     #
#     def __init__(self):
#         self.attrs = {"hyu": "pizda"}
#
# RUN = "r"
#
# d = {Run: 'r'}
#
# print(d.get(Run))
#     # @property
#     # def type_(self):
#     #     return self.type_
#     #
#     # @type_.setter
#     # def type_(self, new_type: str):
#     #     self.attrs[f'w:{self.type_.__name__[:1]}']
#     #     self.type_ = new_type
#     #
#     #
#     # def add_page_break(self):
#     #     """Insert break with type PAGE"""
#     #     break_ = Break(Breaks.PAGE[0])
#     #     self.linked_objects.append(break_)
#     #
#     # def add_column_break(self):
#     #
#
#
#
# # r = Run("DSFDFS")
# # r.add_page_break()
#
#
# class Paragraph(BaseContainerDocx):
#
#     # todo нет проверки на отсутсвие текста, поэтому может создать ненужные ran и text
#     def __init__(self, linked_objects: List[BaseDocx] = None, text: str = ''):
#         super().__init__(
#             si_element=OxmlElement("w:p"),
#             linked_objects=linked_objects
#         )
#         self.add(Run(linked_objects=[Text(text)]))
#
#     def add_run(self, text: str | None = None):
#         self.add(Run(text))
#
#
# a = Run()
#
#
#
# #
# # for elem in linked_objects:
# #     issubclass(elem, BaseDocx)
# #     attributes = elem.attrs
# #     xml = f'<w:{elem.tag} w:type={str(elem.type_)}>'