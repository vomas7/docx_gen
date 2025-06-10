from docx.oxml.xmlchemy import BaseOxmlElement
from core.styles.section_style import SectionStyle
from lxml.etree import _Element


class Stylist:
    """Mixin class to provide methods of applying and retrieve style for object."""

    def style(self, xml: _Element, dc_style: SectionStyle):
        from lxml.etree import QName
        for parent, childs in dc_style.__dict__.items():
            childrens = {}
            for i in xml.getchildren():
                if isinstance(i, BaseOxmlElement):
                    childrens[i._nsptag] = i
            old_child = childrens['w:' + parent]
            for name, value in childs.__dict__.items():
                if value:
                    namespace, clean_attr_name = name.split("_")[0], name.split("_")[1]
                    attr_name = QName(dc_style.ns[namespace], clean_attr_name)
                    old_child.set(attr_name, str(value.twips))
