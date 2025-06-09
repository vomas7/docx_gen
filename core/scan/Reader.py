import copy
from typing import TYPE_CHECKING
from lxml import etree

from core.doc_objects.Section import DOCSection


if TYPE_CHECKING:
    from core.doc import DOC


class DocumentBodyReader:
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }

    def __init__(self, doc: 'DOC'):
        self.doc = doc
        self.xml = self.doc.element.xml
        self.root = etree.fromstring(self.xml)
        self.body = self.root.find("w:body", namespaces=self.ns)
        self.elements_tree = list()
        self.collect_sequence_doc_objects()

    def collect_sequence_doc_objects(self):
        objects_sequence = []
        for element in self.body:
            if element.tag.endswith('p'):  # Paragraph
                if self.paragraph_has_section_tag(element):
                    self.add_section_to_tree(objects_sequence)
                    objects_sequence.clear()
                elif self.paragraph_has_text(element):
                    objects_sequence.append(self.get_text(element))

        self.add_section_to_tree(objects_sequence)

    def paragraph_has_section_tag(self, e: etree.ElementBase) -> bool:
        return bool(e.xpath('.//w:sectPr', namespaces=self.ns))

    def paragraph_has_text(self, e: etree.ElementBase) -> bool:
        return bool(e.xpath('.//w:t', namespaces=self.ns))

    def get_text(self, e: etree.ElementBase):
        return ' '.join(t.text for t in e.xpath('.//w:t', namespaces=self.ns) if t.text)

    def add_section_to_tree(self, objs: list):
        self.elements_tree.append(copy.deepcopy(objs))


class Reader(DocumentBodyReader):
    def __init__(self, doc: 'DOC'):
        self.doc = doc
        super().__init__(self.doc)
        self._document_content = list()

    def read(self):
        for section_index, section_object in enumerate(self.doc.sections):
            try:
                linked_objects = self.elements_tree[section_index]
            except IndexError:
                linked_objects = None
            self._document_content.insert(
                section_index, DOCSection(section_object, linked_objects)
            )

    @property
    def document_content(self) -> list[DOCSection]:
        return self._document_content

    @property
    def text(self):
        text = []
        for d_c in self.document_content:
            for l_0 in d_c.linked_objects:
                text.append(l_0)
        return '/n'.join(text)
