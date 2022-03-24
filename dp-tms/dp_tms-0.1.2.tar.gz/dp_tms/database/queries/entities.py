"""entity query string methods"""
from dp_tms.utils.athena import encode_list_as_list_of_strings

def get_jarvis_request_metadata(entities, entity_types, client_code, environment):
    """
    Args:
        entities (list): entity ids to retrieve
        entity_types (list): list of types for each entity
        client_code (str): client identifier code
        environment (str): development staging environment to use i.e. prod, dev, test

    Returns:
        str: SQL query string
    """

    entity_list_strings = [f"{entity_type}-{entity_id}" for entity_id, entity_type in zip(entities, entity_types)]
    entity_list_strings = encode_list_as_list_of_strings(items=entity_list_strings)

    return f"""
        WITH
        LABEL_BY_MOST_RECENT AS (
            SELECT
                *,
                rank() OVER (
                    PARTITION BY entity_id, entity_type, partition_0, partition_1
                    ORDER BY created_at DESC
                ) AS rnk
                FROM "dp_candidate_matching_tf"."entities_raw"
        )

        SELECT
            entity_id,
            entity_type,
            properties.storage_reference.disk,
            properties.storage_reference.bucket,
            properties.storage_reference.file as file_path,
            properties.storage_reference.type as file_type
        FROM LABEL_BY_MOST_RECENT
        WHERE
            rnk = 1
            AND CONCAT(entity_type, '-', entity_id) in  ({entity_list_strings})
            AND partition_0 = '{client_code}'
            AND partition_1 = '{environment}'
        ;
    """

def get_jarvis_vector_embeddings(entities: list, entity_type: str, client_code: str, environment: str) -> str:
    """get a single listing vector for comparison
        
        note:
            - this could be multiple listings to speed up query
    Args:
        entity_ids (list): entity ids to retrieve
        entity_type (str): type of entity to retrieve
        client_code (str): client identifier code
        environment (str): development staging environment to use i.e. prod, dev, test

    Returns:
        str: SQL query string
    """

    entities = encode_list_as_list_of_strings(items=entities)
    return f"""
        WITH LABEL_BY_MOST_RECENT AS (
            SELECT
                *,
                rank() OVER (
                    PARTITION BY entity_id, entity_type, source, partition_0, partition_1
                    ORDER BY created_at DESC
                ) AS rnk
                FROM "dp_candidate_matching_tf"."entities_enriched"
        )

        SELECT
            entity_id,
            properties.embedding.vector
        FROM LABEL_BY_MOST_RECENT
        WHERE
            rnk = 1
            AND source = 'jarvis'
            AND entity_type = '{entity_type}'
            AND entity_id in ({entities})
            AND partition_0 = '{client_code}'
            AND partition_1 = '{environment}'
        ;
    """
