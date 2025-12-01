from core.doc_objects.base import BaseContainElement


class SI_Document(BaseContainElement):
    """representation of w:document"""


class SI_Body(BaseContainElement):
    """representation of w:body"""

    # todo may be too like si document
    # consider that xml will be extracted from the template

    # todo realize method for section logic
