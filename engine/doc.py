from pathlib import Path
from typing import Union, Iterable

from io import BytesIO
from docx.shared import Cm

from engine.export import DocumentExporter
from engine.doc_utils import validate_filepath
from engine.doc_utils import get_default_docx_path

from docx.package import Package
from docx.document import Document
from docx.opc.constants import CONTENT_TYPE as CT


class DOC(Document):
    __standard_left_margin: Cm = Cm(3)
    __standard_right_margin: Cm = Cm(1.5)
    valid_inputs: Iterable[str] = (".docx", ".doc", ".rtf")
    valid_extensions: Iterable[str] = (".pdf", ".docx", ".doc", ".rtf")
    _file: Union[str, Path] = None

    def __init__(self, template_path: Union[str, Path] = None):

        template_path = template_path if template_path else get_default_docx_path()

        if Path(template_path).suffix not in self.valid_inputs:
            raise ValueError(f'File format not in {self.valid_extensions}')

        document_part = Package.open(template_path).main_document_part

        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            raise ValueError(f"File {template_path} is not a Word file,"
                             f"content type is {document_part.content_type}!")

        document = document_part.document
        element = getattr(document, '_element', None)
        Document.__init__(self, element, document_part)

    def setup_margins(self) -> None:
        """Setup margins in document"""
        for section in self.sections:
            section.left_margin = self.__standard_left_margin
            section.right_margin = self.__standard_right_margin

    def export(self, file: Path = None):
        DocumentExporter(self).export(file)

    def export_to_docx(self, file: Path = None):
        DocumentExporter(self).export_to_docx(file)

    def export_to_pdf(self, file: Path = None):
        DocumentExporter(self).export_to_pdf(file)

    @property
    def doc_bytes(self) -> bytes:
        """Returns bytes of document. May important for HTTP."""
        buffer = BytesIO()
        self.save(buffer)
        content = buffer.getvalue()
        return content

    @property
    def file(self) -> Path:
        return self._file

    @file.setter
    def file(self, value: Path):
        self._file = Path(value) if not isinstance(value, Path) else value
        validate_filepath(self._file)

    def __str__(self):
        return f"<DOC object: {self.file if self.file else 'not saved'}>"
