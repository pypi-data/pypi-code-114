from collections import OrderedDict
from pathlib import Path
from typing import Optional, Dict, Union, List

from phidata.app import PhidataApp, PhidataAppArgs
from phidata.infra.docker.resource.network import DockerNetwork
from phidata.infra.docker.resource.container import DockerContainer
from phidata.infra.docker.resource.group import (
    DockerResourceGroup,
    DockerBuildContext,
)
from phidata.infra.k8s.create.core.v1.config_map import CreateConfigMap
from phidata.infra.k8s.create.core.v1.container import CreateContainer
from phidata.infra.k8s.create.apps.v1.deployment import CreateDeployment
from phidata.infra.k8s.create.core.v1.secret import CreateSecret
from phidata.infra.k8s.create.core.v1.service import CreateService, ServiceType
from phidata.infra.k8s.create.core.v1.persistent_volume import CreatePersistentVolume
from phidata.infra.k8s.create.core.v1.volume import (
    CreateVolume,
    EmptyDirVolumeSource,
    HostPathVolumeSource,
    VolumeType,
)
from phidata.infra.k8s.create.common.port import CreatePort
from phidata.infra.k8s.create.group import CreateK8sResourceGroup
from phidata.infra.k8s.resource.group import (
    K8sResourceGroup,
    K8sBuildContext,
)
from phidata.utils.common import (
    get_image_str,
    get_default_container_name,
    get_default_configmap_name,
    get_default_secret_name,
    get_default_service_name,
    get_default_volume_name,
    get_default_deploy_name,
    get_default_pod_name,
)
from phidata.utils.enums import ExtendedEnum
from phidata.utils.cli_console import print_error, print_info, print_warning
from phidata.utils.log import logger


class PostgresVolumeType(ExtendedEnum):
    EMPTY_DIR = "EMPTY_DIR"
    HOST_PATH = "HOST_PATH"
    PERSISTENT_VOLUME = "PERSISTENT_VOLUME"
    AWS_EBS = "AWS_EBS"
    GCE_PERSISTENT_DISK = "GCE_PERSISTENT_DISK"


class PostgresDbArgs(PhidataAppArgs):
    name: str = "postgres"
    version: str = "1"
    enabled: bool = True

    # Image Args
    image_name: str = "postgres"
    image_tag: str = "14"
    # Add env variables to container env
    # keys: var name
    # values: var values
    env: Optional[Dict[str, str]] = None

    ## Configure the Postgres env
    postgres_db: Optional[str] = None
    postgres_user: Optional[str] = None
    postgres_password: Optional[str] = None
    pgdata: Optional[str] = "/var/lib/postgresql/data/pgdata"
    postgres_initdb_args: Optional[str] = None
    postgres_initdb_waldir: Optional[str] = None
    postgres_host_auth_method: Optional[str] = None
    postgres_password_file: Optional[str] = None
    postgres_user_file: Optional[str] = None
    postgres_db_file: Optional[str] = None
    postgres_initdb_args_file: Optional[str] = None

    ## Configure the Postgres volume
    create_volume: bool = True
    volume_type: PostgresVolumeType = PostgresVolumeType.EMPTY_DIR
    volume_name: Optional[str] = None
    # Container path to mount the postgres volume
    volume_container_path: str = "/var/lib/postgresql/data"
    # Host path to mount the postgres volume
    # If volume_type = PostgresVolumeType.HOST_PATH
    volume_host_path: Optional[Path] = None

    ## Configure the Postgres container
    container_name: Optional[str] = None
    container_port: int = 5432
    # Only used by the K8sContainer
    container_port_name: str = "pg"
    # Only used by the DockerContainer
    container_host_port: int = 5432
    container_detach: bool = True
    container_auto_remove: bool = True
    container_remove: bool = True

    ## Configure the Postgres deploy
    deploy_name: Optional[str] = None
    pod_name: Optional[str] = None
    # Options used by the K8s ConfigMap used
    # to set the container env variables which are not Secret
    config_map_name: Optional[str] = None
    # Options used by the K8s Secret used
    # to set the container env variables which are Secret
    secret_name: Optional[str] = None
    # Read secrets from a file in yaml format
    secrets_file: Optional[str] = None

    ## Configure the Postgres service
    service_name: Optional[str] = None
    # Service type
    service_type: Optional[ServiceType] = None
    # The port that will be exposed by the service.
    service_port: int = 5432
    # The node_port that will be exposed by the service.
    # If service_type = ServiceType.CLUSTER_IP
    node_port: Optional[int] = None
    # The target_port is the port to access on the pods targeted by the service.
    # It can be the port number or port name on the pod.
    target_port: Optional[Union[str, int]] = None


