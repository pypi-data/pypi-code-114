"""
Grouping of common functions used in Google Cloud Platform, intended to help other processes.
@maintainer: Richard Medina (rimedinaz at gmail dot com)
"""

def get_project(project_id=None):
    import os
    if project_id is not None:
        pass
    elif 'GCP_PROJECT' in os.environ:
        project_id = os.environ['GCP_PROJECT']
    elif 'GOOGLE_APPLICATION_CREDENTIALS' in os.environ:
        import json
        with open(os.environ['GOOGLE_APPLICATION_CREDENTIALS'], 'r') as fp:
            credentials = json.load(fp)
        project_id = credentials['project_id']
    else:
        raise Exception('Failed to determine project_id')
    return project_id

def get_secret(secretRef, project, version="latest"):
    """
    Access a secret from Google Secret Manager
    :param string secretRef: A Secret Manager secret name
    :param string project: GCP project name or project ID
    :param string version: Define a specific version to use, otherwise use latest
    :return: A plaintext secret value
    """
    from google.cloud import secretmanager
    client   = secretmanager.SecretManagerServiceClient()
    secret   = f"projects/{project}/secrets/{secretRef}/versions/{version}"

    try:
        response = client.access_secret_version(request={
            "name": secret
        })
    except Exception as e:
        return e

    return response.payload.data.decode("UTF-8")

def get_secret_json(secretRef, subitem, project_id = None, version="latest"):
    """
    Access a secret from Google Secret Manager (low cost version)
    :param string secretRef: A Secret Manager secret name
    :param string project_id: GCP project name or project ID
    :param string version: Define a specific version to use, otherwise use latest
    :return: A plaintext secret value
    """
    project_id = get_project(project_id=None)

    from google.cloud import secretmanager
    client   = secretmanager.SecretManagerServiceClient()
    secret   = f"projects/{project}/secrets/{secretRef}/versions/{version}"

    try:
        response = client.access_secret_version(request={
            "name": secret
        })
    except Exception as e:
        return e

    json_data = response.payload.data.decode("UTF-8")
    return json[password]