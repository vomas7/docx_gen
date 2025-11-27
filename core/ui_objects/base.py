# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import FrozenSet, Type, List
import copy

from core.doc_objects.base import BaseTagElement, BaseContainElement
from core.utils.v_objects import MiddlewareArray
from core.validators.v_objects import validate_access_type
from core.utils.annotaions import annotation_catcher
from abc import abstractmethod, ABC


class BaseDocx(ABC):

    def __init__(self, si_element: BaseTagElement):
        self._si_element = si_element
        self.parent = None

    @property
    def si_element(self):
        return copy.deepcopy(self._si_element)

    def to_SI_element(self) -> BaseTagElement:
        return self._to_SI_element(self.si_element)

    @abstractmethod
    def _to_SI_element(
            self,
            si_element: "BaseTagElement") -> BaseTagElement:
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

        _object_actions = {validate_access_type, self.__assign_parent}
        self.linked_objects = MiddlewareArray(
            iterable=linked_objects,
            actions=_object_actions,
            access_val=self.ACCESS_CHILDREN
        )

    def add(self, elem):
        self.linked_objects.append(elem)

    def _to_SI_element(self, si_element) -> BaseTagElement:
        for child in self.linked_objects:
            si_element.children.append_or_extend(child.to_SI_element())
        return si_element

    @annotation_catcher("self", "value")
    @staticmethod
    def __assign_parent(args):
        if not isinstance(args.value, BaseDocx):
            raise TypeError(f"{args.value} is not a BaseDocx instance")
        args.value.parent = args.self


class BaseNonContainerDocx(BaseDocx):

    def _to_SI_element(self, si_element) -> BaseTagElement:
        return si_element
