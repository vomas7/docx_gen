import os
import sys

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)


# todo аналог pydocx

# todo создать элементы - аналогичние CT_*, отличие в том что нет наследия от BaseOxmlMeta.
# Логика pydocx заключается в том чтобы  добавлять элементы непосредственно в код XML,
# а поскольку мы работаем с чистыми объектами python, возможность изменения XML - будет узким горлышком.
# отриисовка будет производиться в конце программы. создавая xml код

#todo МЫСЛЯ мы Добавляем на абстрактный уровень доп ирерахию для рабыты с элементами в том предсталении, в котором нам это нужно. Потому что на уровне с xml, правила будут противоречить друг другу, поэтомы так мы обходим структуру xml'я

# todo ИДЕЯ, создать метакласс для автоматической генрации необходимых пациков (как атрибутов так и тэгов)
# todo значит нужен ещё один слой обстакции. т.к чтобы добавить стиль для элемента, придётся создавать несколько объкутов внутри него например p нужен pPr и Marg и т.п
# todo также получится добавить простой способ добавления элементов! в общем он нужен и для упрощённой последовательности элементов



# todo------------
# todo 1 привожу метаклассы атрибутов в порядок +
# todo 2 делаю прикол с секциями - по-факту транслит из нормальной последовательности элементов в нужную и наоборот +
# todo 3 создать второй слой абстракции +
# todo 4 добавть body и document single-элементы
# todo определить documentPart через создающийся CT_DOCUMENT
# todo 5 Доремонтировать секции
# todo 6 создать метакласс для автоматической генрации необходимых пациков (как атрибутов так и тэгов)
# todo 7 перенести простые элементы
# todo ... добавить enum'ы для всех тегов
# todo -----------



from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.text import SI_Text
from core.doc_objects.run import SI_Run
from core.doc_objects.section import SI_SectPr
from docx.text.paragraph import Paragraph
from docx import Document
from doc_objects.attributes import AT_Right, AT_Left, AT_Top

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional
from xml.etree.ElementTree import Element as XmlElement
from docx.oxml import OxmlElement
from typing import cast
from docx.oxml import CT_Text, CT_P
from docx import Document





from core.ui_objects.paragraph import Paragraph
from core.ui_objects.section import Section


p = Paragraph()

p2= Paragraph()
p.linked_objects.append(p2)
#p/p2

s = Section([p])
#s/p/p2

any_p = Paragraph()

any_p.linked_objects.append(s)
#p/s/p/p2
s_si = s._to_SI_element()

print(any_p.to_SI_element().to_xml_string())