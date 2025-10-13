from typing import Union
from abc import ABC, abstractmethod
from docx.oxml.xmlchemy import BaseOxmlElement


class BaseDOC:

    def __init__(self):
        self.parent = None

    def validate_annotation(self, **kwargs):
        """
            args:
                obj: class instance
                **kwargs: key-value pairs for checking received arguments
        """
        # todo не обрабатываает генерики

        if not kwargs:
            raise ValueError("arguments are required")
        annotation = self.__init__.__annotations__

        for key, value in kwargs.items():
            if key not in annotation:
                continue

            if not isinstance(value, annotation[key]):
                raise AttributeError(
                    f"Creating {self} object failed: "
                    f"Unknown source {type(value)}!"
                )


class BaseContainerDOC(BaseDOC, ABC):
    CONTAIN_TYPES = Union[BaseDOC]

    def __init__(self):
        super().__init__()
        self._linked_objects = []

    def insert_linked_object(self,
                             value: CONTAIN_TYPES,
                             index: int | None = None):
        if not isinstance(value, self.CONTAIN_TYPES):
            # noqa
            raise TypeError(f'linked_objects must be a {self.CONTAIN_TYPES}')
        value.parent = self
        if index is not None:
            self._linked_objects.insert(index, value)
        else:
            self._linked_objects.append(value)

    @property
    def linked_objects(self):
        return self._linked_objects

    @linked_objects.setter
    def linked_objects(self, value):
        self._linked_objects = value

    def remove_linked_object(self, index: int = - 1):
        _elem = self._linked_objects.pop(index)
        _elem.parent = None
        return _elem

    @staticmethod
    @abstractmethod
    def convert_to_linked_object(elem):
        """abstract implementation of stored object transformation"""
        pass


class BaseNonContainerDOC(BaseDOC):
    # todo soon!
    pass
