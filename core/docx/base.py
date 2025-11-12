# todo remove duplicate logic with base elements in low-level and high-level elements!

from typing import Union, FrozenSet, Type, List
from abc import ABC, abstractmethod
from docx.oxml.xmlchemy import BaseOxmlElement

from core.doc_objects.base import BaseMurkupElement
from core.validators.v_objects import MiddlewareArray
from core.validators.xml_components import validate_access_elem


class BaseDocx:

    def __init__(self, si_element: BaseMurkupElement):
        self.si_element = si_element
        self.parent = None


class BaseContainerDocx(BaseDocx):
    # all  <BaseDocx> elements are available by default
    ACCESS_CHILDREN: FrozenSet[Type[BaseDocx]] = frozenset({
        BaseDocx
    })
    __tag_validators = {validate_access_elem, }

    def __init__(self,
                 si_element,
                 linked_objects: List[BaseDocx] = None):
        super().__init__(si_element)
        self._linked_objects = MiddlewareArray(
            iterable=linked_objects,
            validator=self.__tag_validators,
            access_val=self.ACCESS_CHILDREN
        )


class BaseNonContainerDocx(BaseDocx):
    pass
