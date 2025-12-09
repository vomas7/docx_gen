import os
import sys

# from core.ui_objects import Run

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)


#todo возможно стоит подумать как сделать мроще для понимания сборку элементов и без сборки si_
#todo короче нужно подумать как изначально принимать si_document или перевести blob в норм тему





# from core.ui_objects.api import Document
# from core.ui_objects.paragraph import Paragraph
#
# doc = Document("wiebano.docx")
#
#
# body = doc.body
#
# body.add(Paragraph(text='hello world'))
# doc.save("wiebano.docx")

from core.oxml_magic.register_tag import get_cls_by_tag
from core.ui_objects import base
from core.oxml_magic.parser import make_xml_tree, to_xml_str, convert_xml_to_cls
from core.ui_objects.paragraph import Paragraph, Run, Text


from docx import Document

elem= Document()._element.body

print(convert_xml_to_cls(elem))