class PostgresDb(PhidataApp):
    def __init__(
        self,
        name: str = "postgres",
        version: str = "1",
        enabled: bool = True,
        # Image Args
        image_name: str = "postgres",
        image_tag: str = "14",
        # Add env variables to container env
        env: Optional[Dict[str, str]] = None,
        ## Configure the Postgres env,
        postgres_db: Optional[str] = None,
        postgres_user: Optional[str] = None,
        postgres_password: Optional[str] = None,
        pgdata: Optional[str] = "/var/lib/postgresql/data/pgdata",
        postgres_initdb_args: Optional[str] = None,
        postgres_initdb_waldir: Optional[str] = None,
        postgres_host_auth_method: Optional[str] = None,
        postgres_password_file: Optional[str] = None,
        postgres_user_file: Optional[str] = None,
        postgres_db_file: Optional[str] = None,
        postgres_initdb_args_file: Optional[str] = None,
        ## Configure the Postgres volume
        create_volume: bool = True,
        volume_type: PostgresVolumeType = PostgresVolumeType.EMPTY_DIR,
        volume_name: Optional[str] = None,
        # Container path to mount the postgres volume,
        volume_container_path: str = "/var/lib/postgresql/data",
        # Host path to mount the postgres volume,
        # If volume_type = PostgresVolumeType.HOST_PATH,
        volume_host_path: Optional[Path] = None,
        ## Configure the Postgres container,
        container_name: Optional[str] = None,
        container_port: int = 5432,
        # Options used by the Docker Container
        container_host_port: int = 5432,
        container_detach: bool = True,
        container_auto_remove: bool = True,
        container_remove: bool = True,
        # Options used by the K8s Container
        container_port_name: str = "pg",
        # Options used by the K8s Deploy
        deploy_name: Optional[str] = None,
        pod_name: Optional[str] = None,
        # Options used by the K8s ConfigMap used
        # to set the container env variables which are not Secret
        config_map_name: Optional[str] = None,
        # Options used by the K8s Secret used
        # to set the container env variables which are Secret
        secret_name: Optional[str] = None,
        # Read secrets from a file in yaml format
        secrets_file: Optional[str] = None,
        # Options used by the K8s Service
        service_name: Optional[str] = None,
        # Service type
        service_type: Optional[ServiceType] = None,
        # The port that will be exposed by the service.
        service_port: int = 5432,
        # The node_port that will be exposed by the service.
        node_port: Optional[int] = None,
        target_port: Optional[Union[str, int]] = None,
    ):
        super().__init__()
        try:
            self.args: PostgresDbArgs = PostgresDbArgs(
                name=name,
                version=version,
                enabled=enabled,
                image_name=image_name,
                image_tag=image_tag,
                env=env,
                postgres_db=postgres_db,
                postgres_user=postgres_user,
                postgres_password=postgres_password,
                pgdata=pgdata,
                postgres_initdb_args=postgres_initdb_args,
                postgres_initdb_waldir=postgres_initdb_waldir,
                postgres_host_auth_method=postgres_host_auth_method,
                postgres_password_file=postgres_password_file,
                postgres_user_file=postgres_user_file,
                postgres_db_file=postgres_db_file,
                postgres_initdb_args_file=postgres_initdb_args_file,
                create_volume=create_volume,
                volume_type=volume_type,
                volume_name=volume_name,
                volume_container_path=volume_container_path,
                volume_host_path=volume_host_path,
                container_name=container_name,
                container_port=container_port,
                container_port_name=container_port_name,
                container_host_port=container_host_port,
                container_detach=container_detach,
                container_auto_remove=container_auto_remove,
                container_remove=container_remove,
                deploy_name=deploy_name,
                pod_name=pod_name,
                config_map_name=config_map_name,
                secret_name=secret_name,
                secrets_file=secrets_file,
                service_name=service_name,
                service_type=service_type,
                service_port=service_port,
                node_port=node_port,
                target_port=target_port,
            )
        except Exception:
            logger.error(f"Args for {self.__class__.__name__} are not valid")
            raise

    def get_container_name(self) -> str:
        return self.args.container_name or get_default_container_name(self.args.name)

    def get_service_name(self) -> str:
        return self.args.service_name or get_default_service_name(self.args.name)

    def get_connection_url_docker(self):
        user = self.args.postgres_user
        password = self.args.postgres_password
        host = self.get_container_name()
        port = self.args.container_port
        db = self.args.postgres_db
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"

    def get_connection_url_local(self):
        user = self.args.postgres_user
        password = self.args.postgres_password
        host = "localhost"
        port = self.args.container_host_port
        db = self.args.postgres_db
        return f"postgresql://{user}:{password}@{host}:{port}/{db}"

    ######################################################
    ## Docker Resources
    ######################################################

    def get_postgres_docker_rg(
        self, docker_build_context: DockerBuildContext
    ) -> Optional[DockerResourceGroup]:
        logger.debug(f"Init Postgres DockerResourceGroup")

        app_name = self.args.name
        ## Create a dict to set the container env
        container_env = {
            "POSTGRES_USER": self.args.postgres_user,
            "POSTGRES_PASSWORD": self.args.postgres_password,
            "POSTGRES_DB": self.args.postgres_db,
            "PGDATA": self.args.pgdata,
        }
        # Update the container env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            container_env.update(self.args.env)

        ## Create the container volumes
        container_volumes = {}
        if self.args.create_volume:
            volume_name = self.args.volume_name or get_default_volume_name(app_name)
            if self.args.volume_type == PostgresVolumeType.EMPTY_DIR:
                container_volumes[volume_name] = {
                    "bind": self.args.volume_container_path,
                    "mode": "rw",
                }
            elif self.args.volume_type == PostgresVolumeType.HOST_PATH:
                if self.args.volume_host_path is not None:
                    volume_host_path_str = str(self.args.volume_host_path)
                    container_volumes[volume_host_path_str] = {
                        "bind": self.args.volume_container_path,
                        "mode": "rw",
                    }
                else:
                    print_error("PostgresDb: volume_host_path not provided")
                    return None
            else:
                print_error(f"{self.args.volume_type.value} not supported")
                return None

        ## Create the container
        docker_container = DockerContainer(
            name=self.get_container_name(),
            image=get_image_str(self.args.image_name, self.args.image_tag),
            detach=self.args.container_detach,
            auto_remove=self.args.container_auto_remove,
            remove=self.args.container_remove,
            environment=container_env,
            network=docker_build_context.network,
            ports={
                str(self.args.container_port): self.args.container_host_port,
            },
            volumes=container_volumes,
        )

        docker_rg = DockerResourceGroup(
            name=app_name,
            enabled=self.args.enabled,
            network=DockerNetwork(name=docker_build_context.network),
            containers=[docker_container],
        )
        return docker_rg

    def init_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> None:
        docker_rg: Optional[DockerResourceGroup] = self.get_postgres_docker_rg(
            docker_build_context
        )
        # logger.debug("docker_rg:\n{}".format(docker_rg.json(indent=2)))
        if docker_rg is not None:
            if self.docker_resource_groups is None:
                self.docker_resource_groups = OrderedDict()
            self.docker_resource_groups[docker_rg.name] = docker_rg

    ######################################################
    ## K8s Resources
    ######################################################

    def get_postgres_k8s_rg(
        self, k8s_build_context: K8sBuildContext
    ) -> Optional[K8sResourceGroup]:
        logger.debug(f"Init Postgres K8sResourceGroup")

        app_name = self.args.name
        ## Create a ConfigMap to set the container env variables which are not Secret
        container_env_cm = CreateConfigMap(
            cm_name=self.args.config_map_name or get_default_configmap_name(app_name),
            app_name=app_name,
            data={
                "POSTGRES_USER": self.args.postgres_user,
                "POSTGRES_DB": self.args.postgres_db,
                "PGDATA": self.args.pgdata,
                "POSTGRES_INITDB_ARGS": self.args.postgres_initdb_args,
                "POSTGRES_INITDB_WALDIR": self.args.postgres_initdb_waldir,
                "POSTGRES_HOST_AUTH_METHOD": self.args.postgres_host_auth_method,
                "POSTGRES_PASSWORD_FILE": self.args.postgres_password_file,
                "POSTGRES_USER_FILE": self.args.postgres_user_file,
                "POSTGRES_DB_FILE": self.args.postgres_db_file,
                "POSTGRES_INITDB_ARGS_FILE": self.args.postgres_initdb_args_file,
            },
        )
        # Update the container env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            if container_env_cm.data is not None and isinstance(
                container_env_cm.data, dict
            ):
                container_env_cm.data.update(self.args.env)

        ## Create a Secret to set the container env variables which are Secret
        container_secrets: List[CreateSecret] = []
        if self.args.postgres_password is not None:
            container_secrets.append(
                CreateSecret(
                    secret_name=self.args.secret_name
                    or get_default_secret_name(f"{app_name}-pg"),
                    app_name=app_name,
                    data={
                        "POSTGRES_PASSWORD": self.args.postgres_password,
                    },
                )
            )
        if self.args.secrets_file is not None:
            try:
                import yaml

                secrets_file_path = Path(self.args.secrets_file)
                if secrets_file_path.exists() and secrets_file_path.is_file():
                    secrets_from_file = yaml.safe_load(secrets_file_path.read_text())
                    if secrets_from_file is not None and isinstance(
                        secrets_from_file, dict
                    ):
                        for secret_name, secret_data in secrets_from_file.items():
                            if (
                                secret_name is None
                                or secret_data is None
                                or not isinstance(secret_data, dict)
                            ):
                                print_error("Invalid secret")
                                continue

                            container_secrets.append(
                                CreateSecret(
                                    secret_name=secret_name,
                                    app_name=app_name,
                                    data=secret_data,
                                )
                            )
                    else:
                        print_error("Cannot read secrets_file")
                else:
                    print_error("Invalid secrets_file")
            except Exception as e:
                print_error("Encountered error when reading secrets_file, please fix")
                print_error(e)

        ## Create the container volumes
        container_volumes = []
        if self.args.create_volume:
            volume_name = self.args.volume_name or get_default_volume_name(app_name)
            if self.args.volume_type == PostgresVolumeType.EMPTY_DIR:
                _volume = CreateVolume(
                    volume_name=volume_name,
                    app_name=app_name,
                    mount_path=self.args.volume_container_path,
                    volume_type=VolumeType.EMPTY_DIR,
                )
                container_volumes.append(_volume)
            elif self.args.volume_type == PostgresVolumeType.HOST_PATH:
                if self.args.volume_host_path is not None:
                    volume_host_path_str = str(self.args.volume_host_path)
                    pg_volume = CreateVolume(
                        volume_name=volume_name,
                        app_name=app_name,
                        mount_path=self.args.volume_container_path,
                        volume_type=VolumeType.HOST_PATH,
                        host_path=HostPathVolumeSource(
                            path=volume_host_path_str,
                        ),
                    )
                    container_volumes.append(pg_volume)
                else:
                    print_error("PostgresDb: volume_host_path not provided")
                    return None
            elif self.args.volume_type == PostgresVolumeType.AWS_EBS:
                print_info(f"TO_IMPLEMENT volume_type: {self.args.volume_type.value}")
                return None
            else:
                print_error(f"{self.args.volume_type.value} not supported")
                return None

        ## Create the ports to open
        container_port = CreatePort(
            name=self.args.container_port_name,
            container_port=self.args.container_port,
            service_port=self.args.service_port,
            target_port=self.args.target_port or self.args.container_port_name,
        )

        # If ServiceType == NODE_PORT then validate self.args.node_port is available
        if self.args.service_type == ServiceType.NODE_PORT:
            if (
                self.args.node_port is None
                or self.args.node_port < 30000
                or self.args.node_port > 32767
            ):
                print_error(f"NodePort: {self.args.node_port} invalid")
                print_error(f"Skipping this service")
                return None
            else:
                container_port.node_port = self.args.node_port
        # If ServiceType == LOAD_BALANCER then validate self.args.node_port only IF available
        elif self.args.service_type == ServiceType.LOAD_BALANCER:
            if self.args.node_port is not None:
                if self.args.node_port < 30000 or self.args.node_port > 32767:
                    print_error(f"NodePort: {self.args.node_port} invalid")
                    print_error(f"Skipping this service")
                    return None
                else:
                    container_port.node_port = self.args.node_port
        # else validate self.args.node_port is NOT available
        elif self.args.node_port is not None:
            print_warning(
                f"NodePort: {self.args.node_port} provided without specifying ServiceType as NODE_PORT or LOAD_BALANCER"
            )
            print_warning("NodePort value will be ignored")
            self.args.node_port = None

        ## Create the container
        k8s_container = CreateContainer(
            container_name=self.get_container_name(),
            app_name=app_name,
            image_name=self.args.image_name,
            image_tag=self.args.image_tag,
            envs_from_configmap=[container_env_cm.cm_name],
            envs_from_secret=[secret.secret_name for secret in container_secrets],
            ports=[container_port],
            volumes=container_volumes,
        )

        ## Create the deployment
        k8s_deployment = CreateDeployment(
            deploy_name=self.args.deploy_name or get_default_deploy_name(app_name),
            pod_name=self.args.pod_name or get_default_pod_name(app_name),
            app_name=app_name,
            namespace=k8s_build_context.namespace,
            service_account_name=k8s_build_context.service_account_name,
            containers=[k8s_container],
            volumes=container_volumes,
            labels=k8s_build_context.labels,
        )

        ## Create the service
        k8s_service = CreateService(
            service_name=self.get_service_name(),
            app_name=app_name,
            namespace=k8s_build_context.namespace,
            service_account_name=k8s_build_context.service_account_name,
            service_type=self.args.service_type,
            deployment=k8s_deployment,
            ports=[container_port],
            labels=k8s_build_context.labels,
        )

        ## Create the K8sResourceGroup
        k8s_resource_group = CreateK8sResourceGroup(
            name=app_name,
            enabled=self.args.enabled,
            config_maps=[container_env_cm],
            secrets=container_secrets,
            services=[k8s_service],
            deployments=[k8s_deployment],
        )
        return k8s_resource_group.create()

    def init_k8s_resource_groups(self, k8s_build_context: K8sBuildContext) -> None:
        k8s_rg: Optional[K8sResourceGroup] = self.get_postgres_k8s_rg(k8s_build_context)
        # logger.debug("k8s_rg:\n{}".format(k8s_rg.json(indent=2)))
        if k8s_rg is not None:
            if self.k8s_resource_groups is None:
                self.k8s_resource_groups = OrderedDict()
            self.k8s_resource_groups[k8s_rg.name] = k8s_rg
