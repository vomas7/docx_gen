import tempfile
import docx2pdf
from typing import Union
from pathlib import Path
from typing import TYPE_CHECKING
from engine.doc_utils import validate_filepath

if TYPE_CHECKING:
    from engine.doc import DOC


class DocxExporter:

    def __init__(self, doc: 'DOC'):
        self.doc = doc

    def export_to_docx(self, file: Path = None):
        """Export file as .doc, .docx, .rtf"""
        if not file:
            self.doc.save(str(self.doc.file.resolve()))
        else:
            self.doc.save(str(file.resolve()))


class PdfExporter:

    def __init__(self, doc: 'DOC'):
        self.doc = doc

    def export_to_pdf(self, file: Path = None):
        """Creates a tempdir to generate a .docx file there, then converts it to PDF."""
        with tempfile.TemporaryDirectory(dir=self.doc.file.parent) as tmpdir:
            tmpfile = Path(tmpdir) / str(self.doc.file.name).replace(".pdf", ".docx")
            DocxExporter(self.doc).export_to_docx(tmpfile)
            if not file:
                docx2pdf.convert(tmpfile, self.doc.file.resolve())
            else:
                docx2pdf.convert(tmpfile, file.resolve())


class DocumentExporter(DocxExporter, PdfExporter):

    def __init__(self, doc: 'DOC'):
        super().__init__(doc)

    def export(self, file: Union[str, Path]):
        """Export file as .doc, .docx, .rtf .pdf"""
        file = file if isinstance(file, Path) else Path(file)
        validate_filepath(file)
        self.doc.file = file
        if file.suffix in self.doc.valid_extensions:
            if file.suffix == ".pdf":
                self.export_to_pdf()
            elif file.suffix in (".docx", ".doc", ".rtf"):
                self.export_to_docx()
            else:
                raise NotImplementedError(f"Unsupported file format: {file.suffix}. "
                                          f"Export function not implemented!")
        else:
            raise ValueError(f"Unsupported file format to export: {file.suffix}. "
                             f"Only {self.doc.valid_extensions} are allowed.")
