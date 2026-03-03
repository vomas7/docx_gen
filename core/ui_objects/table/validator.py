from types import NoneType

TABLE_COLUMNS_MAX_COUNT = 64


def validate_word_table_rows(rows_count: int) -> None | ValueError:
    if isinstance(rows_count, NoneType):
        return None
    return validate_positive_integer_number(rows_count)


def validate_word_table_columns(columns_count: int) -> None | ValueError:
    if isinstance(columns_count, NoneType):
        return None
    validate_positive_integer_number(columns_count)
    if not is_less_than_max_columns(columns_count):
        raise ValueError(f"Num of columns must be less than {TABLE_COLUMNS_MAX_COUNT}")
    return None


def validate_positive_integer_number(number: int) -> None | ValueError:
    if not isinstance(number, int) or not is_positive_number(number):
        raise ValueError("Number of rows or cols must be POSITIVE INTEGER!")


def is_positive_number(number: int) -> bool:
    return number > 0


def is_less_than_max_columns(number: int) -> bool:
    return number < TABLE_COLUMNS_MAX_COUNT
