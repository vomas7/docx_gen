# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import FrozenSet, Type, List
import copy

from core.doc_objects.base import (
    BaseMurkupElement,
    BaseContainElement,
    BaseNonContainElement
)
from core.utils.v_objects import MiddlewareArray
from core.validators.xml_components import validate_access_elem
from core.utils.annotaions import annotation_catcher
from abc import abstractmethod, ABC


class BaseDocx(ABC):

    def __init__(self, si_element: BaseMurkupElement):
        self._si_element = si_element
        self.parent = None

    @property
    def si_element(self):
        return copy.deepcopy(self._si_element)

    def to_SI_element(self) -> BaseMurkupElement:
        return self._to_SI_element()

    @abstractmethod
    def _to_SI_element(self) -> BaseMurkupElement:
        pass


class BaseContainerDocx(BaseDocx):
    # all  <BaseDocx> elements are available by default
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })

    def __init__(self,
                 si_element: BaseContainElement,
                 linked_objects: List[BaseDocx] = None):
        super().__init__(si_element)

        _object_actions = {validate_access_elem, self.__assign_parent}
        self.linked_objects = MiddlewareArray(
            iterable=linked_objects,
            actions=_object_actions,
            access_val=self.ACCESS_CHILDREN
        )

    def _to_SI_element(self) -> BaseMurkupElement:
        _si_element = self.si_element
        for child in self.linked_objects:
            _si_element.children.append_or_extend(child.to_SI_element())
        return _si_element

    @annotation_catcher("self", "value")
    @staticmethod
    def __assign_parent(args):
        if not isinstance(args.value, BaseDocx):
            raise TypeError(f"{args.value} is not a BaseDocx instance")
        args.value.parent = args.self


class BaseNonContainerDocx(BaseDocx):

    def _to_SI_element(self) -> BaseMurkupElement:
        return self.si_element
