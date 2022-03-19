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


"""Provide a domain registry which makes available configured repositories."""


from equilibrator_cheminfo.domain.model import (
    AbstractChemicalSpeciesFactory,
    AbstractChemicalSpeciesRepository,
    AbstractDomainRegistry,
)

from .chemical_species_configuration import ChemicalSpeciesConfiguration
from .cheminformatics_backend import CheminformaticsBackend


class DomainRegistry(AbstractDomainRegistry):
    """Implement a domain registry returning ORM-based repository instances."""

    @classmethod
    def chemical_species_repository(
        cls, backend: str
    ) -> AbstractChemicalSpeciesRepository:
        """Return an instance of a chemical species repository."""
        from .persistence.orm import ORMChemicalSpeciesRepository, ORMManagementService

        return ORMChemicalSpeciesRepository(
            session=ORMManagementService.create_session(backend)
        )

    @classmethod
    def chemical_species_factory(
        cls, configuration: ChemicalSpeciesConfiguration
    ) -> AbstractChemicalSpeciesFactory:
        """Return a chemical species factory for the specified backend."""
        if configuration.cheminformatics_backend == CheminformaticsBackend.ChemAxon:
            from .chemaxon import ChemAxonChemicalSpeciesConfiguration

            assert isinstance(configuration, ChemAxonChemicalSpeciesConfiguration)
            from .chemaxon import (
                ChemAxonChemicalSpeciesFactory,
                ChemAxonMajorMicrospeciesService,
                ChemAxonProtonDissociationConstantsService,
            )

            return ChemAxonChemicalSpeciesFactory(
                majorms_service=ChemAxonMajorMicrospeciesService(
                    ph=configuration.fixed_ph
                ),
                pka_service=ChemAxonProtonDissociationConstantsService(
                    minimum_ph=configuration.minimum_ph,
                    minimum_basic_pka=configuration.minimum_ph,
                    maximum_ph=configuration.maximum_ph,
                    maximum_acidic_pka=configuration.maximum_ph,
                    use_large_model=configuration.use_large_model,
                ),
            )
        else:
            raise ValueError(
                "Currently, pKa and major microspecies estimation is only provided by "
                "ChemAxon Marvin."
            )
