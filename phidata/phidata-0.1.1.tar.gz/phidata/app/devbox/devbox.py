from collections import OrderedDict
from pathlib import Path
from typing import Optional, Dict, Any, List, Union

from pydantic import BaseModel

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
    HostPathVolumeSource,
    VolumeType,
)
from phidata.infra.k8s.create.common.port import CreatePort
from phidata.infra.k8s.create.group import CreateK8sResourceGroup
from phidata.infra.k8s.resource.group import (
    K8sResourceGroup,
    K8sBuildContext,
)
from phidata.utils.common import get_default_configmap_name
from phidata.utils.cli_console import print_error, print_info
from phidata.utils.log import logger

default_devbox_name: str = "devbox"


class DevboxDevModeArgs(BaseModel):
    install_phidata_dev: bool = True
    phidata_volume_name: str = "devbox-phidata-volume"
    phidata_dir_path: Path = Path.home().joinpath("p", "philab", "phidata")
    phidata_dir_container_path: str = "/phidata"


class DevboxArgs(PhidataAppArgs):
    name: str = default_devbox_name
    version: str = "1"
    enabled: bool = True

    # Image args
    image_name: str = "phidata/devbox"
    image_tag: str = "1"
    # Path to entrypoint script for the image
    entrypoint: Optional[Union[str, List]] = None
    command: Optional[Union[str, List]] = None
    # Add env variables to container env
    # key: var name, value: var value
    env: Optional[Dict[str, str]] = None

    # Mount the workspace directory on the container
    mount_workspace: bool = True
    workspace_volume_name: str = "devbox-workspace-volume"
    # Path to mount the workspace volume under
    # This is the parent directory for the workspace on the container
    # i.e. the ws is mounted as a subdir in this dir
    # eg: if ws name is: idata, workspace path would be: /usr/local/devbox/idata
    workspace_parent_container_path: str = "/usr/local/devbox"

    # Install python dependencies using a requirements.txt file
    install_requirements: bool = True
    # Path to the requirements.txt file relative to the workspace root
    requirements_file_path: str = "requirements/dev-requirements.txt"

    # Mount Aws config on the container
    mount_aws_config: bool = False
    # Aws config dir on the host
    aws_config_path: Path = Path.home().resolve().joinpath(".aws")
    # Aws config dir on the container
    aws_config_container_path: str = "/usr/local/devbox/.aws"

    # Airflow args
    # If init_airflow = True, this devbox initializes airflow
    init_airflow: bool = True
    # If use_products_as_airflow_dags = True
    # set the AIRFLOW__CORE__DAGS_FOLDER to the products_dir
    use_products_as_airflow_dags: bool = True
    # If use_products_as_airflow_dags = False
    # set the AIRFLOW__CORE__DAGS_FOLDER to the airflow_dags_path
    # airflow_dags_path is the directory in the container containing the airflow dags
    airflow_dags_path: Optional[str] = None
    # Creates an airflow user with username: test, pass: test
    create_airflow_test_user: bool = False

    # Airflow db args
    # If True, initialize the airflow_db on this devbox
    # If None, value is derived from init_airflow i.e. initialize the airflow_db if init_airflow = True
    #   Locally, airflow_db uses sqllite
    # If using the devbox with an external Airflow db, set init_airflow_db = False
    init_airflow_db: Optional[bool] = None
    wait_for_airflow_db: bool = False
    airflow_db_conn_url: Optional[str] = "airflow-pg"
    airflow_db_conn_port: Optional[str] = "5432"
    airflow_db_user: Optional[str] = "airflow"
    airflow_db_password: Optional[str] = "airflow"
    airflow_schema: Optional[str] = "airflow"
    # Airflow db connections in the format { conn_id: conn_url }
    # converted to env var: AIRFLOW_CONN__conn_id = conn_url
    db_connections: Optional[Dict] = None

    # Airflow scheduler args
    # Init Airflow scheduler as a deamon process
    init_airflow_scheduler: bool = False

    # Airflow webserver args
    # Init Airflow webserver when the container starts
    init_airflow_webserver: bool = False
    # webserver port on the container
    airflow_webserver_container_port: int = 8080
    # webserver port on the host machine
    airflow_webserver_host_port: int = 8080
    # K8s args
    # webserver port name
    airflow_webserver_port_name: str = "http"

    # Other airflow args
    load_examples: bool = False
    # Create a soft link from airflow_dir to airflow_home
    # Useful when debugging the airflow conf
    link_airflow_home: bool = False
    # Path to the airflow dir relative to the workspace root
    airflow_dir: str = "airflow"
    # Path to airflow home
    airflow_home: str = "/usr/local/airflow"

    # Other args
    print_env_on_load: bool = True
    dev_mode: Optional[DevboxDevModeArgs] = None


