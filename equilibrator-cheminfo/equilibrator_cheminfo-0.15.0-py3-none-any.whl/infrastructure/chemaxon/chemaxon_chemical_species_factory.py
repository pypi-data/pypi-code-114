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


"""Provide a ChemAxon-based factory for chemical species."""


from typing import List, Optional

from equilibrator_cheminfo.domain.model import (
    AbstractChemicalSpeciesFactory,
    ChemicalSpecies,
    ErrorMessage,
    MajorMicrospecies,
    ManualStructureExceptionSpecification,
    Structure,
)

from .chemaxon_error import ChemAxonError
from .chemaxon_major_microspecies_service import ChemAxonMajorMicrospeciesService
from .chemaxon_molecule import ChemAxonMolecule
from .chemaxon_proton_dissociation_constants_service import (
    ChemAxonProtonDissociationConstantsService,
)


class ChemAxonChemicalSpeciesFactory(AbstractChemicalSpeciesFactory):
    """Define a factory for chemical species that uses ChemAxon services."""

    def __init__(
        self,
        *,
        majorms_service: ChemAxonMajorMicrospeciesService,
        pka_service: ChemAxonProtonDissociationConstantsService,
        **kwargs
    ) -> None:
        """Initialize the base."""
        super().__init__(
            majorms_service=majorms_service, pka_service=pka_service, **kwargs
        )

    def make(self, structure: Structure) -> Optional[ChemicalSpecies]:
        """Return a chemical species created from ChemAxon services."""
        if ManualStructureExceptionSpecification.is_satisfied_by(structure):
            return ManualStructureExceptionSpecification.get_chemical_species(structure)
        try:
            # Create a molecule, preferably from a SMILES rather than an InChI.
            if structure.smiles is not None:
                molecule = ChemAxonMolecule.from_smiles(structure.smiles)
            else:
                molecule = ChemAxonMolecule.from_inchi(structure.identifier.inchi)
        except ChemAxonError as exc:
            # Without a valid molecule, we cannot run ChemAxon predictions and must
            # return early. Since creating a molecule failed, we expect no microspecies.
            return ChemicalSpecies(
                identifier=structure.identifier,
                errors=self._create_error_messages(exc),
            )
        result = ChemicalSpecies(identifier=structure.identifier)
        errors = []
        self._add_pka_values(result, molecule, errors)
        self._add_microspecies(result, molecule, errors)
        self._recover_microspecies(result, structure, molecule)
        result.errors = errors
        return result

    def _add_microspecies(
        self,
        species: ChemicalSpecies,
        molecule: ChemAxonMolecule,
        errors: List[ErrorMessage],
    ) -> None:
        """Add a major microspecies to the chemical species in a failsafe way."""
        try:
            result = self._majorms.estimate_major_microspecies(molecule)
            species.microspecies = [
                MajorMicrospecies(
                    smiles=result.smiles,
                    atom_bag=result.atom_bag,
                    charge=result.charge,
                    ph=self._majorms.ph,
                )
            ]
        except ChemAxonError as exc:
            errors.extend(self._create_error_messages(exc))

    def _add_pka_values(
        self,
        species: ChemicalSpecies,
        molecule: ChemAxonMolecule,
        errors: List[ErrorMessage],
    ) -> None:
        """Add a pKa values to the chemical species in a failsafe way."""
        try:
            species.pka_values = self._pka.estimate_pka_values(molecule)
        except ChemAxonError as exc:
            errors.extend(self._create_error_messages(exc))

    def _recover_microspecies(
        self,
        species: ChemicalSpecies,
        structure: Structure,
        molecule: ChemAxonMolecule,
    ) -> None:
        """
        Recover a microspecies in the case that the prediction by ChemAxon failed.

        If the original structure had a SMILES description, we simply assume that to be
        the major microspecies.
        """
        if structure.smiles is not None and not species.microspecies:
            species.microspecies = [
                MajorMicrospecies(
                    smiles=structure.smiles,
                    atom_bag=molecule.atom_bag,
                    charge=molecule.charge,
                    ph=self._majorms.ph,
                )
            ]
