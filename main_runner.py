from core.ui_objects.document import Document
from core.ui_objects import Run, Paragraph, Text, RunProperty
from core.oxml_magic.parser import to_xml_str, make_xml_tree


r = Run()

r.add_text("text1")
r.add_break("page")

r.bold = True

print(r.linked_objects)
