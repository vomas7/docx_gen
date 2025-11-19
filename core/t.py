import os
import sys

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)
#
# # todo аналог pydocx
#
# # todo создать элементы - аналогичние CT_*, отличие в том что нет наследия от BaseOxmlMeta.
# # Логика pydocx заключается в том чтобы  добавлять элементы непосредственно в код XML,
# # а поскольку мы работаем с чистыми объектами python, возможность изменения XML - будет узким горлышком.
# # отриисовка будет производиться в конце программы. создавая xml код
#
# # todo МЫСЛЯ мы Добавляем на абстрактный уровень доп ирерахию для рабыты с элементами в том предсталении, в котором нам это нужно. Потому что на уровне с xml, правила будут противоречить друг другу, поэтомы так мы обходим структуру xml'я
#
# # todo ИДЕЯ, создать метакласс для автоматической генрации необходимых пациков (как атрибутов так и тэгов)
# # todo значит нужен ещё один слой обстакции. т.к чтобы добавить стиль для элемента, придётся создавать несколько объкутов внутри него например p нужен pPr и Marg и т.п
# # todo также получится добавить простой способ добавления элементов! в общем он нужен и для упрощённой последовательности элементов
#
# # todo главное чтобы метаклассы тегов не переопределяли передающие в него какие-либо элементы!
# # todo------------
# # todo 1 привожу метаклассы атрибутов в порядок +
# # todo 2 делаю прикол с секциями - по-факту транслит из нормальной последовательности элементов в нужную и наоборот +
# # todo 3 создать второй слой абстракции +
# # todo 4 реализовать логику ридера +
# # todo 5 добавть body и document single-элементы +
# # todo 6 создать метакласс для автоматической генрации необходимых пациков (атрибуты) +
# # todo 7 создать метакласс для автоматической генрации необходимых пациков (тэги)
# # todo 8 проинициализировать их в lxml
# # todo 9 определить documentPart через создающийся CT_DOCUMENT. Настроить flow открытия документа
# # todo 10 Доремонтировать секции
# # todo 11 перенести простые элементы
# # todo 12 Настроить экспортёр
# # todo 13 перенести все элементы
# # todo ... добавить enum'ы для всех тегов
# # todo -----------
# # todo для стайлера релизовать во первых его как отдельный объект, у каждого верхоуровнего элемента как атрибут и можно обращаться parahraph.style.align = center
# # todo некоторые параметры styler'а могут иметь отдельные классы или енумы, в целом продумать этот моментик. чтобы пользователю было понятно каке атрибуты и параметры он может туда херачить. например у align есть 4 параметра

#
#
# # from docx import Document
# # from docx.enum.section import WD_HEADER_FOOTER_INDEX
# # from docx.oxml import CT_HdrFtr, CT_HdrFtrRef
#
#
# # doc = Document()
# #
# # s = doc.sections[0]
# # s._sectPr.add_footerReference(WD_HEADER_FOOTER_INDEX.EVEN_PAGE, "11111111")
# # ref = s._sectPr.get_footerReference(WD_HEADER_FOOTER_INDEX.EVEN_PAGE)
# #
# # print(
# #     ref
# # )
#
# #===========
#
# from core.ui_objects.api import Document
# from docx import Document
# from docx.oxml import CT_P
# from core.ui_objects.paragraph import Paragraph
# from core.ui_objects.section import Section
#
# #
# p = Paragraph()
# p2 = Paragraph(linked_objects=[p])
#
# #
# sec = Section(linked_objects=[p2])
# p.linked_objects.append()
# p3 = Paragraph(linked_objects=[sec])
# # print(p3.to_SI_element().to_xml_string())
# # print(p3.to_SI_element().to_xml_string())
# # print(p3.to_SI_element().to_xml_string())
#
#
# # doc = Document()
#
# # doc.body.to_SI_element().to_xml_string()
#
#
#
#
# from typing import TYPE_CHECKING
# from core.doc_objects.paragraph import SI_Paragraph
# from core.doc_objects.section import SI_SectPr
# from core.doc_objects.text import SI_Text
#
# import sys
#
# import time
# import importlib
#
#
# start = time.time()
# #todo реализовать файл со всеми тегами (импорт онных) + реализовтаь сериализацию строковых классов
#
# print(globals().get("__name__"))
#
#
#
#
#
#
# print(time.time() - start)
#
#


# from core.doc_objects.tags import pgMarg
# from core.doc_objects.paragraph import SI_Paragraph
#
# pg = pgMarg()
# print(
#     pg.REQUIRED_ATTRIBUTES,
#     pg.ACCESS_ATTRIBUTES,
#     pg.ACCESS_CHILDREN,
#     pg.REQUIRED_CHILDREN
#
# )
#
# print(pg)
# print(SI_Paragraph)
# print(pg.tag)
fff = 1

print(getattr(__name__, "fff"))
