from typing import List, Dict, Any

def serialize_ns_to_obj(ns: Dict[str, Any], attrs: List[str]) -> Any:
    return [ns.get(attr) for attr in attrs]
