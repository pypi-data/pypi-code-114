"""
Sarmat.

Описание сущностей.

Базовая сущность.
"""
from dataclasses import asdict, dataclass, fields, is_dataclass
from typing import _GenericAlias


def nested_dataclass(*args, **kwargs):
    """Декоратор подменяет метод __init__ для сборки вложенных структур"""
    def wrapper(cls):
        check_cls = dataclass(cls, **kwargs)
        orig_init = cls.__init__

        def __init__(self, *args, **kwargs):
            for name, value in kwargs.items():
                # Определяем тип поля
                field_type = cls.__annotations__.get(name, None)
                # Обработка вложенных структур
                if isinstance(field_type, str) and field_type == cls.__name__:
                    field_type = cls
                is_data_class = is_dataclass(field_type)

                if isinstance(value, (list, tuple, set)):
                    if isinstance(field_type, list):
                        field_type = field_type[0]
                    elif isinstance(field_type, _GenericAlias):
                        field_type = field_type.__args__[0]

                    if isinstance(field_type, str) and field_type == cls.__name__:
                        field_type = cls

                    is_data_class = is_dataclass(field_type)
                    value = [
                        field_type(**item) if is_data_class and isinstance(item, dict) else item
                        for item in value
                    ]
                    kwargs[name] = value
                elif is_data_class and isinstance(value, dict):
                    kwargs[name] = field_type(**value)

                orig_init(self, *args, **kwargs)
        check_cls.__init__ = __init__

        return check_cls

    return wrapper(args[0]) if args else wrapper


class BaseSarmatStructure:
    """Базовая структура"""

    @property
    def sarmat_fields(self):
        return [fld.name for fld in fields(self)]

    def as_dict(self):
        return asdict(self)


@dataclass
class SarmatStructure(BaseSarmatStructure):
    """Основной класс с идентификатором"""

    id: int


@dataclass
class PersonStructure:
    """Реквизиты человека"""

    last_name: str      # фамилия
    first_name: str     # имя
    middle_name: str    # отчество
