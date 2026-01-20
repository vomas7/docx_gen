from core.ui_objects.document import Document
from core.ui_objects.section import Section
from core.ui_objects import Run, Paragraph, Text, Section
from core.oxml_magic.parser import to_xml_str, make_xml_tree

from core.oxml_magic.parser import get_section_template

# print(se)

r = Run()

r.add_text("text1")
# r.font = "Times New Roman"
# r.linked_objects.reverse()
p = Paragraph()
p.add(r)
doc = Document()
doc.open(r"/home/trydimas/work_dir/eipp/docx_gen/something.docx")
#
body = doc.linked_objects[0]
# print(body)
#
sec = body.linked_objects[0]
# print(sec)
sec.add(p)
# print(to_xml_str(make_xml_tree(body)))
doc.save("sosa.docx")
sec.linked_objects.extend([Paragraph([Run([Text("aaaaaaaa")])])])
# s = Section()
print(sec.linked_objects)
from core.oxml_magic.parser import to_xml_str, make_xml_tree, convert_xml_to_cls
#f
xm = make_xml_tree(body)
print(to_xml_str(xm))
# print(xm.getchildren(), "ssssssssssssssss")
