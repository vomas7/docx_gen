from docx.oxml import CT_P, CT_Body, CT_Tbl, CT_SectPr, CT_Document
from docx.opc.constants import CONTENT_TYPE as CT
from docx.shared import Cm
from docx.package import Package
from docx.settings import Settings
from docx.parts.document import DocumentPart
from core.doc_objects.Section import DOCSection
from core.doc_objects.Paragraph import DOCParagraph
from core.doc_objects.base import BaseDOC, BaseContainerDOC
from core.validators.doc_utils import validate_filepath
from core.io.export import DocumentExporter
from core.reader import Reader
from core.writers.Writer import Writer
from collections.abc import Iterable
from importlib import resources
from io import BytesIO
from pathlib import Path
from typing import IO, cast, Union


def get_default_docx_path() -> str | Path:
    """Gets path to libs template."""
    try:
        with resources.path("docx.templates", "default.docx") as path:
            return str(path)
    except AttributeError:
        return resources.path("docx.templates", "default.docx").__enter__()


def is_default_template_path(path: Path) -> bool:
    return Path(get_default_docx_path()) == Path(path)


class DOC(BaseDOC):
    __standard_left_margin: Cm = Cm(3)
    __standard_right_margin: Cm = Cm(1.5)
    valid_inputs: Iterable[str] = (".docx", ".doc", ".rtf")
    valid_extensions: Iterable[str] = (".pdf", ".docx", ".doc", ".rtf")
    _file: str | Path = None
    __system_template_path: Path = None
    __part: DocumentPart = None
    __body: "_DOCBody" = None

    def __init__(self, template_path: str | Path = None):
        super().__init__()
        self.file = template_path or self.system_template_path
        self.parent = self.part
        self._element: CT_Document = self.part._element

        self.export = DocumentExporter(self)
        # self.reader = Reader(self)
        # self.writer = Writer(self)

    def __create_document_part(self):
        if Path(self.file).suffix not in self.valid_inputs:
            raise ValueError(f"File format not in {self.valid_extensions}")

        document_part = cast(
            "DocumentPart",
            Package.open(str(self.file)).main_document_part
        )

        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            tmpl = "file '%s' is not a Word file, content type is '%s'"
            raise ValueError(tmpl % (self.file, document_part.content_type))

        return document_part

    def save(self, path_or_stream: str | IO[bytes]):
        """Save this document to `path_or_stream`.

        `path_or_stream` can be either a path to a filesystem location (a string) or a
        file-like object.
        """
        self.part.save(path_or_stream)

    @property
    def doc_sections(self) -> list[DOCSection]:
        return [DOCSection(_s) for _s in self._element.sectPr_lst]

    @property
    def body(self):
        if self.__body is None:
            self.__body = _DOCBody(self._element.body, self)
        return self.__body

    @property
    def part(self) -> DocumentPart:
        if self.__part is None:
            self.__part = self.__create_document_part()
        return self.__part

    @property
    def core_properties(self):
        """A |CoreProperties| object providing Dublin Core properties of document."""
        return self.part.core_properties

    @property
    def settings(self) -> Settings:
        """A |Settings| object providing access to the document-level settings."""
        return self.part.settings

    @property
    def styles(self):
        """A |Styles| object providing access to the styles in this document."""
        return self.part.styles

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

    @property
    def system_template_path(self):
        if self.__system_template_path is None:
            self.__system_template_path = get_default_docx_path()
        return self.__system_template_path

    def __str__(self):
        return f"<DOC object: {self.file if self.file else 'not saved'}>"


class _DOCBody(BaseContainerDOC):

    CONTAIN_TYPES = Union[DOCSection]

    def __init__(self, obj: CT_Body, parent: DOC):
        super().__init__()
        self.parent = parent
        self._element = obj
        self.__put_in()

    def __put_in(self):
        """
            fills with object in self._linked_object,
            which are placed in doc.
        """
        # todo работает не корректно, берёт только SrctPr, не учитывает SectPr вложенных в паранпаф
        _section = DOCSection(self._element.get_or_add_sectPr())
        for elem in self._element.getchildren():
            if isinstance(elem, CT_P):
                _section.insert_linked_object(DOCParagraph(elem))
            elif isinstance(elem, CT_Tbl):
                _section.insert_linked_object(None)  # TODO Soon!!!
            elif isinstance(elem, CT_SectPr):
                _section._element = elem
                self.insert_linked_object(_section)
