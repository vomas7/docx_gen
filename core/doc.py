from collections.abc import Iterable
from importlib import resources
from io import BytesIO
from pathlib import Path
from typing import overload

from docx.document import Document
from docx.opc.constants import CONTENT_TYPE as CT
from docx.package import Package
from docx.shared import Cm

from core.validators.doc_utils import validate_filepath
from core.io.export import DocumentExporter

from core.reader import Reader
from core.writer import Writer
from core.writer import DOCElement
from core.doc_objects.Section import DOCSection

from core.scan.Reader import Reader
from core.scan.Writer import Writer



def get_default_docx_path() -> str | Path:
    """Gets path to libs template."""
    try:
        with resources.path("docx.templates", "default.docx") as path:
            return str(path)
    except AttributeError:
        return resources.path("docx.templates", "default.docx").__enter__()


def is_default_template_path(path: Path) -> bool:
    return Path(get_default_docx_path()) == Path(path)

IndexInDOC = int  # Индекс в списке всех элементов документа.


class DOC(Document):
    __standard_left_margin: Cm = Cm(3)
    __standard_right_margin: Cm = Cm(1.5)
    valid_inputs: Iterable[str] = (".docx", ".doc", ".rtf")
    valid_extensions: Iterable[str] = (".pdf", ".docx", ".doc", ".rtf")
    _file: str | Path = None
    system_template_path: Path = None

    def __init__(self, template_path: str | Path = None):

        self.system_template_path = Path(get_default_docx_path())

        if not template_path:
            template_path = self.system_template_path

        if Path(template_path).suffix not in self.valid_inputs:
            raise ValueError(f"File format not in {self.valid_extensions}")

        document_part = Package.open(str(template_path)).main_document_part

        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            raise ValueError(
                f"File {template_path} is not a Word file,"
                f"content type is {document_part.content_type}!"
            )

        document = document_part.document
        element = getattr(document, "_element", None)
        Document.__init__(self, element, document_part)

        self.elements = list()

        self.export = DocumentExporter(self)
        self.reader = Reader(self)
        self.writer = Writer(self)

    def set_section(self, section: DOCSection, index: int = -1):
        self._element.body.add_section_break()
        self._element.body.replace(
            self.sections[index]._sectPr,section._sectPr
        )


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
        self._file = validate_filepath(Path(value))

    def __str__(self):
        return f"<DOC object: {self.file if self.file else 'not saved'}>"
