import logging
from contextlib import contextmanager
from typing import Collection, Dict, Optional

import kubernetes
import kubernetes.client as client
from dagster import Array, BoolSource, Field, IntSource, Noneable, Permissive, StringSource, check
from dagster.config.field_utils import Shape
from dagster.core.executor.step_delegating import StepHandler
from dagster.core.host_representation.grpc_server_registry import GrpcServerEndpoint
from dagster.serdes import ConfigurableClass
from dagster.utils import ensure_single_item, merge_dicts
from dagster_cloud.executor import (
    DAGSTER_CLOUD_EXECUTOR_K8S_CONFIG_KEY,
    DAGSTER_CLOUD_EXECUTOR_NAME,
)
from dagster_cloud.workspace.origin import CodeDeploymentMetadata
from dagster_k8s import K8sRunLauncher
from dagster_k8s.executor import K8sStepHandler
from dagster_k8s.job import DagsterK8sJobConfig
from dagster_k8s.models import k8s_snake_case_dict
from kubernetes.client.rest import ApiException

from ..user_code_launcher import DEFAULT_SERVER_PROCESS_STARTUP_TIMEOUT, ReconcileUserCodeLauncher
from .utils import (
    SERVICE_PORT,
    construct_repo_location_deployment,
    construct_repo_location_service,
    get_unique_label_for_location,
    unique_resource_name,
    wait_for_deployment_complete,
)

DEFAULT_DEPLOYMENT_STARTUP_TIMEOUT = 300
DEFAULT_IMAGE_PULL_GRACE_PERIOD = 30


