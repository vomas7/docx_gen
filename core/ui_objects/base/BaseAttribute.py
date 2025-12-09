from enum import Enum
from abc import abstractmethod
from typing import ClassVar, Optional, Type, Any


class BaseAttribute:
    """Base attribute properties"""

    def __init__(self,
                 namespace: str,
                 xml_name: str,
                 name: str,
                 value: str):
        self._namespace = namespace
        self._xml_name = xml_name
        self._name = name
        self._value = value

    @property
    @abstractmethod
    def value(self):
        pass

    @value.setter
    @abstractmethod
    def value(self, another):
        pass

    @property
    def namespace(self):
        return self._namespace

    @property
    def name(self):
        return self._name

    @property
    def xml_name(self):
        return self._xml_name


class EnumAttribute(BaseAttribute):
    """Base class for attributes with enum values"""

    _enum_class: ClassVar[Optional[Type[Enum]]] = None

    def __init_subclass__(cls, **kwargs):
        """check that Enum class is assigned in child"""
        super().__init_subclass__(**kwargs)

        enum_class = None
        for attr_name in dir(cls):
            attr_value = getattr(cls, attr_name)
            if (isinstance(attr_value, type)
                    and issubclass(attr_value, Enum)
                    and attr_value is not Enum):
                enum_class = attr_value
                break

        if enum_class is None:
            raise TypeError(
                f"{cls.__name__} must define an Enum class. "
                f"Example:\n\n"
                f"class {cls.__name__}(EnumAttribute):\n"
                f"    class Align(Enum):\n"
                f"        LEFT = 'left'\n"
                f"        CENTER = 'center'"
            )
        cls._enum_class = enum_class

    def __init__(self,
                 namespace: str,
                 xml_name: str,
                 name: str,
                 value: str):
        if not self._validate_enum_value(value):
            raise ValueError(
                f"Invalid value '{value}' for {self.__class__.__name__}"
            )
        super().__init__(namespace, xml_name, name, value)

    def _validate_enum_value(self, value: str) -> bool:
        return any(
            enum_item.value == value or enum_item.name == value
            for enum_item in self._enum_class
        )

    def _convert_to_string(self, value: Any) -> str:
        """Конвертирует значение в строку, принимая как строки, так и Enum."""
        if isinstance(value, Enum):
            # Если передали Enum член, берем его значение
            if not isinstance(value, self._enum_class):
                raise TypeError(
                    f"Expected {self._enum_class.__name__}, "
                    f"got {type(value).__name__}"
                )
            return value.value
        elif isinstance(value, str):
            return value.strip().lower()
        else:
            return str(value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        value_str = self._convert_to_string(new_value)
        if not self._validate_enum_value(value_str):
            allowed = [e.value for e in self._enum_class]
            raise ValueError(
                f"Invalid value '{value_str}'. "
                f"Allowed: {allowed}"
            )
        self._value = value_str
