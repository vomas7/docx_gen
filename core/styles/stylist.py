from docx.oxml.xmlchemy import BaseOxmlElement
from core.styles.base import BaseStyle
from lxml.etree import _Element
from lxml.etree import QName


def set_style(xml: _Element, dc_style: BaseStyle):
    """
    A function for changing tag attributes in xml related to the element style,
    for use in docx-gen element classes
    """
    for parent, kids in dc_style.__dict__.items():
        children = {}
        for child in xml.getchildren():
            if isinstance(child, BaseOxmlElement):
                children[child._nsptag] = child
        old_child = children.get(f'{dc_style.NAMESPACE}:{parent[1:]}')
        for name, value in kids.__dict__.items():
            if (
                    '__' not in name
                    and value is not None
                    and not isinstance(value, property)
                    and old_child is not None
            ):
                attr_name = QName(dc_style.ns[dc_style.NAMESPACE], name)
                old_child.set(attr_name, str(value.twips))
