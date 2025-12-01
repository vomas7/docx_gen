from core.doc_objects.base import BaseContainElement, BaseNonContainElement
from core.doc_objects.paragraph import SI_Paragraph, SI_pPr


# todo реализовать логику header footer SI элементов. имеет 2 тега в 1 SI_HdrFtr SI_HdrFtrRef


# SI_docGrid = tag_factory('w:docGrid', is_container=False)
# SI_cols = tag_factory('w:cols', is_container=False)
# SI_PageMar = tag_factory('w:pgMar', is_container=False)
# SI_PageSz = tag_factory('w:pgSz', is_container=False)
# SI_HdrRef = tag_factory('w:headerReference', is_container=False)
# SI_FtrRef = tag_factory('w:footerReference', is_container=False)
# SI_Hdr = tag_factory('w:hdr', is_container=True)
# SI_Ftr = tag_factory('w:ftr', is_container=True)

class SI_docGrid(BaseNonContainElement): ...


class SI_cols(BaseNonContainElement): ...


class SI_PageMar(BaseNonContainElement): ...


class SI_PageSz(BaseNonContainElement): ...


class SI_HdrFtrRef(BaseContainElement): ...


class SI_HdrFtr(BaseContainElement): ...


class SI_SectPr(BaseContainElement):
    """representation of w:SectPr"""

    # todo заполнить ограничения
    # ACCESS_CHILDREN = frozenset([qn('w:r')])

    def wrap_to_paragraph(self) -> SI_Paragraph:
        """Returns a new Paragraph containing the existing SectPr"""
        _pPr = SI_pPr(children=[self])
        _paragraph = SI_Paragraph(children=[_pPr])
        return _paragraph
