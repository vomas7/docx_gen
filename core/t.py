import os
import sys
from types import UnionType

current_path = os.getcwd()
root_path = os.path.abspath(os.path.join(current_path, ".."))
sys.path.append(root_path)

from core.doc import DOC
from core.doc_objects.Section import DOCSection
from core.doc_objects.Paragraph import DOCParagraph
from core.doc_objects.Text import Text
from docx.text.run import Run
from docx.text.paragraph import Paragraph
from docx.parts.story import StoryPart

# adder (add_x) - принимает в себя аргументы и записывает их внуть добавляемого элемента add_t(text = 'text') - Добавит внутрь _Text() атрибут text со значение "text"
# Также сам pydocs внутри метакласса формирует у объектов - xml на основе self.append и self.appprevios (::_EtreeXML либы)


#TODO создать генератор xml для всех элементов!

#TODO проблема заключается в том, что мы не не можем добавлять свои объекты в итоговый документ, по-факту происходит изменение текстов и стилей существующих.
#TODO т.е из-за того что не создаются собственные элементы, не получается добавлять их в документ иерархически - путается порядок и нужно коньролировать каждый объект на его добавление.

cast_doc = DOC()


t1=Text("text")
t2=Text()

p1 = DOCParagraph(t1)
p2 = DOCParagraph(t2)

cast_doc.writer.add_paragraph(p1)
cast_doc.writer.add_paragraph(p2)
print(p1._element.xml)

# print(cast_doc._element.xml)




# p = cast_doc.add_paragraph("ffff")
# run = Text("some1\n\tdfdfdf")
#
# par1 = DOCParagraph(p)

# print(par1._element.xml)





# print([se.start_type for se in sections])
# print(cast_doc._body._element.xml)
# cast_doc.save("test.docx")








# ('_pgMar', <class 'docx.oxml.section.CT_PageMar'>), ('_pgSz', <class 'docx.oxml.section.CT_PageSz'>), ('_titlePg', <class 'docx.oxml.shared.CT_OnOff'>), ('_scType', <class 'docx.oxml.section.CT_SectType'>)]
# {'w:pgSz': <CT_PageSz '<w:pgSz>' at 0x1f6015ec2d0>, 'w:pgMar': <CT_PageMar '<w:pgMar>' at 0x1f6015ecf50>}
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'top': 'Length | None', 'right': 'Length | None', 'bottom': 'Length | None', 'left': 'Length | None', 'header': 'Length | None', 'footer': 'Length | None', 'gutter': 'Length | None'}), ('__doc__', '``<w:pgMar>`` element, defining page margins.'), ('top', <property object at 0x000001F6012D1EE0>), ('right', <property object at 0x000001F6012D1F30>), ('bottom', <property object at 0x000001F6012D1F80>), ('left', 3600000), ('header', <property object at 0x000001F6012D2020>), ('footer', <property object at 0x000001F6012D2070>), ('gutter', <property object at 0x000001F6012D20C0>)]
# {'w:pgSz': <CT_PageSz '<w:pgSz>' at 0x1f6015ec2d0>, 'w:pgMar': <CT_PageMar '<w:pgMar>' at 0x1f6015ecf50>}
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'w': 'Length | None', 'h': 'Length | None', 'orient': 'WD_ORIENTATION'}), ('__doc__', '``<w:pgSz>`` element, defining page dimensions and orientation.'), ('w', 10800000), ('h', 21600000), ('orient', <property object at 0x000001F6012D2250>)]
# {'w:pgSz': <CT_PageSz '<w:pgSz>' at 0x1f6015ec2d0>, 'w:pgMar': <CT_PageMar '<w:pgMar>' at 0x1f6015ecf50>}
# [('__module__', 'docx.oxml.shared'), ('__annotations__', {'val': 'bool'}), ('__doc__', 'Used for `w:b`, `w:i` elements and others.\n\n    Contains a bool-ish string in its `val` attribute, xsd:boolean plus "on" and\n    "off". Defaults to `True`, so `<w:b>` for example means "bold is turned on".\n    '), ('val', <property object at 0x000001F601200F90>)]
# [('__module__', 'docx.oxml.shared'), ('__annotations__', {'val': 'bool'}), ('__doc__', 'Used for `w:b`, `w:i` elements and others.\n\n    Contains a bool-ish string in its `val` attribute, xsd:boolean plus "on" and\n    "off". Defaults to `True`, so `<w:b>` for example means "bold is turned on".\n    '), ('val', <property object at 0x000001F601200F90>)]
# [('__module__', 'docx.oxml.shared'), ('__annotations__', {'val': 'bool'}), ('__doc__', 'Used for `w:b`, `w:i` elements and others.\n\n    Contains a bool-ish string in its `val` attribute, xsd:boolean plus "on" and\n    "off". Defaults to `True`, so `<w:b>` for example means "bold is turned on".\n    '), ('val', <property object at 0x000001F601200F90>)]
# [('__module__', 'docx.oxml.shared'), ('__annotations__', {'val': 'bool'}), ('__doc__', 'Used for `w:b`, `w:i` elements and others.\n\n    Contains a bool-ish string in its `val` attribute, xsd:boolean plus "on" and\n    "off". Defaults to `True`, so `<w:b>` for example means "bold is turned on".\n    '), ('val', <property object at 0x000001F601200F90>)]
# {'w:pgSz': <CT_PageSz '<w:pgSz>' at 0x1f6015ecf50>, 'w:pgMar': <CT_PageMar '<w:pgMar>' at 0x1f6015ec2d0>}
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'val': 'WD_SECTION_START | None'}), ('__doc__', '``<w:sectType>`` element, defining the section start type.'), ('val', <property object at 0x000001F6012D2D40>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'val': 'WD_SECTION_START | None'}), ('__doc__', '``<w:sectType>`` element, defining the section start type.'), ('val', <property object at 0x000001F6012D2D40>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'val': 'WD_SECTION_START | None'}), ('__doc__', '``<w:sectType>`` element, defining the section start type.'), ('val', <property object at 0x000001F6012D2D40>)]
# [('__module__', 'docx.oxml.section'), ('__annotations__', {'val': 'WD_SECTION_START | None'}), ('__doc__', '``<w:sectType>`` element, defining the section start type.'), ('val', <property object at 0x000001F6012D2D40>)]