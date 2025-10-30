from typing import Any, Set
from core.exceptions.validation import ValidationError


def validate_access_elem(val: Any, access_val: Set[Any]):
    if not isinstance(val, tuple(access_val)):
        raise ValidationError(
            f"Element '{val}' not allowed! Valid are: {access_val}"
        )
