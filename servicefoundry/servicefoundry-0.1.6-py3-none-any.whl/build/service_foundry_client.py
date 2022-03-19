import jwt
import time

import requests
import json
import logging

from .const import TRUE_FOUNDRY_SERVER, REFRESH_ACCESS_TOKEN_IN_MIN
from .session import ServiceFoundrySession
from .session_factory import get_session
from .util import upload_package_to_s3


logger = logging.getLogger(__name__)


def _get_or_throw(definition, key, error_message):
    if key not in definition:
        raise RuntimeError(error_message)
    return definition[key]


class BadRequestException(Exception):
    def __init__(self, status_code, message=None):
        super(BadRequestException, self).__init__()
        self.status_code = status_code
        self.message = message


def request_handling(res):
    if 200 <= res.status_code <= 299:
        if res.content == b"":
            return None
        return res.json()
    if 400 <= res.status_code <= 499:
        try:
            message = res.json()["message"]
        except Exception:
            message = res
        raise BadRequestException(res.status_code, message)
    if 500 <= res.status_code <= 599:
        raise Exception(res.content)


class ServiceFoundryServiceClient:
    def __init__(self, session: ServiceFoundrySession, host=TRUE_FOUNDRY_SERVER):
        self.host = host
        self.session = session

    @staticmethod
    def get_client():
        # Would be ok to prefer auth token from API instead of local session file
        session = get_session()
        if session:
            return ServiceFoundryServiceClient(session)

    def check_and_refresh_session(self):
        decoded = jwt.decode(
            self.session.access_token, options={"verify_signature": False}
        )
        expiry_second = decoded["exp"]
        if expiry_second - time.time() < REFRESH_ACCESS_TOKEN_IN_MIN:
            logger.info(
                f"Going to refresh the access token {expiry_second - time.time()}."
            )
            self.session.refresh_access_token()

    def _get_header(self):
        return {"Authorization": f"Bearer {self.session.access_token}"}

    def list_workspace(self):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/workspace"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def create_workspace(self, cluster_name, name):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/workspace"
        res = requests.post(
            url,
            data={"name": name, "clusterId": cluster_name},
            headers=self._get_header(),
        )
        return request_handling(res)

    def remove_workspace(self, workspace_id):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/workspace/{workspace_id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_workspace(self, name):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/workspace/{name}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def list_service(self):
        self.check_and_refresh_session()
        url = f'{TRUE_FOUNDRY_SERVER}/service'
        res = requests.get(
            url, headers=self._get_header())
        return request_handling(res)

    def remove_service(self, service_id):
        self.check_and_refresh_session()
        url = f'{TRUE_FOUNDRY_SERVER}/service/{service_id}'
        res = requests.delete(
            url, headers=self._get_header())
        return request_handling(res)

    def get_service(self, service_id):
        self.check_and_refresh_session()
        url = f'{TRUE_FOUNDRY_SERVER}/service/{service_id}'
        res = requests.get(
            url, headers=self._get_header())
        return request_handling(res)

    def create_cluster(self, name, region, aws_account_id, ca_data, server_url):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/cluster"
        res = requests.post(
            url,
            data={
                "id": name,
                "region": region,
                "awsAccountID": aws_account_id,
                "authData": {"caData": ca_data, "serverURL": server_url},
            },
            headers=self._get_header(),
        )
        return request_handling(res)

    def list_cluster(self):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/cluster"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)

    def remove_cluster(self, cluster_id):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/cluster/{cluster_id}"
        res = requests.delete(url, headers=self._get_header())
        return request_handling(res)

    def get_presigned_url(self, space_name, service_name, env):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/deployment/generateUploadUrl"
        res = requests.post(
            url,
            data={"workSpaceId": space_name, "serviceName": service_name, "stage": env},
            headers=self._get_header(),
        )
        return request_handling(res)

    def build_and_deploy(self, service_def, package_zip, env):
        self.check_and_refresh_session()
        service_def_dict = json.loads(service_def.get_json())
        deployments = _get_or_throw(
            service_def_dict, "deployments", "Deployments not declared for this service"
        )
        deployment = _get_or_throw(deployments, env, f"Invalid env: {env}")
        space = _get_or_throw(
            deployment,
            "namespace",
            "TrueFoundry Space not specified for this environment",
        )

        http_response = self.get_presigned_url(space, service_def.name, env)
        upload_package_to_s3(http_response, package_zip)

        url = f"{TRUE_FOUNDRY_SERVER}/deployment"
        data = {
            "sfConfig": {
                "name": service_def.name,
                "build": service_def_dict["build"],
                "deployments": {env: deployment},
            },
            "s3Url": http_response["s3Url"],
        }

        deploy_response = requests.post(url, json=data, headers=self._get_header())
        return request_handling(deploy_response)

    def get_deployment(self, deployment_id):
        self.check_and_refresh_session()
        url = f"{TRUE_FOUNDRY_SERVER}/deployment/{deployment_id}"
        res = requests.get(url, headers=self._get_header())
        return request_handling(res)
