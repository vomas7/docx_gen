import os
import sys

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)



# todo создать элементы - аналогичние CT_*, отличие в том что нет наследия от BaseOxmlMeta.
# Логика pydocx заключается в том чтобы  добавлять элементы непосредственно в код XML,
# а поскольку мы работаем с чистыми объектами python, возможность изменения XML - будет узким горлышком.
# отриисовка будет производиться в конце программы. создавая xml код


# todo ИДЕЯ, создать метакласс для автоматической генрации необходимых пациков (как атрибутов так и тэгов)
# todo добавить остальные элементы ворда
# todo добавить enum для существующих тегов

# todo определить documentPart через создающийся CT_DOCUMENT


# todo Backlog: Добавить все эти элементы
# todo Backlog: Добавить функции под эти элементы на более высоком уровне


# todo значит нужен ещё один слой обстакции. т.к чтобы добавить стиль для элемента, придётся создавать несколько объкутов внутри него например p нужен pPr и Marg и т.п
# todo также получится добавить простой способ добавления элементов! в общем он нужен и для упрощённой последовательности элементов

# todo------------
# todo 1 привожу метаклассы атрибутов в порядок +
# todo 2 делаю прикол с секциями - по-факту транслит из нормальной последовательности элементов в нужную и наоборот
# todo 3 создать второй слой абстракции
# todo 4 добавть body и document single-элементы
# todo 5 адаптировать теги как и атрибуты с возможностью переопределения
# todo -----------
# todo аналог pydocx

#todo МЫСЛЯ мы Добавляем на абстрактный уровень доп ирерахию для рабыты с элементами в том предсталении, в котором нам это нужно. Потому что на уровне с xml, правила будут противоречить друг другу, поэтомы так мы обходим структуру xml'я


from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.text import SI_Text
from core.doc_objects.run import SI_Run
from core.doc_objects.section import SI_Section
from docx.text.paragraph import Paragraph
from docx import Document
from doc_objects.attributes import AT_Right, AT_Left, AT_Top

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from xml.etree.ElementTree import Element as XmlElement
from docx.oxml import OxmlElement
from typing import cast
from docx.oxml import CT_Text, CT_P


# p = Paragraph(children=[
#     Text(),
#     Run(),
# ])
# p.children.append(Section())
#
# r = p.to_xml_string()
# print(r)



# d = doc.add_paragraph()
# _p = d._element
# ppr = _p.get_or_add_pPr()
# ind = ppr.get_or_add_ind()
# ind.left = 6500
# print(ind.left)
# print(d._element.xml)


# attrs = [
#     AT_Right(value=57000),
#     AT_Left(),
#     AT_Top(value=100000)
# ]
#
# t = SI_Text(attrs=attrs)
# r = SI_Run(children=[t])
# p = SI_Paragraph(children=[r])
# lef = AT_Left(value=90000000)
# t.attrs.append(lef)
# t.attrs.pop(0)
# t.attrs.pop(0)
# print(t.to_xml_string())
#
# l = [AT_Right(value=57000), lef]
# t.attrs.extend(l)
# print(p.to_xml_string())


from core.ui_objects.paragraph import Paragraph


p = Paragraph()
from docx import Document
d = Document()
# link = [Paragraph(), Paragraph()]
# p1 = Paragraph(linked_objects=link)

#
# for obj in p1._linked_objects:
#     print(obj.parent)
