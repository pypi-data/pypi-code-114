from collections import OrderedDict
from typing import Optional, Dict, Any, List, Union

from phidata.app import PhidataApp, PhidataAppArgs
from phidata.infra.docker.resource.network import DockerNetwork
from phidata.infra.docker.resource.container import DockerContainer
from phidata.infra.docker.resource.group import (
    DockerResourceGroup,
    DockerBuildContext,
)
from phidata.infra.k8s.create.apps.v1.deployment import CreateDeployment
from phidata.infra.k8s.create.core.v1.config_map import CreateConfigMap
from phidata.infra.k8s.create.core.v1.container import CreateContainer
from phidata.infra.k8s.create.core.v1.volume import (
    CreateVolume,
    EmptyDirVolumeSource,
    VolumeType,
)
from phidata.infra.k8s.create.common.port import CreatePort
from phidata.infra.k8s.create.group import CreateK8sResourceGroup
from phidata.infra.k8s.resource.group import (
    K8sResourceGroup,
    K8sBuildContext,
)
from phidata.utils.common import (
    get_default_configmap_name,
    get_default_container_name,
    get_default_deploy_name,
    get_default_pod_name,
)
from phidata.utils.cli_console import print_error
from phidata.utils.log import logger

default_databox_name: str = "databox"


class DataboxArgs(PhidataAppArgs):
    name: str = default_databox_name
    version: str = "1"
    enabled: bool = True

    # Image args
    image_name: str = "phidata/databox"
    image_tag: str = "1"
    # Path to entrypoint script in the image
    entrypoint: Optional[Union[str, List]] = None
    command: Optional[Union[str, List]] = None
    # Add env variables to container env
    # key: var name, value: var value
    env: Optional[Dict[str, str]] = None

    ## Configure python requirements volume
    # Install python dependencies using a requirements.txt file
    install_requirements: bool = False
    requirements_volume_name: str = "databox-requirements-volume"
    # requirements.txt file path in container
    requirements_file_container_path: str = "/requirements.txt"
    # TODO: load requirements_file from git instead of empty dir

    ## Configure the Data volume
    # Creates a data directory on the container
    create_data_volume: bool = False
    data_dir_volume_name: str = "databox-data-volume"
    # Container path to mount the data volume
    data_dir_container_path: str = "/usr/local/data"
    # If True, create the data volume using an empty dir
    use_empty_dir_for_data_volume: bool = True
    # TODO: load storage_dir from s3 instead of empty dir

    ## Configure the Projects volume
    # Create a projects directory on the container
    create_projects_volume: bool = False
    projects_volume_name: str = "databox-projects-volume"
    # Container path to mount the projects volume
    projects_dir_container_path: str = "/usr/local/projects"
    # TODO: load products_dir from git instead of empty dir

    ## Configure Aws credentials
    load_aws_credentials: bool = False

    ## Airflow args
    # Configure the directory containing the airflow dags
    # If use_projects_for_airflow_dags is True
    # set the AIRFLOW__CORE__DAGS_FOLDER to the projects_dir_container_path
    use_projects_for_airflow_dags: bool = True
    # If use_projects_for_airflow_dags is False
    # set the AIRFLOW__CORE__DAGS_FOLDER to the airflow_dags_dir_path
    airflow_dags_dir_path: Optional[str] = None

    # Airflow db args
    wait_for_airflow_db: bool = False
    airflow_db_conn_url: Optional[str] = None
    airflow_db_conn_port: Optional[str] = None
    airflow_db_user: Optional[str] = None
    airflow_db_password: Optional[str] = None
    airflow_schema: Optional[str] = None
    # Airflow db connections.
    # Format expected: dict of { conn_id: conn_url }
    # Converted to env vars: AIRFLOW_CONN__conn_id = conn_url
    db_connections: Optional[Dict] = None

    # Other args
    print_env_on_load: bool = True


