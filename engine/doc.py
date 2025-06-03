import tempfile
from pathlib import Path
from typing import Union, Iterable
import docx2pdf
from io import BytesIO
from docx.shared import Cm

from engine.doc_utils import validate_filepath
from engine.doc_utils import get_default_docx_path

from docx.package import Package
from docx.document import Document
from docx.opc.constants import CONTENT_TYPE as CT


class DOC(Document):
    __standard_left_margin: Cm = Cm(3)
    __standard_right_margin: Cm = Cm(1.5)
    __valid_extensions: Iterable[str] = (".pdf", ".docx", ".doc", ".rtf")
    _file: Union[str, Path] = None

    def __init__(self, template: str = None):
        template = template if template else get_default_docx_path()
        document_part = Package.open(template).main_document_part
        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            raise ValueError(f"File {template} is not a Word file,"
                             f"content type is {document_part.content_type}!")
        document = document_part.document
        element = getattr(document, '_element', None)
        Document.__init__(self, element, document_part)

    def export(self, file: Union[str, Path]):
        file = file if isinstance(file, Path) else Path(file)
        validate_filepath(file)
        self.file = file
        if file.suffix in self.__valid_extensions:
            if file.suffix == ".pdf":
                self.__export_to_pdf()
            elif file.suffix == ".docx" or file.suffix == ".doc":
                self.__export_to_docx()
            else:
                raise NotImplementedError(f"Unsupported file format: {file.suffix}. "
                                          f"Export function not implemented!")
        else:
            raise ValueError(f"Unsupported file format to export: {file.suffix}. "
                             f"Only {self.__valid_extensions} are allowed.")

    def __export_to_docx(self, file: Path = None):
        """Export file as .doc, .docx, .rtf"""
        if not file:
            self.save(str(self.file.resolve()))
        else:
            self.save(str(file.resolve()))

    def __export_to_pdf(self):
        """Creates a tempdir to generate a .docx file there, then converts it to PDF."""
        with tempfile.TemporaryDirectory(dir=self.file.parent) as tmpdir:
            tmpfile = Path(tmpdir) / str(self.file.name).replace(".pdf", ".docx")
            self.__export_to_docx(tmpfile)
            docx2pdf.convert(tmpfile, self.file.resolve())

    def setup_margins(self) -> None:
        """Setup margins in document"""
        for section in self.sections:
            section.left_margin = self.__standard_left_margin
            section.right_margin = self.__standard_right_margin

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
