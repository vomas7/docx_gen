from core.ui_objects.document import Document
from core.ui_objects.paragraph import Paragraph


doc = Document(r"test.docx")
p = Paragraph()
p.add_text("iysdfasdfasdfasdfgg")
doc.objects[0].objects[0].add(p)
doc.save(r"test.docx")
#
