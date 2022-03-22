"""
Sarmat.

Описание действий с объектами.

Базовые классы.
"""
from __future__ import absolute_import

from sarmat.core.verification.base_verifications import Verification


class Action:
    """Базовый класс для описания работы с объектами"""

    verification_class = Verification

    @classmethod
    def verify_after_create(cls, structure):
        cls.verification_class().verify(structure)

    def __init__(self, **attributes):
        super().__init__(**attributes)
        self.verify_after_create(self)

    def copy(self):
        raise NotImplementedError
