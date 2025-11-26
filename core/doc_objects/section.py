from core.doc_objects.base import BaseContainElement, BaseTagElement
from typing import List
from core.doc_objects.base import BaseAttributeElement, BaseNonContainElement
from core.doc_objects.paragraph import SI_Paragraph, SI_pPr


#todo реализовать логику header footer SI элементов. имеет 2 тега в 1 SI_HdrFtr SI_HdrFtrRef

# class SI_HdrFtr(BaseContainElement):
#     # todo Заполнить подходящими значениями Атрибуты и тэги
#
#     def __init__(self,
#                  children: List[BaseMurkupElement] = None,
#                  attrs: List[BaseAttributeElement] = None):
#         super().__init__("CT_HdrFtr", attrs, children)
#
#
# class SI_HdrFtrRef(BaseNonContainElement):
#     # todo Заполнить подходящими значениями Атрибуты и тэги
#
#     def __init__(self,
#                  attrs: List[BaseAttributeElement] = None):
#         super().__init__("CT_HdrFtrRef", attrs)


class SI_PageMar(BaseNonContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги

    def __init__(self,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("CT_PageMar", attrs)


class SI_PageSz(BaseNonContainElement):
    # todo Заполнить подходящими значениями Атрибуты и тэги

    def __init__(self,
                 attrs: List[BaseAttributeElement] = None):
        super().__init__("CT_PageSz", attrs)


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
