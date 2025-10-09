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



#TODO проблема с объектами которые по своей сути включают парграфы в сой объект - такие как пикча и таблица, в списке парграфов они учитываются - ХОТЯ ...
# может и не нужно удалять picture из параграфов потому что параграф это строка по  факту
#todo расклад такой - таблицы это отдельный элемент, который не хранится в параграфе, а вот пикча хранится в параграфе. поэтому я думаю есть смысл не удалять пикчи из списка паранрафов
# но вот делема, мы не можем же хранить в бади и то и то, либо поместить пикчи внутрб параграфа, либо удалять параграфы (но хзхз),
# также можно сделать функцию - предоставляющую доступ ко всем элементам (типа список всех картинок и список всех параграфов и список всех таблиц например)

#todo для картинок сделать метод, который найдёт объект параграфа в которой она находится или лучше сделать проверку на наличие картинки в параграфе



#todo сделать нормльно section и стори саилд для всех елементов и добавить базовый класс +
#TODO создать генератор xml для всех элементов! +
#TODO создать DOCBODY +
#TODO а что если сделать реализацию такой же как и в storyhcild +
#TODO добавить _parent для элементов +
#todo сделать нормальное сохранение файла и чтобы небыло противоречий с текущим файлом и системным дефолтным +
#todo оформить элемент doc +
#todo base элемен и его подбазисы, + убрат чуваков py-docx +
#todo сделать полную перезапись файла word, неважно файл пустой или взятый шаблон +
#todo перерабоать writer'ов.
# Идея в том чтобы без заморочек записыывать оъекты непосредственно в документ  (сам определяет создавать ему сопутствующие элементы или использовать стандартные) insert_linked_object  более низкоуровненвая тема
#todo подправить косячки

doss = Document()
section = doss.add_section()



# docx = DOC()


# print(doc.linked_objects)

save_file = os.path.join("abra.docx")
# print(type(save_file))
# print(save_file)
doc = DOC('abra.docx')
doc._clear_document_part()
sec1 = DOCSection(section)
body = doc.body
sec2 = DOCSection()
# doc.writer.add_paragraph()
text = Text("nEwYourc\n\t")
par = DOCParagraph(text)
sec = body.linked_objects[0]
sec.insert_linked_object(par)
body.insert_linked_object(sec1)
doc.export.to_docx(save_file)



