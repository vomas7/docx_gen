from lxml import etree

from core.oxml_magic.ns import NamespacePrefixedTag, nsmap, qn
from core.ui_objects import BaseContainerTag, BaseTag, Text


def get_cls_by_tag(tag: str):
    from core.ui_objects import CLASS_REGISTRY

    return CLASS_REGISTRY.get(tag)


def make_xml_tree(cls_element: BaseTag) -> etree.Element:
    xml_tree = etree.Element(qn(cls_element.tag), attrib=cls_element.attrs, nsmap=nsmap)
    if isinstance(cls_element, BaseContainerTag):
        for ch in cls_element.linked_objects:
            tp_elem = make_xml_tree(ch)
            if isinstance(ch, Text):
                tp_elem.text = ch.text
            xml_tree.append(tp_elem)

    return xml_tree


def convert_xml_to_cls(xml_tree: etree.ElementBase):
    cls = get_cls_by_tag(NamespacePrefixedTag.from_clark_name(xml_tree.tag))
    if cls is None:
        raise TypeError(f"{xml_tree} object is not readable")
    obj = cls()
    for child in xml_tree:
        obj.linked_objects.append(convert_xml_to_cls(child))
    return obj


def to_xml_str(xml_tree: etree.Element) -> str:
    return etree.tostring(xml_tree, pretty_print=True, encoding="utf-8").decode()
