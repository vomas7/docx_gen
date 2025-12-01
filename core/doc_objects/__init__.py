# from core.utils.tracker_mixin import RelationDefMeta as _RelationDefMeta

from core.doc_objects.base import (
    BaseTagElement,
    BaseMarkupElement,
    BaseContainElement,
    BaseAttributeElement,
    BaseNonContainElement,
)
# todo .....

from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.run import SI_Run
from core.doc_objects.text import SI_Text
from core.doc_objects.document import SI_Document, SI_Body
from core.doc_objects.section import (
    SI_docGrid,
    SI_cols,
    SI_PageMar,
    SI_PageSz,
    SI_HdrFtrRef,
    SI_HdrFtr,
    SI_SectPr
)

# _RelationDefMeta.initialize_relations()

from core.oxml_magic.parser import register_element_cls

#
# # ---------------------------------------------------------------------------
#

register_element_cls("w:r", SI_Run)
register_element_cls("w:p", SI_Paragraph)
register_element_cls("w:t", SI_Text)

register_element_cls("w:SectPr", SI_SectPr)
register_element_cls("w:docGrid", SI_docGrid)
register_element_cls("w:cols", SI_cols)
register_element_cls("w:pgMar", SI_PageMar)
register_element_cls("w:pgSz", SI_PageSz)
register_element_cls("w:headerReference", SI_HdrFtrRef)
register_element_cls("w:footerReference", SI_HdrFtrRef)
register_element_cls("w:hdr", SI_HdrFtr)
register_element_cls("w:ftr", SI_HdrFtr)


register_element_cls("w:document", SI_Document)
register_element_cls("w:body", SI_Body)


