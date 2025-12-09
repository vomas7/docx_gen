from abc import abstractmethod


class BaseTag:

    __slots__: tuple = ()
    default_namespace: str = "w"
    """
         Abstract base class for XML tag representation.
         All concrete tag classes must:
         1. Define __slots__ containing the tag's attributes
         2. Implement the 'tag' property returning the tag name
         3. Initialize all slot attributes in __init__
         The class automatically converts slot-based attributes
         into XML attribute dictionary with proper namespace prefixes.
     """

    @property
    @abstractmethod
    def tag(self):
        pass

    @property
    def attrs(self):
        slots = getattr(self, '__slots__', ())
        if not slots:
            raise AttributeError(f"Class {self.__class__.__name__} "
                                 f"must define non-empty __slots__")
        attrs = dict()
        for attribute_property in slots:
            attr_name = attribute_property.replace("_", "")
            attr_value = getattr(self, attr_name)
            attrs[f'{self.default_namespace}:{attr_name}'] = attr_value
        return attrs

    def __str__(self):
        attrs = self.attrs
        attrs_str = ' '.join(
            f'{key}="{value}"' for key, value in attrs.items()
        )
        return f"{self.__class__.__name__}: <{self.tag} {attrs_str}/>"
