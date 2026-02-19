from core.ui_objects.base.base_attribute import BaseAttribute
from core.ui_objects.base.base_tag import BaseTag
from typing import Any

def find_name_attr(obj: BaseTag, target: str) -> str | None:
    """find attr name of class obj by xml attr name"""

    for attr_name in obj.__slots__:
        attr_obj = get_attribute(obj, attr_name)
        if isinstance(attr_obj, BaseAttribute) and attr_obj.xml_name == target:
            return attr_name
    return None

def get_attribute(obj, attribute: str) -> Any:
    return getattr(obj, attribute) if hasattr(obj, attribute) else None