from decimal import Decimal


class TableTransformer:
    """
    Класс формирует удобную структуру для заполнения таблиц,
    а также реализует логику некоторых таблиц со сложной структурой.
    """

    @staticmethod
    def stringify_digits(value: int | float | Decimal, round_to: int) -> str:
        return str(round(Decimal(str(value)), round_to)).replace(".", ",")

    @staticmethod
    def find_same_row_indexes(table_engine, col_idx: int) -> list[list[int]]:
        prev_sell = None
        merge_row_indexes = list()
        for index, cell in enumerate(table_engine.column_cells(col_index=col_idx)):
            if prev_sell and cell.text == prev_sell.text:
                if merge_row_indexes and index - 1 in merge_row_indexes[-1]:
                    merge_row_indexes[-1].pop()
                    merge_row_indexes[-1].append(index)
                else:
                    merge_row_indexes.append([index - 1, index])
            prev_sell = cell
        return merge_row_indexes

    @staticmethod
    def is_section_delimiter(row) -> bool:
        return bool(row.cells[-1].text)

    @staticmethod
    def is_upper_level_number(text: str, level: int) -> bool:
        numbers = [num for num in text.split(".") if num != ""]
        return len(numbers) == level
