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


"""Provide abstract base classes for the domain model."""


from .equilibrator_cheminformatics_error import EquilibratorCheminformaticsError
from .abstract_molecule import AbstractMolecule
from .structure_identifier import StructureIdentifier
from .error_message import ErrorMessage, SeverityLevel
from .major_microspecies import MajorMicrospecies
from .chemical_species import ChemicalSpecies
from .abstract_chemical_species_factory import AbstractChemicalSpeciesFactory
from .abstract_chemical_species_repository import AbstractChemicalSpeciesRepository
from .structure import Structure
from .structures_table import Structure, StructuresTable
from .manual_structure_exception_specification import (
    ManualStructureExceptionSpecification,
)
from .abstract_domain_registry import AbstractDomainRegistry
