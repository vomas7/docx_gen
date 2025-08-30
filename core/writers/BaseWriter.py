from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.doc import DOC


class BaseWriter:
    """Base class for writing engine"""

    def __init__(self, doc: "DOC"):
        self.doc = doc