class Databox(PhidataApp):
    def __init__(
        self,
        name: str = default_databox_name,
        version: str = "1",
        enabled: bool = True,
        # Image args
        image_name: str = "phidata/databox",
        image_tag: str = "1",
        # Path to entrypoint script in the image
        entrypoint: Optional[Union[str, List]] = None,
        command: Optional[Union[str, List]] = None,
        # Add env variables to container env
        # key: var name, value: var value
        env: Optional[Dict[str, str]] = None,
        ## Configure python requirements volume
        # Install python dependencies using a requirements.txt file
        install_requirements: bool = False,
        requirements_volume_name: str = "databox-requirements-volume",
        # requirements.txt file path in container
        requirements_file_container_path: str = "/requirements.txt",
        ## Configure the Data volume
        # Creates a data directory on the container
        create_data_volume: bool = False,
        data_dir_volume_name: str = "databox-data-volume",
        # Container path to mount the data volume
        data_dir_container_path: str = "/usr/local/data",
        # If True, create the data volume using an empty dir
        use_empty_dir_for_data_volume: bool = True,
        ## Configure the Projects volume
        # Create a projects directory on the container
        create_projects_volume: bool = False,
        projects_volume_name: str = "databox-projects-volume",
        # Container path to mount the projects volume
        projects_dir_container_path: str = "/usr/local/projects",
        ## Configure Aws credentials
        load_aws_credentials: bool = False,
        ## Airflow args
        # Configure the directory containing the airflow dags
        # If use_projects_for_airflow_dags is True
        # set the AIRFLOW__CORE__DAGS_FOLDER to the projects_dir_container_path
        use_projects_for_airflow_dags: bool = True,
        # If use_projects_for_airflow_dags is False
        # set the AIRFLOW__CORE__DAGS_FOLDER to the airflow_dags_dir_path
        airflow_dags_dir_path: Optional[str] = None,
        # Airflow db args
        wait_for_airflow_db: bool = False,
        airflow_db_conn_url: Optional[str] = None,
        airflow_db_conn_port: Optional[str] = None,
        airflow_db_user: Optional[str] = None,
        airflow_db_password: Optional[str] = None,
        airflow_schema: Optional[str] = None,
        # Airflow db connections.
        # Format expected: dict of { conn_id: conn_url }
        # Converted to env vars: AIRFLOW_CONN__conn_id = conn_url
        db_connections: Optional[Dict] = None,
        # Other args
        print_env_on_load: bool = True,
        # Additional args
        # If True, skip resource creation if active resources with the same name exist.
        use_cache: bool = True,
        # If True, log extra debug messages
        use_verbose_logs: bool = False,
    ):

        super().__init__()
        try:
            self.args: DataboxArgs = DataboxArgs(
                name=name,
                version=version,
                enabled=enabled,
                image_name=image_name,
                image_tag=image_tag,
                entrypoint=entrypoint,
                command=command,
                env=env,
                install_requirements=install_requirements,
                requirements_volume_name=requirements_volume_name,
                requirements_file_container_path=requirements_file_container_path,
                create_data_volume=create_data_volume,
                data_dir_volume_name=data_dir_volume_name,
                data_dir_container_path=data_dir_container_path,
                use_empty_dir_for_data_volume=use_empty_dir_for_data_volume,
                create_projects_volume=create_projects_volume,
                projects_volume_name=projects_volume_name,
                projects_dir_container_path=projects_dir_container_path,
                load_aws_credentials=load_aws_credentials,
                use_projects_for_airflow_dags=use_projects_for_airflow_dags,
                airflow_dags_dir_path=airflow_dags_dir_path,
                wait_for_airflow_db=wait_for_airflow_db,
                airflow_db_conn_url=airflow_db_conn_url,
                airflow_db_conn_port=airflow_db_conn_port,
                airflow_db_user=airflow_db_user,
                airflow_db_password=airflow_db_password,
                airflow_schema=airflow_schema,
                db_connections=db_connections,
                print_env_on_load=print_env_on_load,
                use_cache=use_cache,
                use_verbose_logs=use_verbose_logs,
            )
        except Exception as e:
            logger.error(f"Args for {self.__class__.__name__} are not valid")
            raise

    ######################################################
    ## Docker Resources
    ######################################################

    def configure_airflow_on_docker_container(self, container: DockerContainer) -> None:
        """
        Initialize airflow on a docker container
        """

        airflow_env: Dict[str, Any] = {
            "WAIT_FOR_AIRFLOW_DB": str(self.args.wait_for_airflow_db),
            "AIRFLOW_DB_CONN_URL": self.args.airflow_db_conn_url,
            "AIRFLOW_DB_CONN_PORT": self.args.airflow_db_conn_port,
            "AIRFLOW_DB_USER": self.args.airflow_db_user,
            "AIRFLOW_DB_PASSWORD": self.args.airflow_db_password,
            "AIRFLOW_SCHEMA": self.args.airflow_schema,
        }
        # Set the AIRFLOW__CORE__DAGS_FOLDER
        if self.args.create_projects_volume and self.args.use_projects_for_airflow_dags:
            airflow_env[
                "AIRFLOW__CORE__DAGS_FOLDER"
            ] = self.args.projects_dir_container_path
        elif self.args.airflow_dags_dir_path is not None:
            airflow_env["AIRFLOW__CORE__DAGS_FOLDER"] = self.args.airflow_dags_dir_path

        # Set the AIRFLOW__CONN_ variables
        if self.args.db_connections is not None:
            for conn_id, conn_url in self.args.db_connections.items():
                try:
                    af_conn_id = str("AIRFLOW_CONN_{}".format(conn_id)).upper()
                    airflow_env[af_conn_id] = conn_url
                except Exception as e:
                    logger.exception(e)
                    continue
        # Update the container.environment to include airflow_env
        container.environment.update(airflow_env)

    def get_databox_docker_rg(
        self, docker_build_context: DockerBuildContext
    ) -> Optional[DockerResourceGroup]:
        logger.debug(f"Init Databox DockerResourceGroup")

        # Set the Databox Env
        databox_container_env: Dict[str, Any] = {
            # Env variables used by data workflows and data assets
            "PHI_DATA_DIR": self.args.data_dir_container_path,
            "PHI_PROJECTS_DIR": self.args.projects_dir_container_path,
            # Configure python packages to install
            "INSTALL_REQUIREMENTS": str(self.args.install_requirements),
            "REQUIREMENTS_FILE_PATH": self.args.requirements_file_container_path,
            # Print these env variables when the container is loaded
            "PRINT_ENV_ON_LOAD": str(self.args.print_env_on_load),
        }
        # Update the databox env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            databox_container_env.update(self.args.env)

        # Databox Volumes
        # databox_volumes: A dictionary to configure volumes mounted inside the container.
        # The key is either the host path or a volume name,
        # and the value is a dictionary with 2 keys:
        #   bind - The path to mount the volume inside the container
        #   mode - Either rw to mount the volume read/write, or ro to mount it read-only.
        # For example:
        # {
        #   '/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
        #   '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}
        # }
        databox_volumes = {}
        # Create a volume for the requirements file
        # if install_requirements = True
        if self.args.install_requirements:
            # TODO: load requirements_file from git instead of empty dir
            databox_volumes[self.args.requirements_volume_name] = {
                "bind": self.args.requirements_file_container_path,
                "mode": "rw",
            }
        # Create a volume for the data dir
        # if create_data_volume = True
        if self.args.create_data_volume:
            # TODO: load storage_dir from s3 instead of empty dir
            if self.args.use_empty_dir_for_data_volume:
                databox_volumes[self.args.data_dir_volume_name] = {
                    "bind": self.args.data_dir_container_path,
                    "mode": "rw",
                }
        # Create a volume for the projects dir
        # if create_projects_volume = True
        if self.args.create_projects_volume:
            # TODO: load products_dir from git instead of empty dir
            databox_volumes[self.args.projects_volume_name] = {
                "bind": self.args.projects_dir_container_path,
                "mode": "rw",
            }

        # Create the databox container
        databox_docker_container = DockerContainer(
            name=self.args.name,
            image=f"{self.args.image_name}:{self.args.image_tag}",
            command=self.args.command,
            auto_remove=True,
            detach=True,
            entrypoint=self.args.entrypoint,
            environment=databox_container_env,
            remove=True,
            stdin_open=True,
            tty=True,
            network=docker_build_context.network,
            volumes=databox_volumes,
            use_cache=self.args.use_cache,
            use_verbose_logs=self.args.use_verbose_logs,
        )
        # Configure airflow on container
        self.configure_airflow_on_docker_container(databox_docker_container)

        databox_docker_resource_group = DockerResourceGroup(
            name=self.args.name,
            enabled=self.args.enabled,
            network=DockerNetwork(name=docker_build_context.network),
            containers=[databox_docker_container],
        )
        return databox_docker_resource_group

    def init_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> None:
        databox_docker_rg: Optional[DockerResourceGroup] = self.get_databox_docker_rg(
            docker_build_context
        )
        if databox_docker_rg is not None:
            if self.docker_resource_groups is None:
                self.docker_resource_groups = OrderedDict()
            self.docker_resource_groups[databox_docker_rg.name] = databox_docker_rg

    ######################################################
    ## K8s Resources
    ######################################################

    def configure_airflow_on_k8s_container(
        self, container: CreateContainer, k8s_resource_group: CreateK8sResourceGroup
    ) -> None:
        """
        Initialize airflow on a k8s container
        """

        airflow_cm = CreateConfigMap(
            cm_name=get_default_configmap_name("databox-airflow"),
            app_name=self.args.name,
            data={
                "WAIT_FOR_AIRFLOW_DB": str(self.args.wait_for_airflow_db),
                "AIRFLOW_DB_CONN_URL": self.args.airflow_db_conn_url,
                "AIRFLOW_DB_CONN_PORT": self.args.airflow_db_conn_port,
                "AIRFLOW_DB_USER": self.args.airflow_db_user,
                "AIRFLOW_DB_PASSWORD": self.args.airflow_db_password,
                "AIRFLOW_SCHEMA": self.args.airflow_schema,
            },
        )

        # Set the AIRFLOW__CORE__DAGS_FOLDER
        if self.args.create_projects_volume and self.args.use_projects_for_airflow_dags:
            airflow_cm.data[
                "AIRFLOW__CORE__DAGS_FOLDER"
            ] = self.args.projects_dir_container_path
        elif self.args.airflow_dags_dir_path is not None:
            airflow_cm.data[
                "AIRFLOW__CORE__DAGS_FOLDER"
            ] = self.args.airflow_dags_dir_path

        # Set the AIRFLOW__CONN_ variables
        if self.args.db_connections is not None:
            for conn_id, conn_url in self.args.db_connections.items():
                try:
                    af_conn_id = str("AIRFLOW_CONN_{}".format(conn_id)).upper()
                    airflow_cm.data[af_conn_id] = conn_url
                except Exception as e:
                    logger.exception(e)
                    continue

        # Add airflow_cm to the container env
        if container.envs_from_configmap is None:
            container.envs_from_configmap = []
        container.envs_from_configmap.append(airflow_cm.cm_name)

        # Add airflow_cm to k8s_resource_group
        if k8s_resource_group.config_maps is None:
            k8s_resource_group.config_maps = []
        k8s_resource_group.config_maps.append(airflow_cm)

    def get_databox_k8s_rg(
        self, k8s_build_context: K8sBuildContext
    ) -> Optional[K8sResourceGroup]:
        logger.debug(f"Init Databox K8sResourceGroup")

        # Set the Databox Env
        # Databox Config-Map is a dict of environment variables which are not secrets.
        # The keys of this configmap will become env variables in the databox container
        databox_cm = CreateConfigMap(
            cm_name=get_default_configmap_name(self.args.name),
            app_name=self.args.name,
            data={
                # Env variables used by data workflows and data assets
                "PHI_DATA_DIR": self.args.data_dir_container_path,
                "PHI_PROJECTS_DIR": self.args.projects_dir_container_path,
                # Configure python packages to install
                "INSTALL_REQUIREMENTS": str(self.args.install_requirements),
                "REQUIREMENTS_FILE_PATH": self.args.requirements_file_container_path,
                # Print these env variables when the container is loaded
                "PRINT_ENV_ON_LOAD": str(self.args.print_env_on_load),
            },
        )
        # Update the databox env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            databox_cm.data.update(self.args.env)

        # Databox Volumes
        databox_volumes = []
        # Create a volume for the requirements file
        # if install_requirements = True
        if self.args.install_requirements:
            requirements_volume = CreateVolume(
                volume_name=self.args.requirements_volume_name,
                app_name=self.args.name,
                mount_path=self.args.requirements_file_container_path,
                volume_type=VolumeType.EMPTY_DIR,
                empty_dir=EmptyDirVolumeSource(),
            )
            databox_volumes.append(requirements_volume)
        # Create a volume for the data dir
        # if create_data_volume = True
        if self.args.create_data_volume:
            if self.args.use_empty_dir_for_data_volume:
                data_volume = CreateVolume(
                    volume_name=self.args.data_dir_volume_name,
                    app_name=self.args.name,
                    mount_path=self.args.data_dir_container_path,
                    volume_type=VolumeType.EMPTY_DIR,
                    empty_dir=EmptyDirVolumeSource(),
                )
                databox_volumes.append(data_volume)
        # Create a volume for the projects dir
        # if create_projects_volume = True
        if self.args.create_projects_volume:
            projects_volume = CreateVolume(
                volume_name=self.args.projects_volume_name,
                app_name=self.args.name,
                mount_path=self.args.projects_dir_container_path,
                volume_type=VolumeType.EMPTY_DIR,
                empty_dir=EmptyDirVolumeSource(),
            )
            databox_volumes.append(projects_volume)

        # Create the databox container
        databox_k8s_container = CreateContainer(
            container_name=get_default_container_name(self.args.name),
            app_name=self.args.name,
            image_name=self.args.image_name,
            image_tag=self.args.image_tag,
            # Equivalent to docker images CMD
            args=self.args.command,
            # Equivalent to docker images ENTRYPOINT
            command=self.args.entrypoint,
            envs_from_configmap=[databox_cm.cm_name],
            volumes=databox_volumes,
        )
        databox_deployment = CreateDeployment(
            deploy_name=get_default_deploy_name(self.args.name),
            pod_name=get_default_pod_name(self.args.name),
            app_name=self.args.name,
            namespace=k8s_build_context.namespace,
            service_account_name=k8s_build_context.service_account_name,
            containers=[databox_k8s_container],
            volumes=databox_volumes,
            labels=k8s_build_context.labels,
        )
        databox_k8s_resource_group = CreateK8sResourceGroup(
            name=self.args.name,
            enabled=self.args.enabled,
            config_maps=[databox_cm],
            deployments=[databox_deployment],
        )
        # Configure airflow on container
        self.configure_airflow_on_k8s_container(
            databox_k8s_container, databox_k8s_resource_group
        )
        return databox_k8s_resource_group.create()

    def init_k8s_resource_groups(self, k8s_build_context: K8sBuildContext) -> None:
        databox_k8s_rg: Optional[K8sResourceGroup] = self.get_databox_k8s_rg(
            k8s_build_context
        )
        # logger.debug("databox_k8s_rg: {}".format(databox_k8s_rg))
        if databox_k8s_rg is not None:
            if self.k8s_resource_groups is None:
                self.k8s_resource_groups = OrderedDict()
            self.k8s_resource_groups[databox_k8s_rg.name] = databox_k8s_rg
