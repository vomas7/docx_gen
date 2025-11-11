import os
import sys

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from xml.etree.ElementTree import Element as XmlElement
from docx import Document
from docx.oxml import OxmlElement
from typing import cast
from docx.oxml import CT_Text, CT_P

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
# todo также получится добавить простой способ добавления элементов!

# todo------------
# todo 1 привожу метаклассы атрибутов в порядок +
# todo 2 делаю прикол с секциями - по-факту транслит из нормальной последовательности элементов в нужную и наоборот
# todo 3 создать второй слой абстракции
# todo 4 добавть body и document single-элементы
# todo 5 адаптировать теги как и атрибуты с возможностью переопределения
# todo -----------


from core.doc_objects.paragraph import Paragraph
from core.doc_objects.text import Text
from core.doc_objects.run import Run
from core.doc_objects.section import Section

# p = Paragraph(children=[
#     Text(),
#     Run(),
# ])
# p.children.append(Section())
#
# r = p.to_xml_string()
# print(r)


doc = Document()

# d = doc.add_paragraph()
# _p = d._element
# ppr = _p.get_or_add_pPr()
# ind = ppr.get_or_add_ind()
# ind.left = 6500
# print(ind.left)
# print(d._element.xml)

from doc_objects.attributes import Right, Left, Top

attrs = [
    Right(value=57000),
    Left(),
    Top(value=100000)
]

t = Text(attrs=attrs)
r = Run(children=[t])
p = Paragraph(children=[r])
lef = Left(value=90000000)
t.attrs.append(lef)
t.attrs.pop(0)
t.attrs.pop(0)
print(t.to_xml_string())

l = [Right(value=57000), lef]
t.attrs.extend(l)
print(p.to_xml_string())