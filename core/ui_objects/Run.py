# from enum import Enum
# from core.ui_objects.Break import Break
# from core.ui_objects.base.BaseAttribute import EnumAttribute
# from core.ui_objects.base.BaseAttribute import BooleanAttribute
from core.ui_objects.Text import Text
from core.ui_objects.Break import Break
from core.ui_objects.base.BaseContainerTag import BaseContainerTag
from core.ui_objects.base.LinkedObjects import LinkedObjects


# class Bold(BooleanAttribute):
#
#     def __init__(self, xml_name: str, value):
#         super().__init__(xml_name, value)


# class Italic(BooleanAttribute):
#     def __init__(self, xml_name: str, value):
#         super().__init__(xml_name, value)


# class Underline(EnumAttribute):
#     class Options(Enum):


class Run(BaseContainerTag):

    __slots__ = ("_bold", )

    def __init__(self, linked_objects: LinkedObjects | list = None):
        super().__init__(linked_objects)

    @property
    def tag(self):
        return "w:r"

    @property
    def access_children(self):
        return {Break, Text}

    def add_page_break(self):
        self.add(Break(type='page'))

    def add_column_break(self):
        self.add(Break(type='column'))

    def add_picture(self):
        raise NotImplemented

    def add_table(self):
        raise NotImplemented

    def add_text(self, text: Text | str):
        self.add(Text(text))
