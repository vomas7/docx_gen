"""Module for automatic registration of UI objects."""

import importlib
import pkgutil

from typing import Any

from core.ui_objects.base.base_attribute import BaseAttribute
from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.base_tag import BaseTag
from core.ui_objects.base.linked_objects import LinkedObjects
from core.ui_objects.break_ import Break
from core.ui_objects.document import Body, Document
from core.ui_objects.paragraph import Paragraph, ParagraphProperty
from core.ui_objects.run import Run, RunProperty
from core.ui_objects.section import Section
from core.ui_objects.text import Bold, Font, Italic, Tab, Text

CLASS_REGISTRY: dict[str, dict[str, Any]] = {}


def _is_valid_tag_class(cls: type) -> bool:
    """Checks if a class is a content or container tag."""
    return isinstance(cls, type) and issubclass(
        cls.__base__, (BaseContentTag, BaseContainerTag)
    )


def _extract_slot_attributes(cls: type) -> list:
    """Extracts attribute classes from class slots."""
    if not hasattr(cls, "__slots__"):
        return []

    attributes = []

    for slot_name in cls.__slots__:
        try:
            attribute = cls.get_attribute(slot_name)
            if isinstance(attribute, BaseAttribute):
                attributes.append(attribute.__class__)
        except (AttributeError, TypeError):
            continue
    return attributes


def _register_module_classes(module, initialized_classes: list) -> None:
    """Registers all suitable classes from a module."""
    for attr_name in dir(module):
        attr = getattr(module, attr_name)

        if not _is_valid_tag_class(attr):
            continue
        if attr_name in initialized_classes:
            continue
        else:
            initialized_classes.append(attr_name)

        try:
            instance = attr()
            tag = instance.tag
            attrs = _extract_slot_attributes(instance)

            CLASS_REGISTRY[tag] = {"class_tag": attr, "attrs": attrs}
        except Exception as e:
            print(f"Warning: Could not register class {attr_name}: {e}")


def _discover_and_register() -> None:
    """Discovers and registers all classes in the package."""
    initialized_classes = []
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        if module_name in ("__main__", "__init__"):
            continue

        try:
            module = importlib.import_module(f".{module_name}", __package__)
            _register_module_classes(module, initialized_classes)
        except ImportError as e:
            print(f"Warning: Could not import {module_name}: {e}")


_discover_and_register()

__all__ = [
    "Run",
    "Text",
    "Break",
    "BaseTag",
    "LinkedObjects",
    "BaseContentTag",
    "BaseContainerTag",
    "CLASS_REGISTRY",
    "Document",
    "Body",
    "Section",
    "Paragraph",
    "ParagraphProperty",
    "RunProperty",
    "Bold",
    "Italic",
    "Tab",
    "Font",
]
