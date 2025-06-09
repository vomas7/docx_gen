from docx.shared import Length, Cm

from core.styles.section_style import SectionStyle
from core.styles.stylist import CM
from core.doc import DOC
from core.doc_objects.Section import DOCSection
from docx.section import Sections

s = DOCSection()

s.style(SectionStyle(left_margin=Length(Cm(4))))

print(s.left_margin.cm)
d = DOC()
d.set_section(s)
# list(d.sections)[0].left_margin = CM(5)

d.export.to_docx('test.docx')
