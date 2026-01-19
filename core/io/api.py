import os

from typing import IO, TYPE_CHECKING, cast

from core.io.constants import CONTENT_TYPE as CT
from core.io.package import Package

if TYPE_CHECKING:
    from core.ui_objects import Document
    from core.parts.document import DocumentPart


def parse_document_part(docx: str | IO[bytes] | None = None) -> "DocumentPart":
    """Return a |Document| object loaded from `ui_objects`, where `docx` can be either a path
    to a ``.docx`` file (a string) or a file-like object.

    If `ui_objects` is missing or ``None``, the built-in default document "template" is
    loaded.
    """
    docx = _default_docx_path() if docx is None else docx
    document_part = cast("DocumentPart", Package.open(docx).main_document_part)
    if document_part.content_type != CT.WML_DOCUMENT_MAIN:
        tmpl = "file '%s' is not a Word file, content type is '%s'"
        raise ValueError(tmpl % (docx, document_part.content_type))
    return document_part


def _default_docx_path():
    """Return the path to the built-in default .ui_objects package."""
    _thisdir = os.path.split(__file__)[0]
    return os.path.join(_thisdir, "..", "templates", "default.docx")
