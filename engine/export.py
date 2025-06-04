import tempfile
import docx2pdf
from pathlib import Path
from typing import TYPE_CHECKING
from engine.doc_utils import validate_filepath

if TYPE_CHECKING:
    from engine.doc import DOC


class DocumentExporter:

    valid_docx_formats = (".docx", ".doc", ".rtf")

    @staticmethod
    def export_to_docx(doc: 'DOC', file: Path = None):
        """Export file as .doc, .docx, .rtf"""
        valid_file = validate_filepath(file)
        if valid_file.suffix not in DocumentExporter.valid_docx_formats:
            raise ValueError(f"Unsupported file format to export: {valid_file.suffix}. "
                             f"Only {DocumentExporter.valid_docx_formats} are allowed.")
        if not file:
            doc.save(str(doc.file.resolve()))
        else:
            doc.save(str(file.resolve()))

    @staticmethod
    def export_to_pdf(doc: 'DOC', file: Path = None):
        """Creates a tempdir to generate a .docx file there, then converts it to PDF."""
        valid_file = validate_filepath(file)
        if valid_file.suffix != '.pdf':
            raise ValueError(f"Unsupported file format to export: {valid_file.suffix}. "
                             f"Only .pdf are allowed.")
        with tempfile.TemporaryDirectory(dir=file.parent) as tmpdir:
            tmpfile = Path(tmpdir) / str(file.name).replace(".pdf", ".docx")
            DocumentExporter.export_to_docx(doc, tmpfile)
            if not file:
                docx2pdf.convert(tmpfile, doc.file.resolve())
            else:
                docx2pdf.convert(tmpfile, file.resolve())
