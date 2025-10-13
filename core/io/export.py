from pathlib import Path
import tempfile
from typing import TYPE_CHECKING, cast
from core.doc_objects import DOCParagraph, DOCSection, BaseDOC, Text

import docx2pdf
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.oxml import CT_Document
from core.validators.doc_utils import validate_filepath

if TYPE_CHECKING:
    from core.doc import DOC


class DocumentExporter:
    valid_docx_formats = (".docx", ".doc", ".rtf")

    def __init__(self, document: "DOC"):
        self.doc = document

    def commit(self):
        """
        assembles a DocumentPart from all linked_objects.
        wraps all SectPr into pPr, before implementing xml filling
        """
        def run_through_objects(objects: list):
            """recursion for filling DocumentPart xml"""
            for obj in objects:
                if isinstance(obj, BaseOxmlElement):
                    # todo временная мера т.к элементы Text относятся к _Element
                    continue
                if isinstance(obj.parent, DOCSection):
                    obj.parent._element.addprevious(obj._element)
                else:
                    obj.parent._element.append(obj._element)
                if hasattr(obj, "linked_objects"):
                    run_through_objects(obj.linked_objects)
            return

        for section in self.doc.body.linked_objects[:-1]:
            section.wrap_to_paragraph()

        run_through_objects(self.doc.body.linked_objects)

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
        if self.doc._system_template_path == output:
            raise FileExistsError(
                "Export failed: "
                "Can not rewrite template document!"
                " Please specify output filepath"
            )

        self.doc._clear_document_content()
        self.commit()
        self.doc.save(str(output.resolve()))

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
