"""
    jarvis service utilities

    methods include
    ------------------------
    1. read_file_stream_from_s3
    2. compile_document_for_request
    3. fetch_document_vectors_from_api
    4. slice_baskets
    5. compile_documents_for_jarvis
    6. batch_and_fetch_vectors

"""
import base64
import io
import math
import requests
from typing import List, Any, Dict
import boto3

def read_file_stream_from_s3(bucket_name: str, file_path: str):
    """read file from s3 as a file_stream ready for json encoding

    Args:
        bucket_name (str): name of s3 bucket
        file_path (str): s3 prefix of full filepath

    Returns:
        str: json supported file stream
    """
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)

    object = bucket.Object(file_path)
    file_stream = io.BytesIO()
    object.download_fileobj(file_stream)
    file_stream.seek(0)

    file_stream = file_stream.getvalue()
    return str(base64.b64encode(file_stream))[2:-1]

def compile_document_for_request(
    file_stream: str,
    doc_type: str,
    file_type: str,
    unique_id: int,
) -> dict:
    """compile document in to a jarvis supported dictionary document

    Args:
        file_stream (str): json supported file stream
        doc_type (str): jarvis supported document type i.e. job or cv
        file_type (str): document type i.e. pdf, txt, etc
        unique_id (int): unique entity id

    Raises:
        TypeError: document type not supported

    Returns:
        dict: jarvis supported document
    """
    file_type = file_type.lower()
    if (
        file_type == "doc"
        or file_type == "docx"
        or file_type == "pdf"
        or file_type == "txt"
        or file_type == "html"
        or file_type == "rtf"
    ):

        document_dict = {
            "id": str(unique_id),
            "doctype": doc_type,
            "base64Data": file_stream,
            "filetype": str(file_type)
        }
        return document_dict

    else:
        raise TypeError(f"Error on document type = {file_type} is not supported")

def fetch_document_vectors_from_api(documents: list, embedding_url: str, api_key: str):
    """fetch vectors for given list of documents from jarvis

    Args:
        documents (list): _description_
        embedding_url (str): _description_
        api_key (str): _description_

    Raises:
        requests.exceptions.RequestException: _description_

    Returns:
        list, list: records, errors
    """
    documents_json = {"documents": documents}

    header = {
        "Authorization": "Bearer " + str(api_key),
        "Content-Type": "application/json"
    }

    response = requests.post(embedding_url, headers=header, json=documents_json)

    if response.status_code != 200:
        # should the lambda fail on error? Or just write error to athena?
        raise requests.exceptions.RequestException(
            "error ({}): {}".format(response.status_code, response.raise_for_status())
        )


    resp_json = response.json()

    results = []
    if "results" in resp_json:
        # structure results for response
        
        for record in resp_json["results"]:
            result = {}

            result["entity_id"] = record["id"]
            result["properties"] = {}
            result["properties"]["doctype"] = record["doctype"]
            result["properties"]["title"] = record["title"]
            result["properties"]["skills"] = record["skills"]

            result["properties"]["embedding"] = {}
            result["properties"]["embedding"]["dim"] = record["embedding"]["dim"]
            result["properties"]["embedding"]["vector"] = record["embedding"]["vector"]
            results.append(result)

    errors = []
    if "errors" in resp_json:
        # individual items can fail due to API not being able to extract information or match skills
        
        for record in resp_json["errors"]:
            error = {}
            error["errorCode"] = record["errorCode"]
            error["errorCode"] = record["errorMessage"]
            # structure errors to raise
            errors.append(error)

    return results, errors


def slice_list_in_to_buckets(items: List[Any], max_buckets: int = None, chunk_size: int = None) -> List[List[Any]]:
    """create bucketted list of items from a single list of items

    Args:
        items (List[Any]): items to bucket
        max_buckets (int, optional): max number of buckets. Defaults to None.
        chunk_size (int, optional): max size of each bucket. Defaults to None.

    Raises:
        Exception: Must provide max_buckets or chunk_size

    Returns:
        List[List[Any]]: bucketted list of items
    """
    if chunk_size is not None:
        max_buckets = math.ceil(len(items) / chunk_size)
    if max_buckets is None:
        raise Exception("Provide either max_buckets or chunk_size.")
    n_baskets = min(max_buckets, len(items))
    return [items[i::n_baskets] for i in range(n_baskets)]

def compile_documents_for_jarvis(records: List[Dict[str, str]]) -> List[Dict[str, str]]:
    """compile a document records for jarvis

    Args:
        records (List[Dict[str, str]]): records to compile for jarvis

    Returns:
        List[Dict[str, str]]: compiled documents for jarvis
    """
    compiled_documents = []

    for record in records:
        entity_id = record["entity_id"]
        entity_type = record["entity_type"]
        bucket_name = record["bucket"]
        file_path = record["file_path"]
        file_type = record["file_type"]

        # execute scoring workflow
        file_stream = read_file_stream_from_s3(bucket_name, file_path)
        compile_document = compile_document_for_request(
            file_stream=file_stream,
            doc_type="cv" if entity_type == "candidates" else "job",
            file_type=file_type,
            unique_id=entity_id
        )
        compiled_documents.append(compile_document)
    
    return compiled_documents

def batch_and_fetch_vectors(records: List[Dict[str, str]], compiled_documents: List[Dict[str, str]], embedding_url: str, api_key: str, **kwargs):
    """batch reocrds and fetch vectors from jarvis

    Args:
        records (List[Dict[str, str]]): document records
        compiled_documents (List[Dict[str, str]]): compiled document records
        embedding_url (str): url for jarvis api
        api_key (str): api key for jarvis api

    Returns:
        list, list: results, errors
    """
    created_at = kwargs.get('created_at')
    chunk_size = kwargs.get('chunk_size', 10)

    print("batch and fetch documents from jarvis")
    final_results = []
    final_errors = []
    chunk_index = slice_list_in_to_buckets(items=range(len(compiled_documents)), chunk_size=chunk_size)
    for chunk in chunk_index:

        records_i = [records[i] for i in chunk]
        compiled_documents_i = [compiled_documents[i] for i in chunk]

        results, errors = fetch_document_vectors_from_api(
            documents=compiled_documents_i,
            embedding_url=embedding_url,
            api_key=api_key
        )

        for i, record_i in enumerate(records_i):
            results[i].update(
                {
                    'entity_type': record_i["entity_type"],
                    'source': 'jarvis',
                    'created_at': created_at
                }
            )

        final_results.extend(results)
        final_errors.extend(errors)
    
    return final_results, final_errors
