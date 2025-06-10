from core.doc import DOC
from core.doc_objects.Section import DOCSection
from core.styles.section import SectionStyle


d = DOC()

s = DOCSection()

style = SectionStyle(left_margin=7)
style.right_margin = 4
s.add_style(style)

d.writer.replace_section(s)

d.writer.add_paragraph('test')


d.export.to_docx('test.docx')
print(d.doc_sections)
print(d.doc_sections[0].linked_objects)
for s in d.doc_sections:
    for i in s.linked_objects:
        print(i)
        print(type(i))
