from core.ui_objects.document import Document
from core.ui_objects.section import Section
from core.ui_objects import Run, Paragraph, Text, Section
from core.oxml_magic.parser import to_xml_str, make_xml_tree

from core.oxml_magic.parser import get_section_template
s = Section()

# print(se)

r = Run()

r.add_text("text1")
# r.font = "Times New Roman"
# r.linked_objects.reverse()
p = Paragraph()
p.add(r)
doc = Document()
doc.open(r"C:\Users\AkentevDV\Desktop\localProjects\docx_gen\core\templates\default.docx")
#
body = doc.linked_objects[0]
#
body.add(p)
print(to_xml_str(make_xml_tree(body)))
doc.save("sosa.docx")
body.linked_objects.extend([Paragraph([Run([Text("aaaaaaaa")])])])
