from core.doc import DOC
from core.doc_objects.Section import DOCSection
from core.styles.section_style import SectionStyle


d = DOC()

s = DOCSection()

style = SectionStyle(left_margin=7)
style.right_margin = 4
s.add_style(style)
d.writer.replace_section(s)

d.

d.export.to_docx('test.docx')
print(d.elements)