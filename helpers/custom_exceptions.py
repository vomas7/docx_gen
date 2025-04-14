class CellSelectionValidationError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class ColumnValueError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
