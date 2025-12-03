from __future__ import annotations

from core.doc_objects.base import BaseContainElement, BaseNonContainElement


class SI_Paragraph(BaseContainElement):
    """representation of w:p"""


class SI_pPr(BaseContainElement):
    """representation of w:pPr"""


class SI_BookmarkStart(BaseNonContainElement):
    """representation of w:bookmarkStart"""


class SI_BookmarkEnd(BaseNonContainElement):
    """representation of w:bookmarkEnd"""
