from core.doc_objects.base import BaseContainElement, BaseTagElement
from typing import List
from core.doc_objects.base import BaseAttributeElement
from core.doc_objects.paragraph import SI_Paragraph, SI_pPr
# from core.doc_objects.tags import tag_factory

# from docx.oxml

# todo реализовать логику header footer SI элементов. имеет 2 тега в 1 SI_HdrFtr SI_HdrFtrRef


# SI_docGrid = tag_factory('w:docGrid', is_container=False)
# SI_cols = tag_factory('w:cols', is_container=False)
# SI_PageMar = tag_factory('w:pgMar', is_container=False)
# SI_PageSz = tag_factory('w:pgSz', is_container=False)
# SI_HdrRef = tag_factory('w:headerReference', is_container=False)
# SI_FtrRef = tag_factory('w:footerReference', is_container=False)
# SI_Hdr = tag_factory('w:hdr', is_container=True)
# SI_Ftr = tag_factory('w:ftr', is_container=True)


class SI_SectPr(BaseContainElement):
    """
    Display <Section> without any
    wrapping at the object level
    """

    # todo Заполнить подходящими значениями Атрибуты и тэги
    # xpath = "./w:body/w:p/w:pPr/w:sectPr | ./w:body/w:sectPr"

    def __init__(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("w:SectPr", attrs, children)

    def wrap_to_paragraph(self) -> SI_Paragraph:
        """Returns a new Paragraph containing the existing SectPr"""
        _pPr = SI_pPr(children=[self])
        _paragraph = SI_Paragraph(children=[_pPr])
        return _paragraph
