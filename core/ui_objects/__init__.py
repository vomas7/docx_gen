# __init__.py
import importlib
import pkgutil

from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import LinkedObjects
from core.ui_objects.break_ import Break
from core.ui_objects.run import Run
from core.ui_objects.text import Text

CLASS_REGISTRY = {}
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name not in ["__main__", "__init__"]:
        try:
            module = importlib.import_module(f".{module_name}", __package__)

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type) and issubclass(attr.__base__, (
                        BaseContentTag, BaseContainerTag)):
                    CLASS_REGISTRY[attr().tag] = attr

        except ImportError as e:
            print(f"Warning: Could not import {module_name}: {e}")


__all__ = [
    "Run",
    "Text",
    "Break",
    "BaseTag",
    "LinkedObjects",
    "BaseContentTag",
    "BaseContainerTag",
]
