from core.doc_objects.base import BaseNonContainElement


class SI_Text(BaseNonContainElement):
    """representation of w:t"""

    # todo заполнить ограничения
    # ACCESS_ATTRIBUTES.... = frozenset([qn('w:t')])

    def _fold_elements(self):
        self.text = self.text
        return self
