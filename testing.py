from core.doc import DOC
from core.doc_objects.Paragraph import DOCParagraph
from core.doc_objects.Section import DOCSection
from core.doc_objects.Text import Text
from core.styles.paragraph import ParagraphStyle
from core.styles.section import SectionStyle
from core.styles.text import TextStyle
from core.writers.Writer import Writer

doc = DOC()
s = DOCSection()
s_style = SectionStyle()
s.add_style(s_style)


wr = Writer(doc=doc)
wr.add_section(s)

doc.save("test1.docx")
