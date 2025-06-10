from dataclasses import dataclass
from typing import get_type_hints


@dataclass
class BaseStyle:
    NAMESPACE: str | None = None
    ns = {
        'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
        'wp': 'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
        'a': 'http://schemas.openxmlformats.org/drawingml/2006/main',
        'r': 'http://schemas.openxmlformats.org/officeDocument/2006/relationships'
    }


class StyleMeta(type):
    """A metaclass for automatically generating style properties."""

    def __new__(cls, name, bases, namespace):

        new_class = super().__new__(cls, name, bases, namespace)

        annotations = get_type_hints(new_class)

        if hasattr(new_class, "_style_attrs"):
            for prop_name, (_attr, _field) in new_class._style_attrs.items():
                def getter(self, attr=_attr, field=_field):
                    internal_obj = getattr(self, attr)
                    return getattr(internal_obj, field)

                def setter(self, value, attr=_attr, field=_field):
                    internal_obj = getattr(self, attr)
                    setattr(internal_obj, field, value)

                prop = property(getter)
                prop = prop.setter(setter)
                setattr(new_class, prop_name, prop)

                if prop_name in annotations:
                    if not hasattr(new_class, "__annotations__"):
                        new_class.__annotations__ = {}
                    new_class.__annotations__[prop_name] = annotations[prop_name]

        return new_class