class K8sUserCodeLauncher(ReconcileUserCodeLauncher[str], ConfigurableClass):
    def __init__(
        self,
        dagster_home,
        instance_config_map,
        inst_data=None,
        namespace=None,
        kubeconfig_file=None,
        pull_policy=None,
        env_config_maps=None,
        env_secrets=None,
        service_account_name=None,
        volume_mounts=None,
        volumes=None,
        image_pull_secrets=None,
        deployment_startup_timeout=None,
        server_process_startup_timeout=None,
        image_pull_grace_period=None,
        labels=None,
    ):
        self._inst_data = inst_data
        self._logger = logging.getLogger("K8sUserCodeLauncher")
        self._dagster_home = check.str_param(dagster_home, "dagster_home")
        self._instance_config_map = check.str_param(instance_config_map, "instance_config_map")
        self._namespace = namespace
        self._pull_policy = pull_policy
        self._env_config_maps = check.opt_list_param(
            env_config_maps, "env_config_maps", of_type=str
        )
        self._env_secrets = check.opt_list_param(env_secrets, "env_secrets", of_type=str)
        self._service_account_name = check.str_param(service_account_name, "service_account_name")
        self._volume_mounts = [
            k8s_snake_case_dict(kubernetes.client.V1VolumeMount, mount)
            for mount in check.opt_list_param(volume_mounts, "volume_mounts")
        ]
        self._volumes = [
            k8s_snake_case_dict(kubernetes.client.V1Volume, volume)
            for volume in check.opt_list_param(volumes, "volumes")
        ]
        self._image_pull_secrets = check.opt_list_param(
            image_pull_secrets, "image_pull_secrets", of_type=dict
        )
        self._deployment_startup_timeout = check.opt_int_param(
            deployment_startup_timeout,
            "deployment_startup_timeout",
            DEFAULT_DEPLOYMENT_STARTUP_TIMEOUT,
        )
        self._server_process_startup_timeout = check.opt_int_param(
            server_process_startup_timeout,
            "server_process_startup_timeout",
            DEFAULT_SERVER_PROCESS_STARTUP_TIMEOUT,
        )
        self._image_pull_grace_period = check.opt_int_param(
            image_pull_grace_period,
            "image_pull_grace_period",
            DEFAULT_IMAGE_PULL_GRACE_PERIOD,
        )
        self._labels = check.opt_dict_param(labels, "labels", key_type=str, value_type=str)

        if kubeconfig_file:
            kubernetes.config.load_kube_config(kubeconfig_file)
        else:
            kubernetes.config.load_incluster_config()

        super(K8sUserCodeLauncher, self).__init__()

        self._launcher = K8sRunLauncher(
            dagster_home=self._dagster_home,
            instance_config_map=self._instance_config_map,
            postgres_password_secret=None,
            job_image=None,
            image_pull_policy=self._pull_policy,
            image_pull_secrets=self._image_pull_secrets,
            service_account_name=self._service_account_name,
            env_config_maps=self._env_config_maps,
            env_secrets=self._env_secrets,
            job_namespace=self._namespace,
            volume_mounts=self._volume_mounts,
            volumes=self._volumes,
            labels=self._labels,
        )

    @property
    def requires_images(self):
        return True

    def register_instance(self, instance):
        super().register_instance(instance)
        self._launcher.register_instance(instance)

    @property
    def inst_data(self):
        return self._inst_data

    @classmethod
    def config_type(cls):
        return {
            "dagster_home": Field(StringSource, is_required=True),
            "instance_config_map": Field(StringSource, is_required=True),
            "namespace": Field(StringSource, is_required=False, default_value="default"),
            "kubeconfig_file": Field(StringSource, is_required=False),
            "pull_policy": Field(StringSource, is_required=False, default_value="Always"),
            "env_config_maps": Field(
                Noneable(Array(StringSource)),
                is_required=False,
                description="A list of custom ConfigMapEnvSource names from which to draw "
                "environment variables (using ``envFrom``) for the Job. Default: ``[]``. See:"
                "https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/#define-an-environment-variable-for-a-container",
            ),
            "env_secrets": Field(
                Noneable(Array(StringSource)),
                is_required=False,
                description="A list of custom Secret names from which to draw environment "
                "variables (using ``envFrom``) for the Job. Default: ``[]``. See:"
                "https://kubernetes.io/docs/tasks/inject-data-application/distribute-credentials-secure/#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables",
            ),
            "service_account_name": Field(
                Noneable(StringSource),
                is_required=True,
                description="The name of the Kubernetes service account under which to run.",
            ),
            "volume_mounts": Field(
                Array(
                    Shape(
                        {
                            "name": StringSource,
                            "mountPath": StringSource,
                            "mountPropagation": Field(StringSource, is_required=False),
                            "readOnly": Field(BoolSource, is_required=False),
                            "subPath": Field(StringSource, is_required=False),
                            "subPathExpr": Field(StringSource, is_required=False),
                        }
                    )
                ),
                is_required=False,
                default_value=[],
                description="A list of volume mounts to include in the job's container. Default: ``[]``. See: "
                "https://v1-18.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#volumemount-v1-core",
            ),
            "volumes": Field(
                Array(
                    Permissive(
                        {
                            "name": str,
                        }
                    )
                ),
                is_required=False,
                default_value=[],
                description="A list of volumes to include in the Job's Pod. Default: ``[]``. For the many "
                "possible volume source types that can be included, see: "
                "https://v1-18.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.18/#volume-v1-core",
            ),
            "image_pull_secrets": Field(
                Noneable(Array(Shape({"name": StringSource}))),
                is_required=False,
                description="Specifies that Kubernetes should get the credentials from "
                "the Secrets named in this list.",
            ),
            "labels": Field(
                dict,
                is_required=False,
                description="Labels to apply to the pods created by the agent.",
            ),
            "deployment_startup_timeout": Field(
                IntSource,
                is_required=False,
                default_value=DEFAULT_DEPLOYMENT_STARTUP_TIMEOUT,
                description="Timeout when creating a new Kubernetes deployment for a code server",
            ),
            "server_process_startup_timeout": Field(
                IntSource,
                is_required=False,
                default_value=DEFAULT_SERVER_PROCESS_STARTUP_TIMEOUT,
                description="Timeout when waiting for a code server to be ready after it is created",
            ),
            "image_pull_grace_period": Field(
                IntSource,
                is_required=False,
                default_value=DEFAULT_IMAGE_PULL_GRACE_PERIOD,
            ),
        }

    @staticmethod
    def from_config_value(inst_data, config_value):
        return K8sUserCodeLauncher(
            dagster_home=config_value.get("dagster_home"),
            instance_config_map=config_value.get("instance_config_map"),
            inst_data=inst_data,
            namespace=config_value.get("namespace"),
            kubeconfig_file=config_value.get("kubeconfig_file"),
            pull_policy=config_value.get("pull_policy"),
            env_config_maps=config_value.get("env_config_maps", []),
            env_secrets=config_value.get("env_secrets", []),
            service_account_name=config_value.get("service_account_name"),
            image_pull_secrets=config_value.get("image_pull_secrets"),
            volume_mounts=config_value.get("volume_mounts"),
            volumes=config_value.get("volumes"),
            deployment_startup_timeout=config_value.get("deployment_startup_timeout"),
            server_process_startup_timeout=config_value.get("server_process_startup_timeout"),
            image_pull_grace_period=config_value.get("image_pull_grace_period"),
            labels=config_value.get("labels"),
        )

    @contextmanager
    def _get_api_instance(self):
        with client.ApiClient() as api_client:  # pylint: disable=not-context-manager
            yield client.AppsV1Api(api_client)

    def _create_new_server_endpoint(
        self, location_name: str, metadata: CodeDeploymentMetadata
    ) -> GrpcServerEndpoint:
        resource_name = unique_resource_name(location_name)

        try:
            with self._get_api_instance() as api_instance:
                api_response = api_instance.create_namespaced_deployment(
                    self._namespace,
                    construct_repo_location_deployment(
                        location_name,
                        resource_name,
                        metadata,
                        self._pull_policy,
                        self._env_config_maps,
                        self._env_secrets,
                        self._service_account_name,
                        self._image_pull_secrets,
                        self._volume_mounts,
                        self._volumes,
                        self._labels,
                    ),
                )
            self._logger.info("Created deployment: {}".format(api_response.metadata.name))
        except ApiException as e:
            self._logger.error(
                "Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e
            )
            raise e

        try:
            api_response = client.CoreV1Api().create_namespaced_service(
                self._namespace,
                construct_repo_location_service(location_name, resource_name),
            )
            self._logger.info("Created service: {}".format(api_response.metadata.name))
        except ApiException as e:
            self._logger.error(
                "Exception when calling AppsV1Api->create_namespaced_service: %s\n" % e
            )
            raise e

        wait_for_deployment_complete(
            resource_name,
            self._namespace,
            self._logger,
            location_name,
            metadata,
            existing_pods=[],
            timeout=self._deployment_startup_timeout,
            image_pull_grace_period=self._image_pull_grace_period,
        )
        server_id = self._wait_for_server(
            host=resource_name, port=SERVICE_PORT, timeout=self._server_process_startup_timeout
        )

        endpoint = GrpcServerEndpoint(
            server_id=server_id,
            host=resource_name,
            port=SERVICE_PORT,
            socket=None,
        )

        return endpoint

    def _get_server_handles_for_location(self, location_name: str) -> Collection[str]:
        with self._get_api_instance() as api_instance:
            deployments = api_instance.list_namespaced_deployment(
                self._namespace,
                label_selector=f"location_hash={get_unique_label_for_location(location_name)}",
            ).items
            return [deployment.metadata.name for deployment in deployments]

    def _cleanup_servers(self) -> None:
        with self._get_api_instance() as api_instance:
            deployments = api_instance.list_namespaced_deployment(
                self._namespace,
                label_selector="managed_by=K8sUserCodeLauncher",
            ).items
            for deployment in deployments:
                self._remove_server_handle(deployment.metadata.name)

    def _remove_server_handle(self, server_handle: str) -> None:
        check.str_param(server_handle, "server_handle")
        with self._get_api_instance() as api_instance:
            api_instance.delete_namespaced_deployment(server_handle, self._namespace)
        client.CoreV1Api().delete_namespaced_service(server_handle, self._namespace)
        self._logger.info("Removed deployment and service: {}".format(server_handle))

    def __exit__(self, exception_type, exception_value, traceback):
        super().__exit__(exception_value, exception_value, traceback)
        self._launcher.dispose()

    def get_step_handler(self, execution_config: Optional[Dict]) -> StepHandler:
        executor_name, exc_cfg = (
            ensure_single_item(execution_config) if execution_config else (None, {})
        )

        k8s_cfg = {}

        if executor_name == DAGSTER_CLOUD_EXECUTOR_NAME:
            k8s_cfg = exc_cfg.get(DAGSTER_CLOUD_EXECUTOR_K8S_CONFIG_KEY, {})

        return K8sStepHandler(
            job_config=DagsterK8sJobConfig(
                dagster_home=self._dagster_home,
                instance_config_map=self._instance_config_map,
                postgres_password_secret=None,
                job_image=None,
                image_pull_policy=(
                    k8s_cfg.get("image_pull_policy")
                    if k8s_cfg.get("image_pull_policy") != None
                    else self._pull_policy
                ),
                image_pull_secrets=self._image_pull_secrets
                + (k8s_cfg.get("image_pull_secrets") or []),
                service_account_name=(
                    k8s_cfg.get("service_account_name")
                    if k8s_cfg.get("service_account_name") != None
                    else self._service_account_name
                ),
                env_config_maps=self._env_config_maps + (k8s_cfg.get("env_config_maps") or []),
                env_secrets=self._env_secrets + (k8s_cfg.get("env_secrets") or []),
                volume_mounts=self._volume_mounts + (k8s_cfg.get("volume_mounts") or []),
                volumes=self._volumes + (k8s_cfg.get("volumes") or []),
                labels=merge_dicts(self._labels, exc_cfg.get("labels", {})),
            ),
            job_namespace=(
                k8s_cfg.get("job_namespace")
                if k8s_cfg.get("job_namespace") != None
                else self._namespace
            ),
            load_incluster_config=True,
            kubeconfig_file=None,
        )

    def run_launcher(self):
        return self._launcher
