from typing import Any, Set

def validate_access_elem(val: Any, access_val: Set[Any]) -> bool:
    return type(val) in access_val
