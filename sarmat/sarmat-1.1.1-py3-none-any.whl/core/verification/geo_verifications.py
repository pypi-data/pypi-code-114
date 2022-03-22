"""
Sarmat.

Ядро пакета.

Классы для проведения верификации данных.

Веификация гео объектов.
"""
from __future__ import absolute_import

from sarmat.core.constants import ErrorCode, LocationType
from sarmat.core.containers import GeoStructure

from .base_verifications import VerifyOnEmptyValues
from ..exceptions import SarmatException


class GeoVerifier(VerifyOnEmptyValues):
    """Класс верификации гео объектов"""

    attributes = ["name", "location_type"]

    # NOTE: Проверка на правильность построения иерархии.
    #       У страны не может быть родительских записей.
    #       Для республик, областей и районов в качестве родителя может выступать только страна.
    possible_parent_types = {
        LocationType.COUNTRY: [],
        LocationType.DISTRICT: [LocationType.COUNTRY],
        LocationType.REGION: [LocationType.COUNTRY],
        LocationType.PROVINCE: [LocationType.COUNTRY],
        LocationType.AREA: [LocationType.COUNTRY, LocationType.DISTRICT, LocationType.PROVINCE],
    }

    def verify(self, subject: GeoStructure) -> None:
        super().verify(subject)

        if subject.parent:
            parent_location_types = self.possible_parent_types[subject.location_type]
            if subject.parent.location_type not in parent_location_types:
                raise SarmatException(
                    f"Wrong parent type of location: {subject.parent.location_type}",
                    err_code=ErrorCode.WRONG_VALUE,
                )

            if subject.parent.id == subject.id:
                raise SarmatException(
                    "Geo object can't be a parent for themself",
                    err_code=ErrorCode.WRONG_VALUE,
                )


class DestinationPointVerifier(VerifyOnEmptyValues):
    """Класс верификации пунктов назначения"""

    attributes = ["name", "state", "point_type"]
