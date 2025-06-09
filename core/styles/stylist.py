from abc import abstractmethod
from typing import TYPE_CHECKING
from dataclasses import asdict

from docx.oxml.xmlchemy import BaseOxmlElement

from core.styles.base import BaseStyle
from core.styles.section_style import SectionStyle
from lxml import etree
from lxml.etree import _Element

class Stylist:
    """Mixin class to provide methods of applying and retrieve style for object."""

    # @abstractmethod
    @staticmethod
    def style(xml: _Element, dc_style: SectionStyle):
        # attrs_dict = asdict(dc_style)
        # attr = list(attrs_dict.keys())[0]
        # setattr(cls, attr, attrs_dict[attr])
        print(xml.xml)
        ns = {
            'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
            'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
            'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
            'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
        }
        from lxml.etree import QName
        attr_name = QName(ns['w'], "left")
        # self._sectPr.pgMar.set(attr_name, str(dc_style.left_margin.twips))

        # print(dc_style.__dict__)
        for parent, childs in dc_style.__dict__.items():
            # parent = QName(ns['w'], parent)
            # print(xml.getchildren())
            childrens = {}
            for i in xml.getchildren():
                if isinstance(i, BaseOxmlElement):
                    childrens[i._nsptag] = i
                    print(i._nsptag)
                else:
                    print(i)
            old_child = childrens['w:' + parent]
            print(old_child)
            for name, value in childs.__dict__.items():
                if value:
                    attr_name = QName(ns['w'], name)
                    old_child.set(attr_name, str(value.twips))

        print(xml.xml)
        # attr_name = QName(ns['w'], "left")
        # print(SectionStyle.__dataclass_fields__.keys())
        # self._sectPr.pgMar.set(attr_name, str(dc_style.left_margin.twips))
        # super().style(dc_style)


from docx.shared import Cm, Length, Mm


class CM:
    """Class for only Russian cool gays"""
    def __new__(cls, cm: float):
        return Length(Cm(cm))


class MM:
    """Class for only Russian cool gays"""
    def __new__(cls, mm: float):
        return Length(Mm(mm))
