from typing import List, Dict, Any


def serialize_ns_to_obj(ns: Dict[str, Any], attr: str) -> List[Any]:
    ns_name = ns.get("__name__")
    if ns_name is None:
        raise TypeError("A namespace must be correct!")
    ns_obj = ns.get(attr)
    if ns_obj is None:
        raise AttributeError(
            f"attribute `{attr}` is not available in {ns_name}"
        )
    return ns_obj