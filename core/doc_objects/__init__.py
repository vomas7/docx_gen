from core.utils.tracker_mixin import RelationDefMeta as _RelationDefMeta

from core.doc_objects.base import (
    BaseTagElement,
    BaseMarkupElement,
    BaseContainElement,
    BaseAttributeElement,
    BaseNonContainElement,
)
#todo .....

from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.run import SI_Run
# from core.doc_objects.section import (
#     SI_docGrid,
#     SI_cols,
#     SI_PageMar,
#     SI_PageSz,
#     SI_HdrRef,
#     SI_FtrRef,
#     SI_Hdr,
#     SI_Ftr,
# )

# _RelationDefMeta.initialize_relations()

from docx.oxml.parser import register_element_cls
#
# # ---------------------------------------------------------------------------
# # DrawingML-related elements
#
register_element_cls("w:r", SI_Run)
register_element_cls("w:p", SI_Paragraph)
# register_element_cls("w:docGrid", SI_docGrid)
# register_element_cls("w:cols", SI_cols)
# register_element_cls("w:pgMar", SI_PageMar)
# register_element_cls("w:pgSz", SI_PageSz)
# register_element_cls("w:headerReference", SI_HdrRef)
# register_element_cls("w:footerReference", SI_FtrRef)
# register_element_cls("w:hdr", SI_Hdr)
# register_element_cls("w:ftr", SI_Ftr)
