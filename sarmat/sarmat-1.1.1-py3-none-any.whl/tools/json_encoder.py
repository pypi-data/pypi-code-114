"""
Sarmat.

Вспомогательные инструменты.

Преобразование Sarmat объектов в JSON и обратно
"""
import json
from decimal import Decimal

import sarmat.core.constants.sarmat_constants as constants
from sarmat.core.exceptions import WrongValueError


class SarmatEncoder(json.JSONEncoder):

    def _as_enum(self, obj):
        return {"__enum__": str(obj)}

    def _as_decimal(self, obj):
        return str(obj)

    def default(self, obj):
        if isinstance(obj, constants.SarmatAttribute):
            return self._as_enum(obj)
        if isinstance(obj, Decimal):
            return self._as_decimal(obj)
        return json.JSONEncoder.default(self, obj)


def as_enum(dct):
    if "__enum__" in dct:
        name, member = dct["__enum__"].split(".")

        try:
            cls = getattr(constants, name)
        except AttributeError:
            raise WrongValueError(f"Неизвестный тип {name}")

        try:
            return getattr(cls, member)
        except AttributeError:
            raise WrongValueError(f"Неизвестное значение {member}")
    else:
        return dct
