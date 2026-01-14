import os.path
import warnings

from lxml import etree

from core.oxml_magic.ns import NamespacePrefixedTag, nsmap, qn
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.text import Text
from core.ui_objects.section import Section


def get_cls_by_tag(tag: str):
    from core.ui_objects import CLASS_REGISTRY
    return CLASS_REGISTRY.get(tag)


def make_xml_tree(cls_element: BaseTag) -> etree.Element:
    xml_tree = etree.Element(qn(cls_element.tag), attrib=cls_element.attrs, nsmap=nsmap)
    if isinstance(cls_element, BaseContainerTag):
        children = cls_element._xml_children if isinstance(cls_element, Section) else cls_element.linked_objects
        for ch in children:
            tp_elem = make_xml_tree(ch)
            if isinstance(ch, Text):
                tp_elem.text = ch.text
            xml_tree.append(tp_elem)

    return xml_tree


def declare_attrib(xml_elem: etree._Element, cls_obj: BaseTag):
    for attr, val in xml_elem.attrib.items():
        attr_name = NamespacePrefixedTag.from_clark_name(attr).split(":")[1]
        if hasattr(cls_obj, attr_name):
            property_attr = getattr(type(cls_obj), attr_name)
            property_attr.__set__(cls_obj, val)


def convert_xml_to_cls(
    xml_tree: etree.ElementBase,
):
    tag = get_cls_by_tag(NamespacePrefixedTag.from_clark_name(xml_tree.tag))
    if not tag:
        warnings.warn(f"{xml_tree} object is not readable", stacklevel=2)
        return None
    cls = tag.get("class_tag")

    if cls is None:
        raise TypeError(f"{xml_tree} object is not readable")

    obj = cls()
    if isinstance(obj, Text):
        obj.text = xml_tree.text
    declare_attrib(xml_tree, obj)

    for child in xml_tree:
        cls_object = convert_xml_to_cls(child)
        if cls_object:
            if isinstance(obj, Section):
                continue
            else:
                obj.linked_objects.append(cls_object)
    return obj


def to_xml_str(xml_tree: etree.Element) -> str:
    return etree.tostring(xml_tree, pretty_print=True, encoding="utf-8").decode()


def get_section_template():

    from core.io.api import parse_document_part
    file_path = os.path.dirname(__file__)
    template_file = os.path.join(os.path.abspath(file_path), '..', "templates", "default.docx")

    _part = parse_document_part(template_file)
    [_body] = _part._element.getchildren()
    _section = _body.getchildren()[-1]
    return _section

