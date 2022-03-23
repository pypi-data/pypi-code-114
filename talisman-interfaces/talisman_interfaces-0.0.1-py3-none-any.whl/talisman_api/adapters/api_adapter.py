import logging
import os
from contextlib import AbstractContextManager
from typing import Dict, Iterable, Optional, Tuple

from requests import Timeout
from sgqlc.operation import Operation

from .gql_clients import AbstractGQLClient, KeycloakAwareGQLClient, NoAuthGQLClient
from .schemas.api_schema import ConceptPropertyValueType, ConceptType, Query

logger = logging.getLogger(__name__)


class TalismanAPIAdapter(AbstractContextManager):
    def __init__(self, gql_uri: str):
        self._gql_uri = gql_uri
        self._gql_client: Optional[AbstractGQLClient] = None

    def __enter__(self):
        self._check_api()
        if os.getenv("KEYCLOAK_AUTH_URL") is None:
            self._gql_client = NoAuthGQLClient(self._gql_uri)
        else:
            self._gql_client = KeycloakAwareGQLClient(self._gql_uri)

        logger.info(f"{type(self._gql_client)} will be used")

        self._gql_client.__enter__()
        return self

    def __exit__(self, *exc):
        self._gql_client.__exit__(*exc)
        self._gql_client = None

    def _check_api(self):
        logger.info(f"used correct version of API")
        return True

    def get_base_types(self, dictionary: bool = False, regexp: bool = False, pretrained_nercmodels: bool = False
                       ) -> Tuple[Tuple[ConceptType, ...], Tuple[ConceptPropertyValueType, ...]]:
        op = Operation(Query)

        concept_types: ConceptType = op.list_concept_type
        property_value_types: ConceptPropertyValueType = op.list_concept_property_value_type

        concept_types.id()
        property_value_types.id()

        if dictionary:
            concept_types.dictionary()
            property_value_types.dictionary()

        if regexp:
            concept_types.regexp()
            property_value_types.regexp()

        if pretrained_nercmodels:
            concept_types.pretrained_nercmodels()
            property_value_types.pretrained_nercmodels()

        ret = self.gql_call(op)
        return tuple(ret.list_concept_type), tuple(ret.list_concept_property_value_type)

    def execute_easy_query(self, name: str, params: Iterable[str], variables: Optional[Dict] = None):
        op = Operation(Query)
        if variables:
            op[name](**variables).__fields__(*params)
        else:
            op[name].__fields__(*params)
        return self.gql_call(op)[name]

    def gql_call(self, sgqlc_operation: Operation, variables: Optional[dict] = None, raise_on_timeout: bool = True):
        try:
            return sgqlc_operation + self._gql_client.execute(sgqlc_operation, variables=variables)
        except Timeout as e:
            logger.error('Timeout while query processing', exc_info=e, extra={'query': sgqlc_operation})
            if raise_on_timeout:
                raise e
        except Exception as e:
            logger.error('Some exception was occured during query processing.', exc_info=e,
                         extra={'query': sgqlc_operation})
            raise e
