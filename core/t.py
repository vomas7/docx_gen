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

# todo проинициализировать кллассы-элементы

# todo добавить enum для существующих тегов

#todo Добавить валидацию по допустимым наследникам и атрибутам
# todo Добавить объекты
# todo Добавить преобразование для секции
# todo определить documentPart через создающийся CT_DOCUMENT

#todo можно добавить MixinValidateAttr MixinValidateTag # а если использовать ленивую загрузку для проверки атрибутов и тегов

#todo затранслейтить коменты


#core.validators.v_objects.ValidationError: Элемент(ы) True не прошл(и) валидацию

from core.doc_objects.paragraph import Paragraph
from core.doc_objects.text import Text
from core.doc_objects.run import Run
from core.doc_objects.section import Section

#todo какая-то ошибка
p = Paragraph(children=[
    Text(),
    Run(),
])

r = p.to_xml_string()
print(r)