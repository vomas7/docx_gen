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
from docx.oxml import OxmlElement
from docx.oxml.xmlchemy import BaseOxmlElement

# adder (add_x) - принимает в себя аргументы и записывает их внуть добавляемого элемента add_t(text = 'text') - Добавит внутрь _Text() атрибут text со значение "text"
# Также сам pydocs внутри метакласса формирует у объектов - xml на основе self.append и self.appprevios (::_EtreeXML либы)


# TODO проблема с объектами которые по своей сути включают парграфы в сой объект - такие как пикча и таблица, в списке парграфов они учитываются - ХОТЯ ...
# может и не нужно удалять picture из параграфов потому что параграф это строка по  факту
# todo расклад такой - таблицы это отдельный элемент, который не хранится в параграфе, а вот пикча хранится в параграфе. поэтому я думаю есть смысл не удалять пикчи из списка паранрафов
# но вот делема, мы не можем же хранить в бади и то и то, либо поместить пикчи внутрб параграфа, либо удалять параграфы (но хзхз),
# также можно сделать функцию - предоставляющую доступ ко всем элементам (типа список всех картинок и список всех параграфов и список всех таблиц например)

# todo для картинок сделать метод, который найдёт объект параграфа в которой она находится или лучше сделать проверку на наличие картинки в параграфе

#todo ЭТАП 1
# todo сделать нормльно section и стори саилд для всех елементов и добавить базовый класс +
# TODO создать генератор xml для всех элементов! +
# TODO создать DOCBODY +
# TODO а что если сделать реализацию такой же как и в storyhcild +
# TODO добавить _parent для элементов +
# todo сделать нормальное сохранение файла и чтобы небыло противоречий с текущим файлом и системным дефолтным +
# todo оформить элемент doc +
# todo base элемен и его подбазисы, + убрат чуваков py-docx +
# todo сделать полную перезапись файла word, неважно файл пустой или взятый шаблон +
# todo перерабоать writer'ов. +
# todo отказаться от ридера +     (хотя можно сделать по аналогии с writer - сделать удобный доступ к объектам)
# todo очиста документа +
# todo подправить косячки
# todo создать класс кастомных ошибок
# todo улучшить типы (сделать динамичесскую подставку) + во всём объекте + для других чуваков тоже

#todo ЭТАП 2
#todo создание таблиц


doss = Document()

save_file = os.path.join("abra.docx")
doc = DOC('abra.docx')
body = doc.body
sec1 = body.linked_objects[0]





