import copy
from typing import TYPE_CHECKING
from lxml import etree


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
        self.elements_tree = dict()
        self.collect_sequence_doc_objects()

    def collect_sequence_doc_objects(self):
        section_index = 0
        objects_sequence = []
        for element in self.body:
            if element.tag.endswith('p'):  # Paragraph
                if self.paragraph_has_section_tag(element):
                    self.add_section_to_tree(section_index, objects_sequence)
                    section_index += 1
                    objects_sequence.clear()
                elif self.paragraph_has_text(element):
                    objects_sequence.append(self.get_text(element))

    def paragraph_has_section_tag(self, e: etree.ElementBase) -> bool:
        return bool(e.xpath('.//w:sectPr', namespaces=self.ns))

    def paragraph_has_text(self, e: etree.ElementBase) -> bool:
        return bool(e.xpath('.//w:t', namespaces=self.ns))

    def get_text(self, e: etree.ElementBase):
        return ' '.join(t.text for t in e.xpath('.//w:t', namespaces=self.ns) if t.text)

    def add_section_to_tree(self, section_index: int, objs: list):
        self.elements_tree[f"Section_{section_index}"] = copy.deepcopy(objs)


class Reader(DocumentBodyReader):
    def __init__(self, doc: 'DOC'):
        self.doc = doc
        super().__init__(self.doc)
    # Prisrat Section
