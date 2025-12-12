from core.doc_objects.base import BaseContainElement

class SI_rPr(BaseContainElement):
    """representation of w:rPr"""


class SI_Run(BaseContainElement):
    """representation of w:r"""
    # todo заполнить ограничения

    # ACCESS_CHILDREN = frozenset([qn('w:r')])


#todo для run добавить парсинг:
#
# class _RunContentAppender:
#     """Translates a Python string into run content elements appended in a `w:r` element.
#
#     Contiguous sequences of regular characters are appended in a single `<w:t>` element.
#     Each tab character ('\t') causes a `<w:tab/>` element to be appended. Likewise a
#     newline or carriage return character ('\n', '\r') causes a `<w:cr>` element to be
#     appended.
#     """
#
#     def __init__(self, r: CT_R):
#         self._r = r
#         self._bfr: List[str] = []
#
#     @classmethod
#     def append_to_run_from_text(cls, r: CT_R, text: str):
#         """Append inner-content elements for `text` to `r` element."""
#         appender = cls(r)
#         appender.add_text(text)
#
#     def add_text(self, text: str):
#         """Append inner-content elements for `text` to the `w:r` element."""
#         for char in text:
#             self.add_char(char)
#         self.flush()
#
#     def add_char(self, char: str):
#         """Process next character of input through finite state maching (FSM).
#
#         There are two possible states, buffer pending and not pending, but those are
#         hidden behind the `.flush()` method which must be called at the end of text to
#         ensure any pending `<w:t>` element is written.
#         """
#         if char == "\t":
#             self.flush()
#             self._r.add_tab()
#         elif char in "\r\n":
#             self.flush()
#             self._r.add_br()
#         else:
#             self._bfr.append(char)
#
#     def flush(self):
#         text = "".join(self._bfr)
#         if text:
#             self._r.add_t(text)
#         self._bfr.clear()



    #
    # def add_t(self, text: str) -> CT_Text:
    #     """Return a newly added `<w:t>` element containing `text`."""
    #     t = self._add_t(text=text)
    #     if len(text.strip()) < len(text):
    #         t.set(qn("xml:space"), "preserve")
    #     return t