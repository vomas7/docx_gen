from core.ui_objects.document import Document
from core.ui_objects.paragraph import Paragraph
from core.ui_objects import Section

s = Section()
s.change_page_size(width=12240, height=15840)
# print(s.property)
doc = Document()
# print(str(doc.get_section()))
# print(doc.get_section().property)
doc.objects[0].objects[0] = s
p = Paragraph()
p.add_text("iysdfasdfasdfasdfgg")
doc.objects[0].objects[0].add(p)
doc.save(r"test.docx")
#
