from core.doc_objects.base import BaseAttributeElement
from docx.oxml.simpletypes import ST_TwipsMeasure
from typing import Type
from docx.enum.base import BaseXmlEnum
from docx.oxml.simpletypes import BaseSimpleType
from docx.oxml.ns import nsmap
from core.utils.factories import attr_factory
from core.doc_objects.base import BaseAttributeElement


SI_Right = attr_factory("w:right", simple_type=ST_TwipsMeasure, parent_cls=BaseAttributeElement)
SI_Top = attr_factory("w:top", simple_type=ST_TwipsMeasure, parent_cls=BaseAttributeElement)

# SI_Left = attr_factory(attr_name="w:left")
# SI_Top = attr_factory(attr_name="w:top")
# SI_Bottom = attr_factory(attr_name="w:bottom")
