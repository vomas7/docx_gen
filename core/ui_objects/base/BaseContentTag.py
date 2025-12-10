from abc import abstractmethod
from core.ui_objects.base.BaseTag import BaseTag


class BaseContentTag(BaseTag):
    __slots__: tuple = ()

    @property
    @abstractmethod
    def tag(self) -> str:
        """Must be implemented in child"""
        pass