class Devbox(PhidataApp):
    def __init__(
        self,
        name: str = default_devbox_name,
        version: str = "1",
        enabled: bool = True,
        # Image args,
        image_name: str = "phidata/devbox",
        image_tag: str = "1",
        # Path to entrypoint script for the image,
        entrypoint: Optional[Union[str, List]] = None,
        command: Optional[Union[str, List]] = None,
        # Add env variables to container env,
        # key: var name, value: var value,
        env: Optional[Dict[str, str]] = None,
        # Mount the workspace directory on the container,
        mount_workspace: bool = True,
        workspace_volume_name: str = "devbox-workspace-volume",
        # Path to mount the workspace volume under,
        # This is the parent directory for the workspace on the container,
        # i.e. the ws is mounted as a subdir in this dir,
        # eg: if ws name is: idata, workspace path would be: /usr/local/devbox/idata,
        workspace_parent_container_path: str = "/usr/local/devbox",
        # Install python dependencies using a requirements.txt file,
        install_requirements: bool = True,
        # Path to the requirements.txt file relative to the workspace root,
        requirements_file_path: str = "requirements/dev-requirements.txt",
        # Mount Aws config on the container,
        mount_aws_config: bool = False,
        # Aws config dir on the host,
        aws_config_path: Path = Path.home().resolve().joinpath(".aws"),
        # Aws config dir on the container,
        aws_config_container_path: str = "/usr/local/devbox/.aws",
        # Airflow args,
        # If init_airflow = True, this devbox initializes airflow,
        init_airflow: bool = True,
        # If use_products_as_airflow_dags = True,
        # set the AIRFLOW__CORE__DAGS_FOLDER to the products_dir,
        use_products_as_airflow_dags: bool = True,
        # If use_products_as_airflow_dags = False,
        # set the AIRFLOW__CORE__DAGS_FOLDER to the airflow_dags_path,
        # airflow_dags_path is the directory in the container containing the airflow dags,
        airflow_dags_path: Optional[str] = None,
        # Creates an airflow user with username: test, pass: test,
        create_airflow_test_user: bool = False,
        # Airflow db args,
        # If True, initialize the airflow_db on this devbox,
        # If None, value is derived from init_airflow i.e. initialize the airflow_db if init_airflow = True,
        #   Locally, airflow_db uses sqllite,
        # If using the devbox with an external Airflow db, set init_airflow_db = False,
        init_airflow_db: Optional[bool] = None,
        wait_for_airflow_db: bool = False,
        airflow_db_conn_url: Optional[str] = "airflow-pg",
        airflow_db_conn_port: Optional[str] = "5432",
        airflow_db_user: Optional[str] = "airflow",
        airflow_db_password: Optional[str] = "airflow",
        airflow_schema: Optional[str] = "airflow",
        # Airflow db connections in the format { conn_id: conn_url },
        # converted to env var: AIRFLOW_CONN__conn_id = conn_url,
        db_connections: Optional[Dict] = None,
        # Airflow scheduler args,
        # Init Airflow scheduler as a deamon process,
        init_airflow_scheduler: bool = False,
        # Airflow webserver args,
        # Init Airflow webserver when the container starts,
        init_airflow_webserver: bool = False,
        # webserver port on the container,
        airflow_webserver_container_port: int = 8080,
        # webserver port on the host machine,
        airflow_webserver_host_port: int = 8080,
        # K8s args,
        # webserver port name,
        airflow_webserver_port_name: str = "http",
        # Other airflow args,
        load_examples: bool = False,
        # Create a soft link from airflow_dir to airflow_home,
        # Useful when debugging the airflow conf,
        link_airflow_home: bool = False,
        # Path to the airflow dir relative to the workspace root,
        airflow_dir: str = "airflow",
        # Path to airflow home,
        airflow_home: str = "/usr/local/airflow",
        # Other args,
        print_env_on_load: bool = True,
        dev_mode: Optional[DevboxDevModeArgs] = None,
        # If True, skip resource creation if active resources with the same name exist.
        use_cache: bool = True,
        # If True, log extra debug messages
        use_verbose_logs: bool = False,
    ):

        super().__init__()
        try:
            self.args: DevboxArgs = DevboxArgs(
                name=name,
                version=version,
                enabled=enabled,
                image_name=image_name,
                image_tag=image_tag,
                entrypoint=entrypoint,
                command=command,
                env=env,
                mount_workspace=mount_workspace,
                workspace_volume_name=workspace_volume_name,
                workspace_parent_container_path=workspace_parent_container_path,
                install_requirements=install_requirements,
                requirements_file_path=requirements_file_path,
                mount_aws_config=mount_aws_config,
                aws_config_path=aws_config_path,
                aws_config_container_path=aws_config_container_path,
                init_airflow=init_airflow,
                use_products_as_airflow_dags=use_products_as_airflow_dags,
                airflow_dags_path=airflow_dags_path,
                create_airflow_test_user=create_airflow_test_user,
                init_airflow_db=init_airflow_db,
                wait_for_airflow_db=wait_for_airflow_db,
                airflow_db_conn_url=airflow_db_conn_url,
                airflow_db_conn_port=airflow_db_conn_port,
                airflow_db_user=airflow_db_user,
                airflow_db_password=airflow_db_password,
                airflow_schema=airflow_schema,
                db_connections=db_connections,
                init_airflow_scheduler=init_airflow_scheduler,
                init_airflow_webserver=init_airflow_webserver,
                airflow_webserver_container_port=airflow_webserver_container_port,
                airflow_webserver_host_port=airflow_webserver_host_port,
                airflow_webserver_port_name=airflow_webserver_port_name,
                load_examples=load_examples,
                link_airflow_home=link_airflow_home,
                airflow_dir=airflow_dir,
                airflow_home=airflow_home,
                print_env_on_load=print_env_on_load,
                dev_mode=dev_mode,
                use_cache=use_cache,
                use_verbose_logs=use_verbose_logs,
            )
        except Exception as e:
            logger.error(f"Args for {self.__class__.__name__} are not valid")
            raise

    ######################################################
    ## Docker Resources
    ######################################################

    def init_airflow_on_docker_container(self, container: DockerContainer) -> None:
        """
        Initialize airflow on a docker container
        """

        if not self.args.init_airflow:
            return

        # Update init_airflow_db arg if None
        if self.args.init_airflow_db is None:
            self.args.init_airflow_db = True

        # Workspace paths
        workspace_name = self.workspace_root_path.stem
        workspace_root_container_path = Path(
            self.args.workspace_parent_container_path
        ).joinpath(workspace_name)
        products_dir_container_path = workspace_root_container_path.joinpath(
            self.products_dir
        )
        airflow_dir_container_path = workspace_root_container_path.joinpath(
            self.args.airflow_dir
        )

        airflow_env: Dict[str, Any] = {
            "INIT_AIRFLOW": str(self.args.init_airflow),
            "INIT_AIRFLOW_DB": str(self.args.init_airflow_db),
            "WAIT_FOR_AIRFLOW_DB": str(self.args.wait_for_airflow_db),
            "AIRFLOW_DB_CONN_URL": self.args.airflow_db_conn_url,
            "AIRFLOW_DB_CONN_PORT": self.args.airflow_db_conn_port,
            "AIRFLOW_DB_USER": self.args.airflow_db_user,
            "AIRFLOW_DB_PASSWORD": self.args.airflow_db_password,
            "AIRFLOW_SCHEMA": self.args.airflow_schema,
            "INIT_AIRFLOW_SCHEDULER": str(self.args.init_airflow_scheduler),
            "INIT_AIRFLOW_WEBSERVER": str(self.args.init_airflow_webserver),
            "AIRFLOW__CORE__LOAD_EXAMPLES": str(self.args.load_examples),
            "LINK_AIRFLOW_HOME": str(self.args.link_airflow_home),
            "AIRFLOW_DIR": str(airflow_dir_container_path),
            "AIRFLOW_HOME": self.args.airflow_home,
            "CREATE_AIRFLOW_TEST_USER": str(self.args.create_airflow_test_user),
        }
        # Set the AIRFLOW__CORE__DAGS_FOLDER
        if self.args.mount_workspace and self.args.use_products_as_airflow_dags:
            airflow_env["AIRFLOW__CORE__DAGS_FOLDER"] = str(products_dir_container_path)
        elif self.args.airflow_dags_path is not None:
            airflow_env["AIRFLOW__CORE__DAGS_FOLDER"] = self.args.airflow_dags_path

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

        # Open the airflow webserver port if init_airflow_webserver = True
        if self.args.init_airflow_webserver:
            ws_port: Dict[str, Any] = {
                str(
                    self.args.airflow_webserver_container_port
                ): self.args.airflow_webserver_host_port,
            }
            if container.ports is None:
                container.ports = {}
            container.ports.update(ws_port)

    def get_devbox_docker_rg(
        self, docker_build_context: DockerBuildContext
    ) -> Optional[DockerResourceGroup]:
        logger.debug(f"Init Devbox DockerResourceGroup")

        # Workspace paths
        workspace_name = self.workspace_root_path.stem
        workspace_root_container_path = Path(
            self.args.workspace_parent_container_path
        ).joinpath(workspace_name)
        requirements_file_container_path = workspace_root_container_path.joinpath(
            self.args.requirements_file_path
        )

        scripts_dir_container_path = workspace_root_container_path.joinpath(
            self.scripts_dir
        )
        storage_dir_container_path = workspace_root_container_path.joinpath(
            self.storage_dir
        )
        meta_dir_container_path = workspace_root_container_path.joinpath(self.meta_dir)
        products_dir_container_path = workspace_root_container_path.joinpath(
            self.products_dir
        )
        notebooks_dir_container_path = workspace_root_container_path.joinpath(
            self.notebooks_dir
        )
        workspace_config_dir_container_path = workspace_root_container_path.joinpath(
            self.workspace_config_dir
        )

        # Set the Devbox Env
        devbox_container_env: Dict[str, Any] = {
            # Env variables used by data workflows and data assets
            "PHI_WORKSPACE_PARENT": str(self.args.workspace_parent_container_path),
            "PHI_WORKSPACE_ROOT": str(workspace_root_container_path),
            "PHI_SCRIPTS_DIR": str(scripts_dir_container_path),
            "PHI_STORAGE_DIR": str(storage_dir_container_path),
            "PHI_META_DIR": str(meta_dir_container_path),
            "PHI_PRODUCTS_DIR": str(products_dir_container_path),
            "PHI_NOTEBOOKS_DIR": str(notebooks_dir_container_path),
            "PHI_WORKSPACE_CONFIG_DIR": str(workspace_config_dir_container_path),
            "INSTALL_REQUIREMENTS": str(self.args.install_requirements),
            "REQUIREMENTS_FILE_PATH": str(requirements_file_container_path),
            # Print these env variables when the container is loaded
            "PRINT_ENV_ON_LOAD": str(self.args.print_env_on_load),
            # Dev mode args
            "INSTALL_PHIDATA_DEV": str(self.args.dev_mode.install_phidata_dev)
            if self.args.dev_mode is not None
            else str(False),
            "PHIDATA_DIR_PATH": self.args.dev_mode.phidata_dir_container_path
            if self.args.dev_mode is not None
            else str(False),
        }
        # Update the devbox env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            devbox_container_env.update(self.args.env)

        # Devbox Volumes
        # devbox_volumes: A dictionary to configure volumes mounted inside the container.
        # The key is either the host path or a volume name,
        # and the value is a dictionary with 2 keys:
        #   bind - The path to mount the volume inside the container
        #   mode - Either rw to mount the volume read/write, or ro to mount it read-only.
        # For example:
        # {
        #   '/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
        #   '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}
        # }
        devbox_volumes = {}
        # Create a volume for the workspace dir
        if self.args.mount_workspace:
            workspace_root_path_str = str(self.workspace_root_path)
            workspace_root_container_path_str = str(workspace_root_container_path)
            logger.debug(f"Mounting: {workspace_root_path_str}")
            logger.debug(f"\tto: {workspace_root_container_path_str}")
            devbox_volumes[workspace_root_path_str] = {
                "bind": workspace_root_container_path_str,
                "mode": "rw",
            }
        # Create a volume for Aws credentials
        if self.args.mount_aws_config:
            aws_config_path_str = str(self.args.aws_config_path)
            logger.debug(f"Mounting: {aws_config_path_str}")
            logger.debug(f"\tto: {self.args.aws_config_container_path}")
            devbox_volumes[aws_config_path_str] = {
                "bind": self.args.aws_config_container_path,
                "mode": "ro",
            }
            devbox_container_env[
                "AWS_CONFIG_FILE"
            ] = f"{self.args.aws_config_container_path}/config"
            devbox_container_env[
                "AWS_SHARED_CREDENTIALS_FILE"
            ] = f"{self.args.aws_config_container_path}/credentials"
        # Create a volume for Phidata dev mode
        # if dev_mode is enabled
        if self.args.dev_mode is not None:
            # mount the phidata directory if install_phidata_dev = True
            if (
                self.args.dev_mode.install_phidata_dev
                and self.args.dev_mode.phidata_dir_path is not None
            ):
                phidata_dir_absolute_path_str = str(self.args.dev_mode.phidata_dir_path)
                logger.debug(f"Mounting: {phidata_dir_absolute_path_str}")
                logger.debug(f"\tto: {self.args.dev_mode.phidata_dir_container_path}")
                devbox_volumes[phidata_dir_absolute_path_str] = {
                    "bind": self.args.dev_mode.phidata_dir_container_path,
                    "mode": "rw",
                }

        # Create the devbox container
        devbox_docker_container = DockerContainer(
            name=self.args.name,
            image=f"{self.args.image_name}:{self.args.image_tag}",
            command=self.args.command,
            auto_remove=True,
            detach=True,
            entrypoint=self.args.entrypoint,
            environment=devbox_container_env,
            remove=True,
            stdin_open=True,
            tty=True,
            network=docker_build_context.network,
            volumes=devbox_volumes,
            use_cache=self.args.use_cache,
            use_verbose_logs=self.args.use_verbose_logs,
        )
        # Initialize airflow on container
        self.init_airflow_on_docker_container(devbox_docker_container)
        # logger.debug(f"Devbox Container Env: {devbox_docker_container.environment}")

        devbox_docker_resource_group = DockerResourceGroup(
            name=self.args.name,
            enabled=self.args.enabled,
            network=DockerNetwork(name=docker_build_context.network),
            containers=[devbox_docker_container],
        )
        return devbox_docker_resource_group

    def init_docker_resource_groups(
        self, docker_build_context: DockerBuildContext
    ) -> None:
        devbox_docker_rg: Optional[DockerResourceGroup] = self.get_devbox_docker_rg(
            docker_build_context
        )
        if devbox_docker_rg is not None:
            if self.docker_resource_groups is None:
                self.docker_resource_groups = OrderedDict()
            self.docker_resource_groups[devbox_docker_rg.name] = devbox_docker_rg

    ######################################################
    ## K8s Resources
    ######################################################

    def init_airflow_on_k8s_container(
        self, container: CreateContainer, k8s_resource_group: CreateK8sResourceGroup
    ) -> None:
        """
        Initialize airflow on a k8s container
        """

        if not self.args.init_airflow:
            return

        # Update init_airflow_db arg if None
        if self.args.init_airflow_db is None:
            self.args.init_airflow_db = True

        airflow_cm = CreateConfigMap(
            cm_name=get_default_configmap_name("devbox-airflow"),
            app_name=self.args.name,
            data={
                "INIT_AIRFLOW": str(self.args.init_airflow),
                "INIT_AIRFLOW_DB": str(self.args.init_airflow_db),
                "WAIT_FOR_AIRFLOW_DB": str(self.args.wait_for_airflow_db),
                "AIRFLOW_DB_CONN_URL": self.args.airflow_db_conn_url,
                "AIRFLOW_DB_CONN_PORT": self.args.airflow_db_conn_port,
                "AIRFLOW_DB_USER": self.args.airflow_db_user,
                "AIRFLOW_DB_PASSWORD": self.args.airflow_db_password,
                "AIRFLOW_SCHEMA": self.args.airflow_schema,
                "INIT_AIRFLOW_SCHEDULER": str(self.args.init_airflow_scheduler),
                "INIT_AIRFLOW_WEBSERVER": str(self.args.init_airflow_webserver),
                "CREATE_AIRFLOW_TEST_USER": str(self.args.init_airflow_webserver),
                "AIRFLOW__CORE__LOAD_EXAMPLES": str(self.args.load_examples),
            },
        )

        # Add airflow_cm to container env and
        if container.envs_from_configmap is None:
            container.envs_from_configmap = []
        container.envs_from_configmap.append(airflow_cm.cm_name)
        if k8s_resource_group.config_maps is None:
            k8s_resource_group.config_maps = []
        k8s_resource_group.config_maps.append(airflow_cm)

        # Set the AIRFLOW__CORE__DAGS_FOLDER
        if self.args.mount_workspace and self.args.use_products_as_airflow_dags:
            projects_dir_container_path = Path(
                self.args.workspace_parent_container_path
            ).joinpath(self.args.workspace_dir_path.stem, self.args.projects_dir)
            airflow_cm.data["AIRFLOW__CORE__DAGS_FOLDER"] = projects_dir_container_path
        elif self.args.airflow_dags_path is not None:
            airflow_cm.data["AIRFLOW__CORE__DAGS_FOLDER"] = self.args.airflow_dags_path
        if self.args.db_connections is not None:
            for conn_id, conn_url in self.args.db_connections.items():
                try:
                    af_conn_id = str("AIRFLOW_CONN_{}".format(conn_id)).upper()
                    airflow_cm.data[af_conn_id] = conn_url
                except Exception as e:
                    logger.exception(e)
                    continue
        # Open the airflow webserver port if init_airflow_webserver = True
        if self.args.init_airflow_webserver:
            ws_port = CreatePort(
                name=self.args.airflow_webserver_port_name,
                container_port=self.args.airflow_webserver_container_port,
            )
            if container.ports is None:
                container.ports = []
            container.ports.append(ws_port)

    def get_devbox_k8s_rg(
        self, k8s_build_context: K8sBuildContext
    ) -> Optional[K8sResourceGroup]:
        logger.debug(f"Init Devbox K8sResourceGroup")

        # Set the Devbox Env
        # Devbox Config-Map is a dict of environment variables which are not secrets.
        # The keys of this configmap will become env variables in the devbox container
        workspace_dir_container_path = Path(
            self.args.workspace_parent_container_path
        ).joinpath(self.args.workspace_dir_path.stem)
        projects_dir_container_path = workspace_dir_container_path.joinpath(
            self.args.projects_dir
        )
        devbox_cm = CreateConfigMap(
            cm_name=get_default_configmap_name(self.args.name),
            app_name=self.args.name,
            data={
                # Env variables used by data workflows and data assets
                "PHI_DATA_DIR": self.args.data_dir_container_path,
                "PHI_PROJECTS_DIR": str(projects_dir_container_path),
                "PHI_WORKSPACE_DIR": str(workspace_dir_container_path),
                "PHI_WORKSPACE_PARENT": str(self.args.workspace_parent_container_path),
                # Configure python packages to install
                "INSTALL_REQUIREMENTS": str(self.args.install_requirements),
                "REQUIREMENTS_FILE_PATH": self.args.requirements_file_container_path,
                # Print these env variables when the container is loaded
                "PRINT_ENV_ON_LOAD": str(self.args.print_env_on_load),
                # Dev mode args
                "INSTALL_PHIDATA_DEV": str(self.args.dev_mode.install_phidata_dev)
                if self.args.dev_mode is not None
                else str(False),
                "PHIDATA_DIR_PATH": self.args.dev_mode.phidata_dir_container_path
                if self.args.dev_mode is not None
                else str(False),
            },
        )
        # Update the devbox env with user provided env
        if self.args.env is not None and isinstance(self.args.env, dict):
            devbox_cm.data.update(self.args.env)

        # Devbox Volumes
        devbox_volumes = []
        # Create a volume for the requirements file
        # if install_requirements = True
        if self.args.install_requirements:
            requirements_file_absolute_path = str(
                self.args.workspace_dir_path.joinpath(self.args.requirements_file_path)
            )
            logger.debug(f"Mounting: {requirements_file_absolute_path}")
            logger.debug(f"\tto: {self.args.requirements_file_container_path}")
            requirements_volume = CreateVolume(
                volume_name=self.args.requirements_volume_name,
                app_name=self.args.name,
                mount_path=self.args.requirements_file_container_path,
                volume_type=VolumeType.HOST_PATH,
                host_path=HostPathVolumeSource(path=requirements_file_absolute_path),
            )
            devbox_volumes.append(requirements_volume)
        # Create a volume for the data dir
        # if create_data_volume = True
        if self.args.create_data_volume:
            if (
                self.args.use_host_path_for_data_volume
                and self.args.data_dir_path is not None
            ):
                data_dir_absolute_path = str(
                    self.args.workspace_dir_path.joinpath(self.args.data_dir_path)
                )
                logger.debug(f"Mounting: {data_dir_absolute_path}")
                logger.debug(f"\tto: {self.args.data_dir_container_path}")
                data_volume = CreateVolume(
                    volume_name=self.args.data_dir_volume_name,
                    app_name=self.args.name,
                    mount_path=self.args.data_dir_container_path,
                    volume_type=VolumeType.HOST_PATH,
                    host_path=HostPathVolumeSource(
                        path=data_dir_absolute_path,
                    ),
                )
                devbox_volumes.append(data_volume)
            elif self.args.use_empty_dir_for_data_volume:
                logger.debug(f"Mounting EmptyDir")
                logger.debug(f"\tto: {self.args.data_dir_container_path}")
                data_volume = CreateVolume(
                    volume_name=self.args.data_dir_volume_name,
                    app_name=self.args.name,
                    mount_path=self.args.data_dir_container_path,
                    volume_type=VolumeType.EMPTY_DIR,
                    empty_dir=EmptyDirVolumeSource(),
                )
                devbox_volumes.append(data_volume)
        # Create a volume for the projects dir
        # if mount_workspace = True
        if self.args.mount_workspace:
            if self.args.use_host_path_for_workspace:
                ws_dir_container_path_str = str(
                    Path(self.args.workspace_parent_container_path).joinpath(
                        self.args.workspace_dir_path.stem
                    )
                )
                ws_dir_path_str = str(self.args.workspace_dir_path)
                logger.debug(f"Mounting: {ws_dir_path_str}")
                logger.debug(f"\tto: {ws_dir_container_path_str}")
                workspace_volume = CreateVolume(
                    volume_name=self.args.workspace_volume_name,
                    app_name=self.args.name,
                    mount_path=ws_dir_container_path_str,
                    volume_type=VolumeType.HOST_PATH,
                    host_path=HostPathVolumeSource(
                        path=ws_dir_path_str,
                    ),
                )
                devbox_volumes.append(workspace_volume)
        # Airflow conf file
        if self.args.mount_airflow_dir:
            airflow_dir_file_absolute_path = str(
                self.args.workspace_dir_path.joinpath(self.args.airflow_dir_path)
            )
            logger.debug(f"Mounting: {airflow_dir_file_absolute_path}")
            logger.debug(f"\tto: {self.args.airflow_dir_container_path}")
            airflow_dir_volume = CreateVolume(
                volume_name=self.args.airflow_volume_name,
                app_name=self.args.name,
                mount_path=self.args.airflow_dir_container_path,
                volume_type=VolumeType.HOST_PATH,
                host_path=HostPathVolumeSource(path=airflow_dir_file_absolute_path),
            )
            devbox_volumes.append(airflow_dir_volume)
        # Create a volume for Phidata dev mode
        # if dev_mode is enabled
        if self.args.dev_mode is not None:
            # mount the phidata directory if install_phidata_dev = True
            if (
                self.args.dev_mode.install_phidata_dev
                and self.args.dev_mode.phidata_dir_path is not None
            ):
                phidata_dir_absolute_path = str(self.args.dev_mode.phidata_dir_path)
                logger.debug(f"Mounting: {phidata_dir_absolute_path}")
                logger.debug(f"\tto: {self.args.dev_mode.phidata_dir_container_path}")
                phidata_volume = CreateVolume(
                    volume_name=self.args.dev_mode.phidata_volume_name,
                    app_name=self.args.name,
                    mount_path=self.args.dev_mode.phidata_dir_container_path,
                    volume_type=VolumeType.HOST_PATH,
                    host_path=HostPathVolumeSource(
                        path=phidata_dir_absolute_path,
                    ),
                )
                devbox_volumes.append(phidata_volume)

        # Create the devbox container
        devbox_k8s_container = CreateContainer(
            container_name=f"{self.args.name}-container",
            app_name=self.args.name,
            image_name=self.args.image_name,
            image_tag=self.args.image_tag,
            # Equivalent to docker images CMD
            args=self.args.command,
            # Equivalent to docker images ENTRYPOINT
            command=self.args.entrypoint,
            envs_from_configmap=[devbox_cm.cm_name],
            volumes=devbox_volumes,
        )
        devbox_deployment = CreateDeployment(
            deploy_name=f"{self.args.name}-deploy",
            pod_name=f"{self.args.name}-pod",
            app_name=self.args.name,
            namespace=k8s_build_context.namespace,
            service_account_name=k8s_build_context.service_account_name,
            containers=[devbox_k8s_container],
            volumes=devbox_volumes,
            labels=k8s_build_context.labels,
        )
        devbox_k8s_resource_group = CreateK8sResourceGroup(
            name=self.args.name,
            enabled=self.args.enabled,
            config_maps=[devbox_cm],
            deployments=[devbox_deployment],
        )
        # Initialize airflow on container
        self.init_airflow_on_k8s_container(
            devbox_k8s_container, devbox_k8s_resource_group
        )
        return devbox_k8s_resource_group.create()

    def init_k8s_resource_groups(self, k8s_build_context: K8sBuildContext) -> None:
        devbox_k8s_rg: Optional[K8sResourceGroup] = self.get_devbox_k8s_rg(
            k8s_build_context
        )
        # logger.debug("devbox_k8s_rg: {}".format(devbox_k8s_rg))
        if devbox_k8s_rg is not None:
            if self.k8s_resource_groups is None:
                self.k8s_resource_groups = OrderedDict()
            self.k8s_resource_groups[devbox_k8s_rg.name] = devbox_k8s_rg
