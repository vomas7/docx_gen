from core.doc_objects.base import BaseContainElement, BaseTagElement
from typing import List
from core.doc_objects.base import BaseAttributeElement


class SI_Run(BaseContainElement):

    # todo Заполнить подходящими значениями Атрибуты и тэги
    """"""

    #todo убирается _init как вызывающий иницилизатор
    def _init(self,
                 children: List[BaseTagElement] = None,
                 attrs: List[BaseAttributeElement] = None):
        super()._init(children, attrs)
