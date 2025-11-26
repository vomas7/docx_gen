from core.utils.tracker_mixin import RelationDefMeta as _RelationDefMeta


from core.doc_objects.paragraph import SI_Paragraph
from core.doc_objects.run import SI_Run
from core.doc_objects.base import BaseTagElement, BaseAttributeElement, \
    BaseMarkupElement, BaseNonContainElement, BaseContainElement



_RelationDefMeta.initialize_relations()