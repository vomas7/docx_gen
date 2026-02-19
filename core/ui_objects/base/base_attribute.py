from abc import abstractmethod
from enum import Enum
from typing import ClassVar
from core.utils.metrics import Length, Twips


class BaseAttribute:
    """Base attribute properties"""

    def __init__(self, xml_name: str):
        self._xml_name = xml_name

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, another):
        pass

    @property
    def xml_name(self):
        return self._xml_name


class EnumAttribute(BaseAttribute):
    """Base class for attributes with enum values"""

    _enum_class: ClassVar[type[Enum] | None] = None

    def __init_subclass__(cls, **kwargs):
        """check that Enum class is assigned in child"""
        super().__init_subclass__(**kwargs)

        enum_class = None
        for attr_name in dir(cls):
            attr_value = getattr(cls, attr_name)
            if (
                isinstance(attr_value, type)
                and issubclass(attr_value, Enum)
                and attr_value is not Enum
                and attr_value.__name__ == "Options"
            ):
                enum_class = attr_value
                break

        if enum_class is None:
            raise TypeError(
                f"{cls.__name__} must define an Enum class with name Options\n"
                f"Example:\n\n"
                f"class {cls.__name__}(EnumAttribute):\n"
                f"    class Options(Enum):\n"
                f"        left = 'left'\n"
                f"        center = 'center'"
            )
        cls._enum_class = enum_class

    def __init__(self, xml_name: str, value):
        if not self.validate(value):
            raise ValueError(f"Invalid value '{value}' for {self.__class__.__name__}")

        super().__init__(xml_name)
        self.value = value

    def validate(self, value) -> bool:
        if isinstance(value, Enum):
            if not isinstance(value, self._enum_class):
                return False
            return isinstance(value, self._enum_class)
        elif isinstance(value, str):
            value = value.strip().lower() if value else value
            return any(
                enum_item.value == value or enum_item.name == value
                for enum_item in self._enum_class
            )
        elif value is None:
            return any(enum_item.value is None for enum_item in self._enum_class)

        return False

    def _convert_to_value(self, value) -> str | None:
        if isinstance(value, Enum):
            if not isinstance(value, self._enum_class):
                raise TypeError(
                    f"Expected {self._enum_class.__name__}, got {type(value).__name__}"
                )
            return value.value
        elif isinstance(value, str):
            return getattr(self._enum_class, value.strip().lower()).value
        elif value is None and value in {v.value for v in self._enum_class}:
            return None
        else:
            raise TypeError("Unable to determine value!")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        value = self._convert_to_value(new_value)
        if not self.validate(value):
            allowed = [e.value for e in self._enum_class]
            raise ValueError(f"Invalid value '{value}'. Allowed: {allowed}")
        self._value = value


class BooleanAttribute(BaseAttribute):
    def __init__(self, xml_name: str, value):
        super().__init__(xml_name)
        self.name = xml_name
        self.value = value

    @property
    def value(self) -> str:
        if isinstance(self._value, bool):
            return str(self._value).lower()
        else:
            raise TypeError(
                f"Attribute {self.name} "
                f"has two states True|False "
                f"not {type(self._value)}!"
            )

    @value.setter
    def value(self, another):
        if isinstance(another, bool):
            self._value = another
        else:
            raise TypeError(
                f"Attribute {self.name} has two states True|False not {type(another)}!"
            )


class SimpleAttribute(BaseAttribute):
    def __init__(self, xml_name: str, value: str | int | float):
        self._value = value
        super().__init__(xml_name)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, another: str | int | float):
        if isinstance(another, str) and another.isdecimal():
            self._value = another
        elif isinstance(another, int | float):
            self._value = str(another)
        else:
            TypeError(f"another must be str or int not {type(another)}")


class SizeAttribute(BaseAttribute):
    def __init__(self, xml_name: str, value: Length):
        self.value = value
        super().__init__(xml_name)

    @property
    def value(self) -> Length:
        return self._value

    @value.setter
    def value(self, new_value: Length):
        if isinstance(new_value, Length):
            self._value = new_value
        TypeError(f"value must be Length not {type(new_value)}")


class TwipsAttribute(SizeAttribute):
    def __init__(self, xml_name: str, value: Length):
        super().__init__(xml_name, value)

    @property
    def value(self) -> Twips:
        return self._value.twips

    @value.setter
    def value(self, new_value: Length):
        SizeAttribute.value.fset(self, new_value)
