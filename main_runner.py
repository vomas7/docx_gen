from core.ui_objects.document import Document
from core.ui_objects import Run, Paragraph, Text
from core.oxml_magic.parser import to_xml_str, make_xml_tree


r = Run()

r.add_text("text1")
r.font = "Times New Roman"
# r.linked_objects.reverse()
p = Paragraph()
p.add(r)
doc = Document()
doc.open("test.docx")

body = doc.linked_objects[0]

body.add(p)
print(to_xml_str(make_xml_tree(body)))
doc.save("sos.docx")
# body.linked_objects.extend([Paragraph([Run([Text("aaaaaaaa")])])])
