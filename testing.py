from core.doc import DOC
from core.doc_objects.Paragraph import DOCParagraph
from core.doc_objects.Section import DOCSection

# from core.doc_objects.Text import Text
from core.styles.paragraph import ParagraphStyle
from core.styles.section import SectionStyle

# from core.styles.text import TextStyle
from core.writers.Writer import Writer
from core.styles.paragraph import WD_ALIGN_PARAGRAPH

doc = DOC()
s = DOCSection()
s_style = SectionStyle()
s.add_style(s_style)

# этот кусок пока не сработает, т.к не реализованы нужные классы
p = DOCParagraph()
p_style = ParagraphStyle()
p_style.alignment = WD_ALIGN_PARAGRAPH.RIGHT
p.add_style(p_style)

# text = Text("привет-привет")
# t_style = TextStyle()
# text.add_style(t_style)

# p.add_run(text)
# кусок до этого места


wr = Writer(doc=doc)
wr.add_section(s)

# разве параграф не должен записываться внурь секции?
wr.add_paragraph(p)
# например, следующим образом:
# s.add_paragraph(p)

doc.save("test1.docx")
