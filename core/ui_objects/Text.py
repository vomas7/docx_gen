from core.ui_objects.base.BaseContentTag import BaseContentTag


class Text(BaseContentTag):
    """tag <w:t> text assignment"""

    def __init__(self, text: str = ''):
        self._text = text

    def __str__(self) -> str:
        return f'Text({self._text})'

    def __repr__(self) -> str:
        return self.__str__()

    @property
    def text(self):
        return self._text

    @property
    def tag(self) -> str:
        return 'w:t'

