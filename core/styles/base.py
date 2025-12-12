# from abc import ABCMeta
# from dataclasses import dataclass
# from typing import get_type_hints
# from core.utils.metric_system import CM
#
#
# class StyleMeta(ABCMeta):
#     """A metaclass for automatically generating style properties."""
#
#     def __new__(cls, name, bases, namespace):
#         new_class = super().__new__(cls, name, bases, namespace)
#
#         annotations = get_type_hints(new_class)
#
#         if hasattr(new_class, "_style_attrs"):
#             for prop_name, (_attr, _field) in new_class._style_attrs.items():
#
#                 def getter(self, attr=_attr, field=_field):
#                     internal_obj = getattr(self, attr)
#                     return getattr(internal_obj, field)
#
#                 def setter(self, value, attr=_attr, field=_field):
#                     internal_obj = getattr(self, attr)
#                     value = CM(value) if isinstance(value, int | float) else value
#                     setattr(internal_obj, field, value)
#
#                 prop = property(getter)
#                 prop = prop.setter(setter)
#                 setattr(new_class, prop_name, prop)
#
#                 if prop_name in annotations:
#                     if not hasattr(new_class, "__annotations__"):
#                         new_class.__annotations__ = {}
#                     new_class.__annotations__[prop_name] = annotations[prop_name]
#
#         return new_class
#
#     def __call__(cls, *args, **kwargs):
#         if cls.__name__ == "BaseStyle":
#             raise TypeError("Cannot instantiate BaseStyle directly")
#         return super().__call__(*args, **kwargs)
#
#
# @dataclass
# class BaseStyle(metaclass=StyleMeta):
#     _style_attrs: dict
#
#     ns = {
#         "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
#         "c": "http://schemas.openxmlformats.org/drawingml/2006/chart",
#         "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
#         "dc": "http://purl.org/dc/elements/1.1/",
#         "dcmitype": "http://purl.org/dc/dcmitype/",
#         "dcterms": "http://purl.org/dc/terms/",
#         "dgm": "http://schemas.openxmlformats.org/drawingml/2006/diagram",
#         "m": "http://schemas.openxmlformats.org/officeDocument/2006/math",
#         "pic": "http://schemas.openxmlformats.org/drawingml/2006/picture",
#         "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
#         "sl": "http://schemas.openxmlformats.org/schemaLibrary/2006/main",
#         "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
#         "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
#         "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
#         "xml": "http://www.w3.org/XML/1998/namespace",
#         "xsi": "http://www.w3.org/2001/XMLSchema-instance",
#     }
#
#     NAMESPACE: str | None
#
#     def __init__(self, **kwargs):
#         if not self._style_attrs:
#             raise AttributeError("Style_tags and style_attrs must not be empty")
#         for key, value in kwargs.items():
#             if key not in self._style_attrs:
#                 raise AttributeError(f"Invalid property: {key}")
#             super().__setattr__(key, value)
#
#     def __setattr__(self, name, value):
#         style_tags = {i[0] for i in self._style_attrs.values()}
#         style_child = {i for i in self._style_attrs.keys()}
#         if name in style_tags or name in style_child:
#             super().__setattr__(name, value)
#         else:
#             raise AttributeError(f"Cannot add new attribute '{name}'")
