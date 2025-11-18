from docx.oxml import CT_P, CT_Body, CT_R, CT_SectPr, CT_Text, CT_Document, CT_PageSz, CT_PageMar, CT_HdrFtr, CT_HdrFtrRef
from core.doc_objects.text import SI_Text
from core.doc_objects.section import SI_SectPr, SI_PageSz, SI_PageMar
from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.run import SI_Run
from core.doc_objects.document import SI_Body
from core.doc_objects.document import SI_Document

from typing import TYPE_CHECKING
from docx.oxml.xmlchemy import BaseOxmlElement

if TYPE_CHECKING:
    from core.doc_objects.base import BaseMurkupElement

from typing import Optional
from lxml import etree

# todo is temporary solution, in future need to migrate to own objects
# todo it required for clean logic and independent project

assign_si = {
    CT_R: SI_Run,
    CT_SectPr: SI_SectPr,
    CT_Body: SI_Body,
    CT_Text: SI_Text,
    CT_P: SI_Paragraph,
    CT_Document: SI_Document,
    CT_PageMar: SI_PageMar,
    CT_PageSz: SI_PageSz
}


def FromOxml(elem: "BaseOxmlElement") -> Optional["BaseMurkupElement"]:
    if isinstance(elem, BaseOxmlElement):
        return assign_si[elem.__class__]()
    raise TypeError(f"Unsupported element type: {type(elem)}")


def convert_to_Si(oxml_elem: "BaseOxmlElement") -> "BaseMurkupElement":
    si_element = FromOxml(oxml_elem)
    for child in oxml_elem:
        si_element.children.append(convert_to_Si(child))
    return si_element
