from collections.abc import Iterable
from importlib import resources
from io import BytesIO
from pathlib import Path
from docx.document import Document, Section
from docx.opc.constants import CONTENT_TYPE as CT
from docx.package import Package
from docx.shared import Cm
from core.validators.doc_utils import validate_filepath
from core.io.export import DocumentExporter
from core.reader import Reader
from core.writers.Writer import Writer
from core.doc_objects.Section import DOCSection
from docx.document import _Body
import docx.types as t
from docx.oxml import CT_Body


def get_default_docx_path() -> str | Path:
    """Gets path to libs template."""
    try:
        with resources.path("docx.templates", "default.docx") as path:
            return str(path)
    except AttributeError:
        return resources.path("docx.templates", "default.docx").__enter__()


def is_default_template_path(path: Path) -> bool:
    return Path(get_default_docx_path()) == Path(path)


class DOC(Document):
    __standard_left_margin: Cm = Cm(3)
    __standard_right_margin: Cm = Cm(1.5)
    valid_inputs: Iterable[str] = (".docx", ".doc", ".rtf")
    valid_extensions: Iterable[str] = (".pdf", ".docx", ".doc", ".rtf")
    _file: str | Path = None
    system_template_path: Path = None

    #todo адаптировать body под docx_gen - убрать ненужные хзависимости

    def __init__(self, template_path: str | Path = None):

        self.system_template_path = Path(get_default_docx_path())

        if not template_path:
            template_path = self.system_template_path

        if Path(template_path).suffix not in self.valid_inputs:
            raise ValueError(f"File format not in {self.valid_extensions}")

        document_part = Package.open(str(template_path)).main_document_part

        if document_part.content_type != CT.WML_DOCUMENT_MAIN:
            tmpl = "file '%s' is not a Word file, content type is '%s'"
            raise ValueError(
                tmpl % (template_path, document_part.content_type)
            )

        document = document_part.document
        element = getattr(document, "_element", None)
        Document.__init__(self, element, document_part)

        self.__body = None

        self.doc_sections: list[DOCSection] = [
            DOCSection(
                Section(self._body._element.get_or_add_sectPr, document_part)
            )
        ]

        self.export = DocumentExporter(self)
        self.reader = Reader(self)
        self.writer = Writer(self)

    def set_section(self, section: DOCSection, index: int = -1):
        self._element.body.add_section_break()
        self._element.body.replace(
            self.sections[index]._sectPr, section._sectPr
        )

    @property
    def body(self):
        if self.__body is None:
            self.__body = _DOCBody(self._element.body, self)
        return self.__body

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


from core.doc_objects.Section import DOCSection
from core.doc_objects.Paragraph import DOCParagraph
from docx.oxml import CT_P, CT_Body, CT_Tbl, CT_SectPr
from core.doc_objects.base import BaseDOC
from typing import Union

CONTAIN_TYPES = Union[DOCSection]


class _DOCBody(BaseDOC):

    def __init__(self, obj: CT_Body, parent: DOC):
        BaseDOC.__init__(self)
        self.parent = parent
        self._element = obj
        self.__put_in()

    def __put_in(self):
        """
            fills with object in self._linked_object,
            which are placed in doc.
        """
        #todo работает не корректно, берёт только SrctPr, не учитывает SectPr вложенных в паранпаф
        _section = DOCSection(self._element.get_or_add_sectPr())
        for elem in self._element.getchildren():
            if isinstance(elem, CT_P):
                _section.insert_linked_object(DOCParagraph(elem))
            elif isinstance(elem, CT_Tbl):
                _section.insert_linked_object(None)  # TODO Soon!!!
            elif isinstance(elem, CT_SectPr):
                _section._element = elem
                self.insert_linked_object(_section)

    @property
    def linked_objects(self):
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, value):
        self._linked_objects = value

    # todo это будет повторяться у элементов, которые хранят объекты

    def insert_linked_object(self, value: CONTAIN_TYPES, index: int = - 1):
        if not isinstance(value, CONTAIN_TYPES):
            raise TypeError(f'linked_objects must be a {CONTAIN_TYPES}') # noqa
        value.parent = self
        self._linked_objects.insert(index, value)

    def remove_linked_object(self, index: int = - 1):
        _elem = self._linked_objects.pop(index)
        _elem.parent = None
        return _elem
