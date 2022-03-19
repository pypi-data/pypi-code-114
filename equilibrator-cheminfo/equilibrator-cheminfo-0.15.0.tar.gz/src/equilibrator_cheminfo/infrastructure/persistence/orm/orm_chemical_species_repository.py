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


"""Provide a chemical species repository backed by an ORM."""


import logging
from typing import FrozenSet

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import selectinload

from equilibrator_cheminfo.domain.model import (
    AbstractChemicalSpeciesRepository,
    ChemicalSpecies,
    ErrorMessage,
    MajorMicrospecies,
    StructureIdentifier,
)

from .orm_base import ORMSession
from .orm_chemical_species import ORMChemicalSpecies
from .orm_error_message import ORMErrorMessage
from .orm_major_microspecies import ORMMajorMicrospecies
from .orm_proton_dissociation_constant import ORMProtonDissociationConstant


logger = logging.getLogger(__name__)


class ORMChemicalSpeciesRepository(AbstractChemicalSpeciesRepository):
    """Define an ORM-based chemical species repository."""

    def __init__(self, *, session: ORMSession, **kwargs) -> None:
        """Initialize the base."""
        super().__init__(**kwargs)
        self._session = session

    @classmethod
    def reconstruct(cls, chemical_species: ORMChemicalSpecies) -> ChemicalSpecies:
        """Build an ORM representation of a chemical species."""
        return ChemicalSpecies(
            identifier=StructureIdentifier(
                inchikey=chemical_species.inchikey, inchi=chemical_species.inchi
            ),
            microspecies=[
                MajorMicrospecies(
                    smiles=ms.smiles, atom_bag=ms.atom_bag, charge=ms.charge, ph=ms.ph
                )
                for ms in chemical_species.microspecies
            ],
            pka_values=[
                pka.value for pka in chemical_species.proton_dissociation_constants
            ],
            errors=[
                ErrorMessage(message=error.message, level=error.level)
                for error in chemical_species.error_messages
            ],
        )

    def find_by_inchikey(self, inchikey: str) -> ChemicalSpecies:
        """Find a chemical species in the repository by its InChIKey."""
        identifier = StructureIdentifier(
            inchikey=inchikey, inchi="InChI=1"
        ).neutralize_protonation()
        try:
            species: ORMChemicalSpecies = (
                self._session.query(ORMChemicalSpecies)
                .options(selectinload(ORMChemicalSpecies.proton_dissociation_constants))
                .options(selectinload(ORMChemicalSpecies.microspecies))
                .options(selectinload(ORMChemicalSpecies.error_messages))
                .filter_by(inchikey=identifier.inchikey)
                .one()
            )
        except NoResultFound:
            raise KeyError(f"{inchikey} is not in the repository.")
        return self.reconstruct(species)

    def get_inchikeys(self) -> FrozenSet[str]:
        """Return InChIKeys that already exist in the repository."""
        return frozenset(
            row.inchikey for row in self._session.query(ORMChemicalSpecies.inchikey)
        )

    def add(self, chemical_species: ChemicalSpecies) -> None:
        """Add a chemical species to the repository."""
        try:
            result: ORMChemicalSpecies = (
                self._session.query(ORMChemicalSpecies)
                .options(selectinload(ORMChemicalSpecies.proton_dissociation_constants))
                .options(selectinload(ORMChemicalSpecies.microspecies))
                .options(selectinload(ORMChemicalSpecies.error_messages))
                .filter_by(inchikey=chemical_species.identifier.inchikey)
                .one()
            )
        except NoResultFound:
            result = ORMChemicalSpecies(
                inchikey=chemical_species.identifier.inchikey,
                inchi=chemical_species.identifier.inchi,
            )
        result.microspecies = [
            ORMMajorMicrospecies(
                smiles=ms.smiles, atom_bag=ms.atom_bag, charge=ms.charge, ph=ms.ph
            )
            for ms in chemical_species.microspecies
        ]
        result.proton_dissociation_constants = [
            ORMProtonDissociationConstant(value=pka)
            for pka in chemical_species.pka_values
        ]
        result.error_messages = [
            ORMErrorMessage(message=error.message, level=error.level)
            for error in chemical_species.errors
        ]
        self._session.add(result)
        self._session.commit()

    def remove(self, chemical_species: ChemicalSpecies) -> None:
        """Remove a chemical species from the repository."""
        try:
            result = (
                self._session.query(ORMChemicalSpecies)
                .filter_by(inchikey=chemical_species.identifier.inchikey)
                .one()
            )
        except NoResultFound:
            raise KeyError(
                f"{chemical_species.identifier.inchikey} is not in the repository."
            )
        self._session.delete(result)
        self._session.commit()

    def log_summary(self) -> None:
        """Summarize the information on chemical species."""
        logger.info("Chemical species summary:")
        base_query = self._session.query(ORMChemicalSpecies.id).select_from(
            ORMChemicalSpecies
        )
        num_total = base_query.count()
        logger.info(f"- {num_total:n} unique InChIKeys")
        num_with_pka = base_query.join(ORMProtonDissociationConstant).distinct().count()
        logger.info(
            f"- {num_with_pka:n} ({num_with_pka / num_total:.2%}) with pKa values"
        )
        num_with_major_ms = base_query.join(ORMMajorMicrospecies).distinct().count()
        logger.info(
            f"- {num_with_major_ms:n} ({num_with_major_ms / num_total:.2%}) with major "
            f"microspecies at pH 7"
        )
        num_with_error = base_query.join(ORMErrorMessage).distinct().count()
        logger.info(
            f"- {num_with_error:n} ({num_with_error / num_total:.2%}) with errors:"
        )
        if num_with_error > 0:
            num_with_error_but_pka = (
                base_query.join(ORMErrorMessage)
                .join(ORMProtonDissociationConstant)
                .distinct()
                .count()
            )
            logger.info(
                f"  - {num_with_error_but_pka:n} "
                f"({num_with_error_but_pka / num_with_error:.2%}) "
                f"of those with pKa values"
            )
            num_with_error_but_major_ms = (
                base_query.join(ORMErrorMessage)
                .join(ORMMajorMicrospecies)
                .distinct()
                .count()
            )
            logger.info(
                f"  - {num_with_error_but_major_ms:n} "
                f"({num_with_error_but_major_ms / num_with_error:.2%}) "
                f"of those with major microspecies at pH 7"
            )
