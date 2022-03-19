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


"""Provide a chemical species, an aggregate root within the domain."""


from typing import Iterable, List

from .error_message import ErrorMessage
from .major_microspecies import MajorMicrospecies
from .structure_identifier import StructureIdentifier


class ChemicalSpecies:
    """
    Define a chemical species.

    A chemical species, according to [1]_, is:

        An ensemble of chemically identical molecular entities that can explore
        the same set of molecular energy levels on the time scale of the
        experiment. The term is applied equally to a set of chemically identical
        atomic or molecular structural units in a solid array. For example, two
        conformational isomers may be interconverted sufficiently slowly to be
        detectable by separate NMR spectra and hence to be considered to be
        separate chemical species on a time scale governed by the radiofrequency
        of the spectrometer used. On the other hand, in a slow chemical reaction
        the same mixture of conformers may behave as a single chemical species,
        i.e. there is virtually complete equilibrium population of the total set
        of molecular energy levels belonging to the two conformers. Except where
        the context requires otherwise, the term is taken to refer to a set of
        molecular entities containing isotopes in their natural abundance. The
        wording of the definition given in the first paragraph is intended to
        embrace both cases such as graphite , sodium chloride or a surface
        oxide, where the basic structural units may not be capable of isolated
        existence, as well as those cases where they are. In common chemical
        usage generic and specific chemical names (such as radical or hydroxide
        ion) or chemical formulae refer either to a chemical species or to a
        molecular entity.

    References
    ----------
    .. [1] IUPAC. Compendium of Chemical Terminology, 2nd ed. (the "Gold Book").
        Compiled by A. D. McNaught and A. Wilkinson.
        Blackwell Scientific Publications, Oxford (1997).
        Online version (2019-) created by S. J. Chalk.
        ISBN 0-9678550-9-8.
        https://doi.org/10.1351/goldbook.
        https://goldbook.iupac.org/terms/view/CT01038

    """

    def __init__(
        self,
        *,
        identifier: StructureIdentifier,
        microspecies: Iterable[MajorMicrospecies] = (),
        pka_values: Iterable[float] = (),
        errors: Iterable[ErrorMessage] = (),
        **kwargs,
    ) -> None:
        """Initialize a chemical species."""
        super().__init__(**kwargs)
        self.identifier = identifier.neutralize_protonation()
        self.microspecies: List[MajorMicrospecies] = list(microspecies)
        self.pka_values: List[float] = list(pka_values)
        self.errors: List[ErrorMessage] = list(errors)

    def __repr__(self) -> str:
        """Return a string representation of the chemical species."""
        return (
            f"{type(self).__name__}(identifier={self.identifier}, "
            f"pKa={self.pka_values}, "
            f"major_ms={len(self.microspecies)})"
        )
