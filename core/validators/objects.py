from typing import Any, Iterable
def obj_has_all_attrs(_cls: Any, attrs: Iterable) -> bool:
    return all(map(lambda x: hasattr(_cls, x), attrs))
