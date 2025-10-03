import os
import sys
from types import UnionType
from docx import Document

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)

from core.doc import DOC
from docx.oxml import CT_P, CT_Body, CT_R, CT_Tbl, CT_RPr, CT_SectPr
from core.doc_objects.Section import DOCSection
from core.doc_objects.Paragraph import DOCParagraph
from core.doc_objects.Text import Text
import docx.types as t
from typing import cast
from docx.text.run import Run
from docx.text.paragraph import Paragraph
from docx.parts.story import StoryPart
from docx.oxml.parser import parse_xml

# adder (add_x) - принимает в себя аргументы и записывает их внуть добавляемого элемента add_t(text = 'text') - Добавит внутрь _Text() атрибут text со значение "text"
# Также сам pydocs внутри метакласса формирует у объектов - xml на основе self.append и self.appprevios (::_EtreeXML либы)


#TODO создать генератор xml для всех элементов!
#TODO создать DOCBODY
#TODO а что если сделать реализацию такой же как и в storyhcild
#TODO добавить _parent для элементов
#TODO проблема с объектами которые по своей сути включают парграфы в сой объект - такие как пикча и таблица, в списке парграфов они учитываются - ХОТЯ ...
# может и не нужно удалять picture из параграфов потому что параграф это строка по  факту
#todo расклад такой - таблицы это отдельный элемент, который не хранится в параграфе, а вот пикча хранится в параграфе. поэтому я думаю есть смысл не удалять пикчи из списка паранрафов
# но вот делема, мы не можем же хранить в бади и то и то, либо поместить пикчи внутрб параграфа, либо удалять параграфы (но хзхз),
# также можно сделать функцию - предоставляющую доступ ко всем элементам (типа список всех картинок и список всех параграфов и список всех таблиц например)

#todo для картинок сделать метод, который найдёт объект параграфа в которой она находится или лучше сделать проверку на наличие картинки в параграфе

#todo сделать нормльно section и стори саилд для всех елементов и добавить базовый класс


doss = Document()
section = doss.add_section()

doc = DOCSection(section)

print(doc.linked_objects)














# class Base:
#
#     @staticmethod
#     def validate_annotation(obj, **kwargs):
#         """
#             args:
#                 obj: class instance
#                 **kwargs: key-value pairs for checking received arguments
#         """
#         if not kwargs:
#             raise ValueError("arguments are required")
#         annotation = obj.__init__.__annotations__
#
#         for key, value in kwargs.items():
#             if key not in annotation:
#                 continue
#
#             if not type(value) in (annotation[key]):
#                 raise AttributeError(
#                     f"Creating Text object failed: "
#                     f"Unknown source {type(value)}!"
#                 )
#
#
# class Any:
#     def __init__(self, abra):
#         self.abra = abra
#
# from typing import List, Iterable
#
# class MySection(Base, Any):
#
#     def __init__(self, section: Iterable[int]):
#         print(section)
#         Base.validate_annotation(self, section=section)
#         self.section = section
#         Any.__init__(self, "111")
#
#
# se = MySection(section=[12,])
#
# print(se.section)




# fff = Document(r'C:\Users\AkentevDV\Desktop\пара\rename.docx')
#
# all_elem = fff._element.body.getchildren()
#
# sec_elem = []
# sub_sect = []
# for elem in all_elem:
#     if isinstance(elem, CT_SectPr):
#         sec_elem.append(DOCSection(elem))



# sections = map(lambda x: x, fff._element.sectPr_lst)
# print(next(sections))


# print(all_ellem.index(next(sections)))

#xpath('./w:p/w:r/w:drawing')
# print(list(map(lambda x: x._sectPr, fff.sections)))

# print(fff._element.body.getchildren())
# print(list(map(lambda x: x.text, lst_p)))
# print(fff.inline_shapes._inline_lst)


# cast_doc = DOC()

# print(    cast_doc._element.sectPr_lst)




