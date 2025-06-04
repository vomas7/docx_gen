import tempfile
import docx2pdf
from pathlib import Path
from typing import TYPE_CHECKING
from engine.doc_utils import validate_filepath

if TYPE_CHECKING:
    from engine.doc import DOC


class DocumentExporter:

    valid_docx_formats = (".docx", ".doc", ".rtf", '.html')

    def __init__(self, doc: 'DOC'):
        self.doc = doc

    def to_docx(self, file: Path = None):
        """Export file as .doc, .docx, .rtf"""
        valid_file = validate_filepath(file)
        if valid_file.suffix not in self.valid_docx_formats:
            raise ValueError(f"Unsupported file format to export: {valid_file.suffix}. "
                             f"Only {self.valid_docx_formats} are allowed.")
        if not valid_file:
            self.doc.save(str(self.doc.file.resolve()))
        else:
            self.doc.save(str(file.resolve()))

    def to_pdf(self, file: Path = None):
        """Creates a tempdir to generate a .docx file there, then converts it to PDF."""
        valid_file = validate_filepath(file)
        if valid_file.suffix != '.pdf':
            raise ValueError(f"Unsupported file format to export: {valid_file.suffix}. "
                             f"Only .pdf are allowed.")
        with tempfile.TemporaryDirectory(dir=file.parent) as tmpdir:
            tmpfile = Path(tmpdir) / str(file.name).replace(".pdf", ".docx")
            self.to_docx(tmpfile)
            if not file:
                docx2pdf.convert(tmpfile, self.doc.file.resolve())
            else:
                docx2pdf.convert(tmpfile, file.resolve())
