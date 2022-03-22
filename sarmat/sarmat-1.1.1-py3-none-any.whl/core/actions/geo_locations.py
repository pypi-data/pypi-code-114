"""
Sarmat.

Описание действий с объектами.

Классы для работы с объектами гео локации.
"""
from __future__ import absolute_import

from sarmat.core.verification import (
    DestinationPointVerifier,
    GeoVerifier,
)

from .bases import Action


class AGeoLocation(Action):
    """Действия с объектами гео локации"""

    verification_class = GeoVerifier

    def copy(self):
        return self.__class__(
            id=0,
            name=f"Копия {self.name}",
            location_type=self.location_type,
            latin_name=f"Copy of {self.latin_name}" if self.latin_name else "",
            mapping_data=self.mapping_data,
            tags=self.tags,
            parent=self.parent,
        )


class ADestinationPoint(Action):
    """Действия с пунктами назначения"""

    verification_class = DestinationPointVerifier

    def copy(self):
        return self.__class__(
            id=0,
            name=f"Копия {self.name}",
            state=self.state,
            point_type=self.point_type,
        )
