# Copyright (c) 2021, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide an abstract factory for creating chemical species."""


from abc import ABC, abstractmethod
from typing import List, Optional

from ..service import (
    AbstractMajorMicrospeciesService,
    AbstractProtonDissociationConstantsService,
)
from .chemical_species import ChemicalSpecies
from .equilibrator_cheminformatics_error import EquilibratorCheminformaticsError
from .error_message import ErrorMessage, SeverityLevel
from .structure import Structure


class AbstractChemicalSpeciesFactory(ABC):
    """Define an abstract factory for creating chemical species."""

    def __init__(
        self,
        majorms_service: AbstractMajorMicrospeciesService,
        pka_service: AbstractProtonDissociationConstantsService,
        **kwargs
    ) -> None:
        """Initialize the base."""
        super().__init__(**kwargs)
        self._majorms = majorms_service
        self._pka = pka_service

    @abstractmethod
    def make(
        self,
        structure: Structure,
    ) -> Optional[ChemicalSpecies]:
        """Return a chemical species built from services."""

    @classmethod
    def _create_error_messages(
        cls,
        error: EquilibratorCheminformaticsError,
    ) -> List[ErrorMessage]:
        """Return a list of error messages from an exception instance."""
        result = [
            ErrorMessage(message=msg, level=SeverityLevel.ERROR) for msg in error.errors
        ]
        result.extend(
            (
                ErrorMessage(message=msg, level=SeverityLevel.WARNING)
                for msg in error.warnings
            )
        )
        return result
