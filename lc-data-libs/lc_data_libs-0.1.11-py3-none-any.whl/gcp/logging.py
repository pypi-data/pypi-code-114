import os
import google.cloud.logging
from google.cloud.logging_v2.resource import Resource
from google.cloud.logging_v2._helpers import retrieve_metadata_server
from google.cloud import dataproc_v1


def get_execution_id_from_request(request):
    return request.headers.get("Function-Execution-Id")

def get_execution_id_from_context(context):
    return context.event_id

def get_gcp_handler(type, labels):

    client = google.cloud.logging.Client()
    if type=='cloud_dataproc_job':
        name, resource, labels = _get_dataproc_resource_labels(client, labels)
        handler = client.get_default_handler(name=name, resource=resource, labels=labels)
    else:
        handler = client.get_default_handler(labels=labels)
    return handler

def _get_dataproc_resource_labels(logclient, labels):

    # Get step_id and job_id
    job_id = os.environ['PWD'].split('/')[-1]
    step_id = job_id.rsplit('-',1)[0]

    # Get job_uuid
    region = retrieve_metadata_server("instance/attributes/dataproc-region")
    client = dataproc_v1.JobControllerClient(
        client_options={'api_endpoint': 'europe-west1-dataproc.googleapis.com:443'})
    job = client.get_job(project_id=logclient.project, region=region, job_id=job_id)
    job_uuid = job.job_uuid

    # Complete labels
    labels['step_id'] = step_id
    labels["dataproc.googleapis.com/cluster_name"] = retrieve_metadata_server("instance/attributes/dataproc-cluster-name")
    labels["dataproc.googleapis.com/cluster_uuid"] = retrieve_metadata_server("instance/attributes/dataproc-cluster-uuid")

    # Create resource
    name = "dataproc.job.driver"
    resource = Resource(
        type='cloud_dataproc_job',
        labels={
            'job_id': job_id,
            'job_uuid': job_uuid,
            'region': region
        }
    )

    return name, resource, labels


def add_labels(logger, labels):
    for h in logger.handlers:
        if hasattr(h,'labels'):
            h.labels.update(labels)

def add_gcp_handler(logger, type, labels):
    gcp_handler = get_gcp_handler(type, labels)
    logger.addHandler(gcp_handler)
    return logger
