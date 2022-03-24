from typing import List, Optional

from kubernetes.client import CoreV1Api
from kubernetes.client.models.v1_pod import V1Pod
from kubernetes.client.models.v1_pod_list import V1PodList

from phidata.infra.k8s.api_client import K8sApiClient
from phidata.infra.k8s.resource.base import K8sResource


class Pod(K8sResource):
    """
    There are no attributes in the Pod model because we don't create Pods manually.
    This class exists only to read from the K8s cluster.

    References:
        * Doc: https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#pod-v1-core
        * Type: https://github.com/kubernetes-client/python/blob/master/kubernetes/client/models/v1_pod.py
    """

    resource_type: str = "Pod"

    @staticmethod
    def get_from_cluster(
        k8s_client: K8sApiClient, namespace: Optional[str] = None, **kwargs: str
    ) -> Optional[List[V1Pod]]:

        core_v1_api: CoreV1Api = k8s_client.core_v1_api
        pod_list: Optional[V1PodList] = None
        if namespace:
            # logger.debug(f"Getting Pods for ns: {namespace}")
            pod_list = core_v1_api.list_namespaced_pod(namespace=namespace)
        else:
            # logger.debug("Getting SA for all namespaces")
            pod_list = core_v1_api.list_pod_for_all_namespaces()

        pods: Optional[List[V1Pod]] = None
        if pod_list:
            pods = pod_list.items
        # logger.debug(f"pods: {pods}")
        # logger.debug(f"pods type: {type(pods)}")
        return pods
