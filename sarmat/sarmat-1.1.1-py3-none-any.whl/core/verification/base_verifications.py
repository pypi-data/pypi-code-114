"""
Sarmat.

Ядро пакета.

Классы для проведения верификации данных.

Классы базовой верификации.
"""
from __future__ import absolute_import

from abc import ABC, abstractmethod

from sarmat.core.containers import SarmatStructure
from sarmat.core.constants import ErrorCode
from sarmat.core.exceptions import SarmatException


class Verification(ABC):
    """Базовый класс проверки."""

    def __init__(self, parent=None):
        self._parent = parent

    @abstractmethod
    def verify(self, subject: SarmatStructure) -> None:
        """Объект проверяет свои атрибуты."""
        if self._parent:
            self._parent.verify(subject)


class VerifyOnEmptyValues(Verification):
    """
    Проверка на непустоту атрибутов.

    Если атрибут отсутствует, будет вызвана ошибка.
    """

    attributes = []

    def verify(self, subject: SarmatStructure) -> None:
        for attr in subject.sarmat_fields:
            if hasattr(subject, attr):
                if attr in self.attributes and getattr(subject, attr) is None:
                    raise SarmatException(attr, err_code=ErrorCode.NOT_FILLED)
            else:
                raise SarmatException(attr, err_code=ErrorCode.NO_ATTRIBUTE)

        super().verify(subject)
