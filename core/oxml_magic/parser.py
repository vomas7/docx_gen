import zipfile
import warnings
from typing import TYPE_CHECKING, IO
from lxml import etree
from core.oxml_magic.xml_object import find_name_attr
from core.oxml_magic.ns import NamespacePrefixedTag, nsmap, qn, XmlString
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.section import Section
from core.ui_objects.text import Text


if TYPE_CHECKING:
    pass


def get_cls_by_tag(tag: str):
    from core.ui_objects import CLASS_REGISTRY

    return CLASS_REGISTRY.get(tag)


def make_xml_tree(cls_element: BaseTag) -> etree.Element:
    xml_tree = etree.Element(qn(cls_element.tag), attrib=cls_element.attrs, nsmap=nsmap)
    if isinstance(cls_element, BaseContainerTag):
        if isinstance(cls_element, Section):
            children = cls_element.property
        elif cls_element.property:
            children = list(cls_element.property) + list(cls_element.objects)
        else:
            children = cls_element.objects
        for ch in children:
            if isinstance(ch, Section):
                extracted = [make_xml_tree(i) for i in ch.objects]
                list(map(lambda ex: xml_tree.append(ex), extracted))

            tp_elem = make_xml_tree(ch)
            if isinstance(ch, Text):
                tp_elem.text = ch.text
            xml_tree.append(tp_elem)

    return xml_tree


def declare_attrib(xml_elem: etree._Element, cls_obj: BaseTag):
    for attr, val in xml_elem.attrib.items():
        if ":" not in attr:
            attr = cls_obj.tag.split(":")[0] + f":{attr}"  # takes tag prefix
        attr_name = find_name_attr(cls_obj, attr)
        if attr_name is not None and attr_name.startswith("_"):
            attr_name = attr_name[1:]
            property_attr = getattr(type(cls_obj), attr_name)
            property_attr.__set__(cls_obj, val)


def read_xml_markup(xml_tree: etree.ElementBase):
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
        cls_object = read_xml_markup(child)
        if cls_object:
            access_property = list(
                filter(
                    lambda x: x.get("class").__name__ == cls_object.__class__.__name__,
                    obj.access_property,
                )
            )

            if len(access_property) > 0:
                position = access_property[0].get("required_position") or 0
                obj.property.insert(position, cls_object)
            else:
                obj.objects.append(cls_object)
    return obj


def process_sections(obj_markup: BaseTag):
    from core.ui_objects.document import Body

    if isinstance(obj_markup, Body):
        elements = []
        body_linked = []
        for item in obj_markup.objects:
            if isinstance(item, Section):
                item.objects = elements
                elements.clear()
                body_linked.append(item)
            else:
                elements.append(item)
        obj_markup.objects = body_linked
        return obj_markup


def convert_xml_to_cls(xml_tree: etree.ElementBase) -> BaseTag:
    object_markup = read_xml_markup(xml_tree)
    return process_sections(object_markup)


def to_xml_str(xml_tree: etree.Element) -> XmlString:
    xml = etree.tostring(xml_tree, pretty_print=True, encoding="utf-8").decode()
    return XmlString(xml)


def parse_document(file: str | IO[bytes]) -> BaseTag:
    """Returns the Document Body tag"""
    with (
        zipfile.ZipFile(file, "r") as docx_zip,
        docx_zip.open("word/document.xml") as xml_file,
    ):
        xml_content = xml_file.read()
        xml = etree.fromstring(xml_content)
    [_body] = xml.getchildren()
    return convert_xml_to_cls(_body)
