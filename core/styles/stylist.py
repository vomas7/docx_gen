import enum

from docx.enum.section import WD_ORIENTATION
from docx.opc.oxml import qn
from docx.oxml.xmlchemy import BaseOxmlElement
from docx.shared import Twips

from core.styles.base import BaseStyle
from lxml.etree import _Element
from lxml.etree import QName


def set_style(xml: _Element, dc_style: BaseStyle):
    """
    A function for changing tag attributes in xml related to the element style,
    for use in docx-gen element classes
    """
    # print(list(dc_style.__dict__.items()))
    # for parent, kids in dc_style.__dict__.items():
    #     children = {}
    #     for child in xml.getchildren():
    #         if isinstance(child, BaseOxmlElement):
    #             children[child._nsptag] = child
    #     old_child = children.get(f'{dc_style.NAMESPACE}:{parent[1:]}')
    #     print(children)
    #     for name, value in kids.__dict__.items():
    #         print(list(kids.__dict__.items()))
    #         if (
    #                 '__' not in name
    #                 and value is not None
    #                 and not isinstance(value, property)
    #                 and old_child is not None
    #         ):
    #             attr_name = QName(dc_style.ns[dc_style.NAMESPACE], name)
    #             old_child.set(attr_name, str(value.twips))
    children = {}
    for child in xml.getchildren():
        if isinstance(child, BaseOxmlElement):
            children[child._nsptag] = child
    for attr_name, (xml_elem_name, tag_name) in dc_style._style_attrs.items():
        old_child = children.get(f'{dc_style.NAMESPACE}:{xml_elem_name[1:]}')
        style_value = getattr(dc_style, attr_name)
        if (style_value is not None and not isinstance(style_value, property)
                and old_child is not None):
            attr_name = QName(dc_style.ns[dc_style.NAMESPACE], tag_name)
            if isinstance(style_value, Twips):
                old_child.set(attr_name, str(style_value.twips))
            elif isinstance(style_value, WD_ORIENTATION):
                old_child.set(attr_name, str(style_value.name.lower()))
