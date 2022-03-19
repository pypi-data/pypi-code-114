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


"""Provide a specification for which structures require exceptional treatment."""


import json
from importlib.resources import open_text
from typing import Dict, NamedTuple

import pandas as pd

from . import data
from .chemical_species import ChemicalSpecies
from .major_microspecies import MajorMicrospecies
from .structure import Structure, StructureIdentifier


class _ChemicalSpeciesRow(NamedTuple):
    """Define the expected fields on the manual exceptions table."""

    inchikey: str
    inchi: str
    smiles: str
    atom_bag: str
    charge: int


def _row2chemical_species(row: _ChemicalSpeciesRow) -> ChemicalSpecies:
    """Create a chemical species from the table row's field values."""
    return ChemicalSpecies(
        identifier=StructureIdentifier(inchikey=row.inchikey, inchi=row.inchi),
        microspecies=[
            MajorMicrospecies(
                smiles=row.smiles,
                atom_bag=json.loads(row.atom_bag),
                charge=row.charge,
                ph=7.0,
            )
        ],
    )


class ManualStructureExceptionSpecification:
    """
    Define a specification for which structures require exceptional treatment.

    This list is mostly comprised of metal ions for which ChemAxon will predict a major
    microspecies and pKa values but they are very likely incorrect and are not of
    interest for eQuilibrator.

    """

    with open_text(data, "manual_exceptions.tsv") as handle:
        _exceptions: Dict[str, ChemicalSpecies] = {
            row.inchikey: _row2chemical_species(row)
            for row in pd.read_table(handle, sep="\t").itertuples(index=False)
        }

    @classmethod
    def is_satisfied_by(cls, structure: Structure) -> bool:
        """Check the given structure to see if it needs special treatment."""
        return structure.identifier.inchikey in cls._exceptions

    @classmethod
    def get_chemical_species(cls, structure: Structure) -> ChemicalSpecies:
        """Return the pre-determined chemical species for the given structure."""
        return cls._exceptions[structure.identifier.inchikey]
