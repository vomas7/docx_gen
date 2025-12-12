from core.doc_objects.base import BaseNonContainElement, BaseContainElement


class SI_lang(BaseNonContainElement):
    """representation of w:lang"""


class SI_Text(BaseNonContainElement):
    """representation of w:t"""


    def __str__(self):
        return self.text or ""

    # todo заполнить ограничения
    # ACCESS_ATTRIBUTES.... = frozenset([qn('w:t')])
