"""query utilities and reusable methods"""
from typing import List, Dict
import numpy as np
import pandas as pd
import awswrangler as aw
from dp_tms.database.queries import entities  as entity_queries

def query_from_candidate_matching_database(query: str, workgroup: str) -> pd.DataFrame:
    """run query against selected database

    Args:
        query (str): SQL query string
        workgroup (str): name of athena workgroup

    Returns:
        pd.DataFrame: results of query
    """
    dataframe = aw.athena.read_sql_query(
        query,
        database='dp_candidate_matching_tf',
        workgroup=workgroup
    )
    return dataframe

def get_vectors_by_entity_type(entities: list, client_code: str, environment: str, entity_type: str, workgroup: str) -> np.ndarray:
    """get entity vectors by entity type

    Args:
        entities (list): entity ids to retrieve
        client_code (str): client identifier code
        environment (str): development staging environment to use i.e. prod, dev, test
        entity_type (str): type of entity to retrieve
        workgroup (str): name of athena workgroup

    Raises:
        TypeError: for unsupported entity type

    Returns:
        np.ndarray: _description_
    """
    if entity_type == 'listings':
        query = entity_queries.get_jarvis_vector_embeddings(
            entities=entities,
            entity_type="listing",
            client_code=client_code,
            environment=environment
        )
        data = query_from_candidate_matching_database(query, workgroup)

        # order rows by entity_ids
        # and return vector
        return data.set_index('entity_id').loc[entities].vector.to_numpy()

    elif entity_type == 'candidates':
        query = entity_queries.get_jarvis_vector_embeddings(
            entities=entities,
            entity_type="candidate",
            client_code=client_code,
            environment=environment
        )

        data = query_from_candidate_matching_database(query, workgroup)
        # order rows by entity_ids
        # and return vector
        return data.set_index('entity_id').loc[entities].vector.to_numpy()
    else:
        raise TypeError(f"`entity_type` == {entity_type} is not supported")

def get_jarvis_request_metadata_by_entity_type(
    entities: list, entity_types: list, client_code: str, environment: str, workgroup: str
) -> List[Dict[str, str]]:
    """get entity vectors for entity type & id for client and environment

    Args:
        entities (list): list of ids for each entity
        entity_types (list): list of types for each entity
        client_code (str): client identifier code
        environment (str): development staging environment to use i.e. prod, dev, test
        workgroup (str): name of athena workgroup

    Returns:
        List[Dict[str, str]]: result from query as records
    """

    query = entity_queries.get_jarvis_request_metadata(
        entities=entities,
        entity_types=entity_types,
        client_code=client_code,
        environment=environment
    )

    data = query_from_candidate_matching_database(query, workgroup)

    return data.to_dict(orient='records')
