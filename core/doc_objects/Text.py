

class Text:
    def __init__(self, text: str, style):
        self._text = text
        self._style = style
        self._iid = None

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        if not isinstance(value, str):
            raise AttributeError(f"value must be str not {type(value)}!")
        else:
            self._text = value
