from collections import namedtuple

from helpers.custom_exceptions import CellSelectionValidationError


class CellSelection:
    """
    Класс для хранения, валидации и передачи индексов ячеек,
    которые будут сливаться.
    """

    def __init__(self, c1: namedtuple, c2: namedtuple, max_row: int, max_col: int):
        """
        Здесь реализуется валидация индексов ячеек, которые будут сливаться.
        """
        self.c1 = c1
        self.c2 = c2
        self.max_col = max_col
        self.max_row = max_row
        self.indexes = [c1.col, c1.row, c2.col, c2.row]
        self.validate()

    def validate(self):
        """Проверка возможных ошибок."""
        if any([self.is_negative(index) for index in self.indexes]):
            raise CellSelectionValidationError("Indexes can't be negative!")

        if self.is_same_cell():
            raise CellSelectionValidationError("Can not merge same cell!")

        if self.is_gt_max(self.c1.col, self.max_col):
            raise CellSelectionValidationError(
                f"col: {self.c1.col} > max_col: {self.max_col}"
            )

        if self.is_gt_max(self.c2.col, self.max_col):
            raise CellSelectionValidationError(
                f"col: {self.c2.col} > max_col: {self.max_col}"
            )

        if self.is_gt_max(self.c1.row, self.max_row):
            raise CellSelectionValidationError(
                f"row: {self.c1.row} > max_row: {self.max_row}"
            )

        if self.is_gt_max(self.c2.row, self.max_row):
            raise CellSelectionValidationError(
                f"row: {self.c2.row} > max_row: {self.max_row}"
            )

        if not self.is_start_col_lte_stop():
            raise CellSelectionValidationError(
                f"column index of stop cell can't be lower than start cell"
                f"stop_col:{self.c2.col} < start_col:{self.c1.col}"
            )

        if not self.is_start_row_lte_stop():
            raise CellSelectionValidationError(
                f"row index of stop cell can't be lower than start cell"
                f"stop_row:{self.c2.row} < start_row:{self.c1.row}"
            )

    @staticmethod
    def is_negative(index: int):
        """Проверка на отрицательность индекса."""
        return index < 0

    def is_same_cell(self):
        """Проверка на одинаковость ячеек."""
        return (self.c1.col, self.c1.row) == (self.c2.col, self.c2.row)

    def is_start_col_lte_stop(self):
        """Проверка, что индекс колонки 1 ячейки меньше (либо равен) второй."""
        return self.c1.col <= self.c2.col

    def is_start_row_lte_stop(self):
        """Проверка, что индекс строки 1 ячейки меньше (либо равен) второй."""
        return self.c1.row <= self.c2.row

    @staticmethod
    def is_gt_max(cell, max_cell):
        """Проверка, что индексы ячеек больше максимальных значений."""
        return cell > max_cell
