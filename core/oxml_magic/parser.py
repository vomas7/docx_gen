# pyright: reportImportCycles=false

"""XML parser for python-ui_objects."""
from tkinter.font import names
from typing import TYPE_CHECKING, Dict, Type, cast

from lxml import etree
from lxml.etree import XMLParser

from core.doc_objects import SI_Text
from core.oxml_magic.ns import NamespacePrefixedTag, nsmap


if TYPE_CHECKING:
    from core.doc_objects.base import BaseMarkupElement

# -- configure XML parser --
element_class_lookup = etree.ElementNamespaceClassLookup()
oxml_parser = etree.XMLParser(remove_blank_text=True, resolve_entities=False)
oxml_parser.set_element_class_lookup(element_class_lookup)


def parse_xml(xml: str | bytes):
    """Root lxml element obtained by parsing XML character string `xml`.

    The custom parser is used, so custom element classes are produced for elements in
    `xml` that have them.
    """
    return etree.fromstring(xml, oxml_parser)


def register_element_cls(tag: str, cls: Type["BaseOxmlElement"]):
    """Register an lxml custom element-class to use for `tag`.

    A instance of `cls` to be constructed when the oxml parser encounters an element
    with matching `tag`. `tag` is a string of the form `nspfx:tagroot`, e.g.
    `'w:document'`.
    """
    nspfx, tagroot = tag.split(":")
    namespace = element_class_lookup.get_namespace(nsmap[nspfx])
    namespace[tagroot] = cls

def OxmlElement(
        nsptag_str: str,
        attrs: Dict[str, str] | None = None,
        nsdecls: Dict[str, str] | None = None,
):  # pyright: ignore[reportPrivateUsage]
    """Return a 'loose' lxml element having the tag specified by `nsptag_str`.

    The tag in `nsptag_str` must contain the standard namespace prefix, e.g. `a:tbl`.
    The resulting element is an instance of the custom element class for this tag name
    if one is defined. A dictionary of attribute values may be provided as `attrs`; they
    are set if present. All namespaces defined in the dict `nsdecls` are declared in the
    element using the key as the prefix and the value as the namespace name. If
    `nsdecls` is not provided, a single namespace declaration is added based on the
    prefix on `nsptag_str`.
    """
    nsptag = NamespacePrefixedTag(nsptag_str)
    if nsdecls is None:
        nsdecls = nsptag.nsmap
    return oxml_parser.makeelement(nsptag.clark_name, attrib=attrs, nsmap=nsdecls)

from docx.oxml.xmlchemy import BaseOxmlElement

def _set_text_or_skip(old_elem: etree.Element, new_elem: "BaseMarkupElement"):
    _text = None
    if isinstance(old_elem, BaseOxmlElement):
        _text = old_elem.xpath("../w:t") #todo работает не совсем правильно

    elif isinstance(old_elem, etree._Element):
        _text = old_elem.xpath("../w:t", namespaces=nsmap)

    if _text:
        new_elem.text= _text[0].text



def to_si_element(element: etree._Element) -> "BaseMarkupElement":
    """transform any subclass of <etree._Element> to si element."""
    si_tree = OxmlElement(
        NamespacePrefixedTag.from_clark_name(element.tag), element.attrib
    )

    _set_text_or_skip(element, si_tree)
    for child in element:
        si_tree.children.append(to_si_element(child))
    return si_tree


from core.ui_objects.base import BaseDocx, BaseContainerDocx, BaseNonContainerDocx
from lxml import etree
from core.oxml_magic.ns import qn, nsmap, NamespacePrefixedTag
from core.oxml_magic.register_tag import get_cls_by_tag


def make_xml_tree(cls_element: BaseDocx) -> etree.Element:
    xml_tree = etree.Element(qn(cls_element.tag), nsmap=nsmap)
    if isinstance(cls_element, BaseContainerDocx):
        for ch in cls_element.linked_objects:
            xml_tree.append(make_xml_tree(ch))
    return xml_tree

def convert_xml_to_cls(xml_tree: str):
    cls = get_cls_by_tag(NamespacePrefixedTag.from_clark_name(xml_tree.tag))
    if cls is None:
        raise TypeError(f"{xml_tree} object is not readable")
    obj = cls()
    for child in xml_tree:
        obj.linked_objects.append(convert_xml_to_cls(child))
    return cls


def to_xml_str(xml_tree: etree.Element) -> str:
    return etree.tostring(xml_tree, pretty_print=True).decode()