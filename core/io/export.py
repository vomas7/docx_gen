from pathlib import Path
import tempfile
from typing import TYPE_CHECKING

import docx2pdf

from core.validators.doc_utils import validate_filepath
from core.validators.export_utils import is_default_template_path

if TYPE_CHECKING:
    from core.doc import DOC


class DocumentExporter:
    valid_docx_formats = (".docx", ".doc", ".rtf")

    def __init__(self, doc: "DOC"):
        self.doc = doc

    def to_docx(self, file: Path = None):
        """Export file as .doc, .docx, .rtf"""
        if not file and not self.doc.file:
            raise ValueError(f"Export failed: No output path specified!")
        elif not file and self.doc.file:
            output = self.doc.file
        else:
            output = validate_filepath(Path(file))
            if output.suffix not in self.valid_docx_formats:
                raise ValueError(
                    f"Export failed: "
                    f"Unsupported file format to export: {output.suffix}. "
                    f"Only {self.valid_docx_formats} are allowed."
                )
        if is_default_template_path(output):
            raise FileExistsError(
                "Export failed: "
                "Can not rewrite template document!"
                " Please specify output filepath"
            )
        self.doc.save(str(output.resolve()))
        self.doc.file = output

    def to_pdf(self, file: Path = None):
        """Creates a tempdir to generate a .docx file there, then converts it to PDF."""
        valid_file = validate_filepath(file)
        if valid_file.suffix != ".pdf":
            raise ValueError(
                f"Unsupported file format to export: {valid_file.suffix}. "
                f"Only .pdf are allowed."
            )
        with tempfile.TemporaryDirectory(dir=file.parent) as tmpdir:
            tmpfile = Path(tmpdir) / str(file.name).replace(".pdf", ".docx")
            self.to_docx(tmpfile)
            if not file:
                docx2pdf.convert(tmpfile, self.doc.file.resolve())
            else:
                docx2pdf.convert(tmpfile, file.resolve())
