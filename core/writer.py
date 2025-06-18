from typing import Union, TYPE_CHECKING
if TYPE_CHECKING:
    from core.doc import DOC
from core.doc_objects.Section import DOCSection


DOCElement = Union[DOCSection]


class Writer:

    def __init__(self, doc: 'DOC'):
        self.doc = doc

    def write(self, obj: DOCElement, index: int = -1):
        if isinstance(obj, DOCSection):
            self.__write_section(obj, index)

    def __write_section(self, section: DOCSection, index: int = -1):
        section_to_replace = self.doc.sections[index]
        doc_body = self.doc._element.body
        to_replace_xml = section_to_replace._sectPr
        is_replaced_xml = section._sectPr
        print(id(doc_body.add_section_break()))
        doc_body.replace(to_replace_xml, is_replaced_xml)
