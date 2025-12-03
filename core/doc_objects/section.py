from core.doc_objects.base import BaseContainElement, BaseNonContainElement
from core.doc_objects.paragraph import SI_Paragraph, SI_pPr


# todo реализовать логику header footer SI элементов. имеет 2 тега в 1 SI_HdrFtr SI_HdrFtrRef



class SI_docGrid(BaseNonContainElement): ...


class SI_cols(BaseNonContainElement): ...


class SI_PageMar(BaseNonContainElement): ...


class SI_PageSz(BaseNonContainElement): ...


class SI_HdrFtrRef(BaseContainElement): ...


class SI_HdrFtr(BaseContainElement): ...


class SI_SectPr(BaseContainElement):
    """representation of w:sectPr"""

    # todo заполнить ограничения
    # ACCESS_CHILDREN = frozenset([qn('w:r')])

    def wrap_to_paragraph(self) -> SI_Paragraph:
        """Returns a new Paragraph containing the existing SectPr"""
        _pPr = SI_pPr(children=[self])
        _paragraph = SI_Paragraph(children=[_pPr])
        return _paragraph
