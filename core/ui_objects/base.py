# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import FrozenSet, Type, List

from core.doc_objects.base import BaseMurkupElement
from core.utils.v_objects import MiddlewareArray
from core.validators.xml_components import validate_access_elem
from core.utils.annotaions import annotation_catcher

class BaseDocx:

    def __init__(self, si_element: BaseMurkupElement):
        self.si_element = si_element
        self.parent = None


class BaseContainerDocx(BaseDocx):
    # all  <BaseDocx> elements are available by default
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })

    def __init__(self,
                 si_element,
                 linked_objects: List[BaseDocx] = None):

        super().__init__(si_element)

        _object_actions = {validate_access_elem, self.__assign_parent}
        self._linked_objects = MiddlewareArray(
            iterable=linked_objects,
            actions=_object_actions,
            access_val=self.ACCESS_CHILDREN
        )
    @annotation_catcher("self", "value")
    @staticmethod
    def __assign_parent(args):
        if not isinstance(args.value, BaseDocx):
            raise TypeError(f"{args.value} is not a BaseDocx instance")
        args.value.parent = args.self

class BaseNonContainerDocx(BaseDocx):
    pass
