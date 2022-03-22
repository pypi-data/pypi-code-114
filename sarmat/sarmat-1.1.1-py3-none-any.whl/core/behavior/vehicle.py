"""
Sarmat.

Описание поведения объектов.

Подвижной состав.
"""
from .bases import CompareBehavior
from .sarmat import BhPerson
from ..exceptions import IncomparableTypesError


class BhVehicle(CompareBehavior):
    """Методы сравнения объекта 'Транспортное средство'"""

    def _compare_classes(self, other):
        return isinstance(other, BhVehicle)

    def __eq__(self, other):
        """Сравнение двух транспортных средств"""
        super().__eq__(other)
        condition1 = self.vehicle_type == other.vehicle_type and self.vehicle_name == other.vehicle_name
        condition2 = self.state_number == other.state_number
        return condition1 and condition2

    def __ne__(self, other):
        """Проверка на неравенство двух транспортных средств"""
        super().__ne__(other)
        return self.state_number != other.state_number \
            or self.vehicle_type != other.vehicle_type \
            or self.vehicle_name != other.vehicle_name

    def __lt__(self, other):
        """Сравнение транспортных средств по вместимости.
           Количество посадочных мест, количество мест стоя, вместимость багажного отделения
        """
        super().__lt__(other)
        return (self.seats, self.stand, self.capacity) < (other.seats, other.stand, other.capacity)

    def __gt__(self, other):
        """Сравнение транспортных средств по вместимости.
           Количество посадочных мест, количество мест стоя, вместимость багажного отделения
        """
        super().__gt__(other)
        return (self.seats, self.stand, self.capacity) > (other.seats, other.stand, other.capacity)

    def __le__(self, other):
        """Сравнение транспортных средств по вместимости.
           Количество посадочных мест, количество мест стоя, вместимость багажного отделения
        """
        super().__le__(other)
        return (self.seats, self.stand, self.capacity) <= (other.seats, other.stand, other.capacity)

    def __ge__(self, other):
        """Сравнение транспортных средств по вместимости.
           Количество посадочных мест, количество мест стоя, вместимость багажного отделения
        """
        super().__ge__(other)
        return (self.seats, self.stand, self.capacity) >= (other.seats, other.stand, other.capacity)

    def __contains__(self):
        """Проверка на вхождение для транспортного средства не имеет смысла"""
        raise IncomparableTypesError("Проверка на вхождение для транспортного средства не производится")


class BhCrew(BhPerson):
    """Методы сравнения сведений об экипаже"""

    def _compare_classes(self, other):
        return isinstance(other, BhCrew)

    def __eq__(self, other):
        person_compare = super().__eq__(other)
        return person_compare and self.crew_type == other.crew_type

    def __ne__(self, other):
        person_compare = super().__ne__(other)
        return person_compare or self.crew_type != other.crew_type


class BhPermit(CompareBehavior):
    """Методы сравнения путевых листов"""
    compare_error_message = "Направления сравнению не подлежат"

    def _compare_classes(self, other):
        return isinstance(other, BhPermit)

    def __eq__(self, other):
        """Сравнение путевых листов"""
        super().__eq__(other)
        return self.number == other.number \
            and self.permit_type == other.permit_type \
            and self.depart_date == other.depart_date

    def __ne__(self, other):
        """Проверка на неравенство путевых листов"""
        super().__ne__(other)
        return self.number != other.number \
            or self.permit_type != other.permit_type \
            or self.depart_date != other.depart_date

    def __lt__(self, other):
        """Проверка сравнение не имеет смысла для путевых листов"""
        raise IncomparableTypesError(self.compare_error_message)

    def __gt__(self, other):
        """Проверка сравнение не имеет смысла для путевых листов"""
        raise IncomparableTypesError(self.compare_error_message)

    def __le__(self, other):
        """Проверка сравнение не имеет смысла для путевых листов"""
        raise IncomparableTypesError(self.compare_error_message)

    def __ge__(self, other):
        """Проверка сравнение не имеет смысла для путевых листов"""
        raise IncomparableTypesError(self.compare_error_message)

    def __contains__(self, item):
        """Проверка на вхождение транспортного средства или водителя в состав экипажа"""

        if isinstance(item, BhCrew):
            if self.crew is None:
                return False
            return item in self.crew

        if isinstance(item, BhVehicle):
            if self.vehicle is None:
                return False
            return item in self.vehicle

        raise IncomparableTypesError(f"Тип {item.__class__} не предназначен для проверки на вхождение в состав экипажа")
