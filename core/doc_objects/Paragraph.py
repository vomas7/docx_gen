from core.doc_objects.Text import Text


class DOCParagraph(Text):

    def __init__(self, text: str):
        super().__init__(text=text)

    def __repr__(self):
        return "<DOC.PARAGRAPH object>"
