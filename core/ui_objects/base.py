# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import FrozenSet, Type, List
import copy

from core.doc_objects.base import BaseTagElement, BaseContainElement
from core.utils.v_objects import MiddlewareArray
from core.validators.v_objects import validate_access_type
from core.utils.annotaions import annotation_catcher
from abc import abstractmethod, ABC


class BaseDocx(ABC):

    def __init__(self):
        self.parent = None


class BaseContainerDocx(BaseDocx):
    # all  <BaseDocx> elements are available by default
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })

    def __init__(self,
                 linked_objects: List[BaseDocx] = None):
        super().__init__()

        self.linked_objects = linked_objects or []

    def add(self, elem):
        self.linked_objects.append(elem)


class BaseNonContainerDocx(BaseDocx):
    pass
