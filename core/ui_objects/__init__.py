from .document import Body, Document
from .paragraph import Paragraph, Run, Text
from .section import Section

from core.oxml_magic.register_tag import register_tag

register_tag("w:body", Body)
register_tag("w:document", Document)
register_tag("w:p", Paragraph)
register_tag("w:r", Run)
register_tag("w:sectPr", Section)
register_tag("w:t", Text)

