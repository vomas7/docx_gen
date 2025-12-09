from collections import UserString
from core.ui_objects.base.BaseContentTag import BaseContentTag


class Text(UserString, BaseContentTag):
    """tag <w:t> text assignment"""

    def __init__(self, text: str = ''):
        super().__init__(seq=text)

    def __str__(self) -> str:
        return f'Text({self.data})'

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def tag(self) -> str:
        return 'w:t'
