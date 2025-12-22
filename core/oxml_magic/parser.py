from lxml import etree

from core.oxml_magic.ns import NamespacePrefixedTag, nsmap, qn, find_qn
from core.ui_objects import BaseContainerTag, BaseTag, Text


def get_cls_by_tag(tag: str):
    from core.ui_objects import CLASS_REGISTRY
    print(tag, "11111111111")
    return CLASS_REGISTRY.get(tag)


def make_xml_tree(cls_element: BaseTag) -> etree.Element:
    xml_tree = etree.Element(qn(cls_element.tag), attrib=cls_element.attrs, nsmap=nsmap)
    # find_qn(xml_tree.attrib) #todo пока хз
    if isinstance(cls_element, BaseContainerTag):
        for ch in cls_element.linked_objects:
            tp_elem = make_xml_tree(ch)
            if isinstance(ch, Text):
                tp_elem.text = ch.text
            xml_tree.append(tp_elem)

    return xml_tree


def declare_attrib(xml_elem : etree._Element, cls_obj: BaseTag):
    slots_element = []
    for attr, val in xml_elem.attrib.items():
        attr_name = NamespacePrefixedTag.from_clark_name(attr).split(":")[1]
        slots_element.append(attr_name)
        setattr(cls_obj, "_" + attr_name, val)

def convert_xml_to_cls(xml_tree: etree.ElementBase):
    tag = get_cls_by_tag(NamespacePrefixedTag.from_clark_name(xml_tree.tag))
    cls = tag["class_tag"]
    if cls is None:
        raise TypeError(f"{xml_tree} object is not readable")
    obj = cls()
    declare_attrib(xml_tree, cls)
    for child in xml_tree:
        obj.linked_objects.append(convert_xml_to_cls(child))
    return obj


def to_xml_str(xml_tree: etree.Element) -> str:
    return etree.tostring(xml_tree, pretty_print=True, encoding="utf-8").decode()
