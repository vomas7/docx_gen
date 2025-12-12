# __init__.py
import pkgutil
import importlib

from core.ui_objects.Run import Run
from core.ui_objects.Text import Text
from core.ui_objects.Break import Break

from core.ui_objects.base.BaseTag import BaseTag
from core.ui_objects.base.LinkedObjects import LinkedObjects
from core.ui_objects.base.BaseContentTag import BaseContentTag
from core.ui_objects.base.BaseContainerTag import BaseContainerTag


CLASS_REGISTRY = {}
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name not in ['__main__', '__init__']:
        try:
            module = importlib.import_module(f'.{module_name}', __package__)

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type):
                    if issubclass(attr.__base__, (BaseContentTag, BaseContainerTag)):
                        CLASS_REGISTRY[attr().tag] = attr

        except ImportError as e:
            print(f"Warning: Could not import {module_name}: {e}")

# print(CLASS_REGISTRY)


__all__ = [
    "BaseContentTag",
    "BaseTag",
    "BaseContainerTag",
    "Text",
    "Run",
    "Break"
]
