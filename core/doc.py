from multiprocessing.spawn import set_executable

from docx.oxml import CT_P, CT_Body, CT_Tbl, CT_SectPr, CT_Document
from docx.oxml.xmlchemy import BaseOxmlElement
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
from docx.oxml.ns import nsmap


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
    _file: str | Path = None
    __system_template_path: Path = None
    __part: DocumentPart = None
    __body: "_DOCBody | None" = None

    def __init__(self, template_path: str | Path = None):
        super().__init__()
        self.file = template_path or self._system_template_path
        self.parent = self.part

        self.export = DocumentExporter(self)
        # self.reader = Reader(self) #todo наладить ридер
        self.writer = Writer(self)

    def save(self, path_or_stream: str | IO[bytes]):
        """Save this document to `path_or_stream`.

        `path_or_stream` can be either a path to a filesystem location (a string) or a
        file-like object.
        """
        self.part.save(path_or_stream)

    def _clear_document_content(self):
        """Clear xml of this document."""
        self._element._remove_body()
        self._element._add_body()

    @classmethod
    def _create_document_part(cls, file: str | Path):
        if Path(file).suffix not in cls.valid_inputs:
            raise ValueError(f"File format not in {cls.valid_inputs}")

        document_part = cast(
            "DocumentPart",
            Package.open(str(file)).main_document_part
        )

        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            tmpl = "file '%s' is not a Word file, content type is '%s'"
            raise ValueError(
                tmpl % (file, document_part.content_type)
            )

        return document_part

    @property
    def _element(self) -> CT_Document:
        """Indirect reference to | _element | of documentPart"""
        return self.part._element

    @property
    def doc_sections(self) -> list[DOCSection]:
        return [DOCSection(_s) for _s in self._element.sectPr_lst]

    @property
    def body(self):
        if self.__body is None:
            self.__body = _DOCBody(self)
        return self.__body

    @property
    def part(self) -> DocumentPart:
        if self.__part is None:
            self.__part = self._create_document_part(self.file)
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
        """Active document file"""
        return self._file

    @file.setter
    def file(self, value: Path | str):
        self._file = validate_filepath(Path(value))

    @property
    def _system_template_path(self):
        if self.__system_template_path is None:
            self.__system_template_path = get_default_docx_path()
        return self.__system_template_path

    def __str__(self):
        return f"<DOC object: {self.file if self.file else 'not saved'}>"


class _DOCBody(BaseContainerDOC):
    CONTAIN_TYPES = Union[DOCSection]

    def __init__(self, parent: DOC):
        super().__init__()
        self.parent = parent
        self.__put_in()

    @property
    def _element(self) -> CT_Body:
        """Indirect reference to | _element | of Body element"""
        return self.parent._element.body

    @staticmethod
    def __reveal_sections(lst_elem: list[BaseOxmlElement]):
        """detects sections and extracts them from a paragraph"""
        for index, elem in enumerate(lst_elem):
            if isinstance(elem, CT_SectPr):
                continue

            section = elem.find("./w:pPr/w:sectPr", namespaces=nsmap)
            if section is not None:
                lst_elem.pop(index)
                lst_elem.insert(index, section)

    def __uniform_oxml_elements(self) -> list[BaseOxmlElement]:
        _uniform_lst = list(self._element)
        self.__reveal_sections(_uniform_lst)
        # todo будет обрабатывать и картинки, возможно таблицы!
        return _uniform_lst

    def __put_in(self):
        """
            fills with object in self._linked_object,
            which are placed in doc.
        """
        elem_lst = self.__uniform_oxml_elements()
        _inner = []
        for elem in elem_lst:
            if isinstance(elem, CT_SectPr):
                self.insert_linked_object(
                    DOCSection(elem, linked_objects=_inner)
                )
                _inner = []
            else:
                _inner.append(DOCSection.convert_to_linked_object(elem))
