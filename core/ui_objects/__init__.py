# __init__.py
import pkgutil
import importlib
from .base import BaseDocx, BaseNonContainerDocx, BaseContainerDocx

CLASS_REGISTRY = {}
for _, module_name, _ in pkgutil.iter_modules(__path__):
    if module_name not in ['__main__', '__init__']:
        try:
            module = importlib.import_module(f'.{module_name}', __package__)

            for attr_name in dir(module):
                attr = getattr(module, attr_name)
                if isinstance(attr, type):
                    if issubclass(attr.__base__, (BaseNonContainerDocx, BaseContainerDocx)):
                        CLASS_REGISTRY[attr().tag] = attr

        except ImportError as e:
            print(f"Warning: Could not import {module_name}: {e}")

print(CLASS_REGISTRY)

from .paragraph import *
from .section import *
from .document import *

__all__ = [
    "BaseNonContainerDocx",
    "BaseDocx",
    "BaseContainerDocx",
    "Paragraph",
    "Section",
    "Text",
    "Run"
]
