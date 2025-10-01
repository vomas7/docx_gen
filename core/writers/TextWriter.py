from core.doc_objects.Text import Text
from core.doc_objects.Paragraph import DOCParagraph

class TextWriter:
    def add_text_to_paragraph(self, paragraph: DOCParagraph, run: Text):
        paragraph.add_run(run.text)
        paragraph.linked_objects.append(run)

