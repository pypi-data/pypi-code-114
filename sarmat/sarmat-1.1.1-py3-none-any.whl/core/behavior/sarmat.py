"""
Sarmat.

Описание поведения объектов.

Объекты общего назначения.
"""
from .bases import CompareBehavior
from ..exceptions import IncomparableTypesError


class BhPerson(CompareBehavior):
    """Методы сравнения учетных записей"""
    compare_error_message = "Учетные записи сравнению не подлежат"
    contains_error_message = "Учетные записи проверке на вхождение не подлежат"

    def _compare_classes(self, other):
        return isinstance(other, BhPerson)

    def __eq__(self, other):
        """Сравнение учетных записей"""
        super().__eq__(other)
        return self.last_name == other.last_name \
            and self.first_name == other.first_name \
            and self.middle_name == other.middle_name

    def __ne__(self, other):
        """Проверка на неравенство учетных записей"""
        super().__ne__(other)
        return self.last_name != other.last_name \
            or self.first_name != other.first_name \
            or self.middle_name != other.middle_name

    def __lt__(self, other):
        """Сравнение учетных записей не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, other):
        """Сравнение учетных записей не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Сравнение учетных записей не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Сравнение учетных записей не имеет смысла"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на вхождение учетных записей не имеет смысла"""
        raise IncomparableTypesError(self.contains_error_message)
