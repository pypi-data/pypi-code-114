from time import sleep
from typing import Optional, Any, Dict, Union, List

from docker.models.containers import Container
from docker.errors import NotFound, ImageNotFound, APIError

from phidata.infra.docker.api_client import DockerApiClient
from phidata.infra.docker.resource.base import DockerResource
from phidata.infra.docker.exceptions import DockerResourceCreationFailedException
from phidata.utils.cli_console import print_info
from phidata.utils.log import logger


class DockerContainerMount(DockerResource):
    resource_type: str = "ContainerMount"

    target: str
    source: str
    type: str = "volume"
    read_only: bool = False
    labels: Optional[Dict[str, Any]] = None


class DockerContainer(DockerResource):
    resource_type: str = "Container"

    # image (str) – The image to run.
    image: Optional[str] = None
    # command (str or list) – The command to run in the container.
    command: Optional[Union[str, List]] = None
    # auto_remove (bool) – enable auto-removal of the container on daemon side when the container’s process exits.
    auto_remove: bool = True
    # detach (bool) – Run container in the background and return a Container object.
    detach: bool = True
    # entrypoint (str or list) – The entrypoint for the container.
    entrypoint: Optional[Union[str, List]] = None
    # environment (dict or list) – Environment variables to set inside the container
    environment: Optional[Union[Dict[str, Any], List]] = None
    # group_add (list) – List of additional group names and/or IDs that the container process will run as.
    group_add: Optional[List[Any]] = None
    # healthcheck (dict) – Specify a test to perform to check that the container is healthy.
    healthcheck: Optional[Dict[str, Any]] = None
    # hostname (str) – Optional hostname for the container.
    hostname: Optional[str] = None
    # labels (dict or list) – A dictionary of name-value labels
    # e.g. {"label1": "value1", "label2": "value2"})
    # or a list of names of labels to set with empty values (e.g. ["label1", "label2"])
    labels: Optional[Dict[str, Any]] = None
    # mounts (list) – Specification for mounts to be added to the container.
    # More powerful alternative to volumes.
    # Each item in the list is a DockerContainerMount object which is then converted to a docker.types.Mount object.
    mounts: Optional[List[DockerContainerMount]] = None
    # network (str) – Name of the network this container will be connected to at creation time
    network: Optional[str] = None
    # network_disabled (bool) – Disable networking.
    network_disabled: Optional[str] = None
    # network_mode (str) One of:
    # bridge - Create a new network stack for the container on on the bridge network.
    # none - No networking for this container.
    # container:<name|id> - Reuse another container’s network stack.
    # host - Use the host network stack. This mode is incompatible with ports.
    # network_mode is incompatible with network.
    network_mode: Optional[str] = None
    # ports (dict) – Ports to bind inside the container.
    # The keys of the dictionary are the ports to bind inside the container,
    # either as an integer or a string in the form port/protocol, where the protocol is either tcp, udp.
    #
    # The values of the dictionary are the corresponding ports to open on the host, which can be either:
    #   - The port number, as an integer.
    #       For example, {'2222/tcp': 3333} will expose port 2222 inside the container as port 3333 on the host.
    #   - None, to assign a random host port. For example, {'2222/tcp': None}.
    #   - A tuple of (address, port) if you want to specify the host interface.
    #       For example, {'1111/tcp': ('127.0.0.1', 1111)}.
    #   - A list of integers, if you want to bind multiple host ports to a single container port.
    #       For example, {'1111/tcp': [1234, 4567]}.
    ports: Optional[Dict[str, Any]] = None
    # remove (bool) – Remove the container when it has finished running. Default: False.
    remove: Optional[bool] = None
    # Restart the container when it exits. Configured as a dictionary with keys:
    # Name: One of on-failure, or always.
    # MaximumRetryCount: Number of times to restart the container on failure.
    # For example: {"Name": "on-failure", "MaximumRetryCount": 5}
    restart_policy: Optional[Dict[str, Any]] = None
    # stdin_open (bool) – Keep STDIN open even if not attached.
    stdin_open: Optional[bool] = None
    # stdout (bool) – Return logs from STDOUT when detach=False. Default: True.
    stdout: Optional[bool] = None
    # stderr (bool) – Return logs from STDERR when detach=False. Default: False.    # tty (bool) – Allocate a pseudo-TTY.
    stderr: Optional[bool] = None
    tty: Optional[bool] = None
    # user (str or int) – Username or UID to run commands as inside the container.
    user: Optional[Union[str, int]] = None
    # volumes (dict or list) –
    # A dictionary to configure volumes mounted inside the container.
    # The key is either the host path or a volume name, and the value is a dictionary with the keys:
    # bind - The path to mount the volume inside the container
    # mode - Either rw to mount the volume read/write, or ro to mount it read-only.
    # For example:
    # {
    #   '/home/user1/': {'bind': '/mnt/vol2', 'mode': 'rw'},
    #   '/var/www': {'bind': '/mnt/vol1', 'mode': 'ro'}
    # }
    volumes: Optional[Union[Dict[str, Any], List]] = None
    # working_dir (str) – Path to the working directory.
    working_dir: Optional[str] = None

    # Data provided by the resource running on the docker client
    status: Optional[str] = None

    def run_container(self, docker_client: DockerApiClient) -> Optional[Container]:

        print_info("Running container: {}".format(self.name))
        # self.verbose_log(
        #     "Args: {}".format(
        #         self.json(indent=2, exclude_unset=True, exclude_none=True)
        #     )
        # )
        try:
            container = docker_client.api_client.containers.run(
                name=self.name,
                image=self.image,
                command=self.command,
                auto_remove=self.auto_remove,
                detach=self.detach,
                entrypoint=self.entrypoint,
                environment=self.environment,
                group_add=self.group_add,
                healthcheck=self.healthcheck,
                hostname=self.hostname,
                labels=self.labels,
                mounts=self.mounts,
                network=self.network,
                network_disabled=self.network_disabled,
                network_mode=self.network_mode,
                ports=self.ports,
                remove=self.remove,
                restart_policy=self.restart_policy,
                stdin_open=self.stdin_open,
                stdout=self.stdout,
                stderr=self.stderr,
                tty=self.tty,
                user=self.user,
                volumes=self.volumes,
                working_dir=self.working_dir,
            )
            return container
        except AttributeError as attr_error:
            logger.warning("AttributeError")
            raise DockerResourceCreationFailedException(attr_error)
        except ImageNotFound as img_error:
            logger.warning("ImageNotFound")
            raise DockerResourceCreationFailedException(
                f"Image {self.image} not found. Explanation: {img_error.explanation}"
            )
        except NotFound as not_found_error:
            logger.warning("NotFound")
            raise DockerResourceCreationFailedException(
                f"Image {self.image} not found. Explanation: {not_found_error.explanation}"
            )
        except APIError as api_err:
            logger.warning("APIError")
            raise DockerResourceCreationFailedException(
                f"Explanation: {api_err.explanation}"
            )
        except Exception as uncaught_err:
            raise DockerResourceCreationFailedException(uncaught_err)

    def _create(self, docker_client: DockerApiClient) -> bool:
        """Creates the Container on docker

        Args:
            docker_client: The DockerApiClient for the current cluster
        """

        logger.debug("Creating: {}".format(self.get_resource_name()))
        container_name: Optional[str] = self.name
        container_object: Optional[Container] = self._read(docker_client)

        # delete the container if it exists and use_cache = False
        if container_object is not None and not self.use_cache:
            print_info(
                f"Deleting container {container_object.name}, use_cache={self.use_cache}"
            )
            self._delete(docker_client)

        try:
            container_object = self.run_container(docker_client)
            if container_object is not None:
                self.verbose_log("Container Created: {}".format(container_object.name))
            else:
                self.verbose_log("Container could not be created")
            # self.verbose_log("Container {}".format(container_object.attrs))
        except Exception as e:
            raise

        # By this step the container should be created
        # Validate that the container is running
        self.verbose_log("Validating container is created")
        if container_object is not None:
            container_object.reload()
            _status: str = container_object.status
            # self.verbose_log("status type: {}".format(type(_status)))
            print_info("Container Status: {}".format(_status))
            self.status = _status
            wait_for_container_to_start = False
            if _status == "created":
                self.verbose_log(
                    f"Container {container_name} is created but not yet running"
                )
                self.verbose_log(
                    "Waiting for 30 seconds for the container to start running"
                )
                sleep(30)
                container_object.reload()
                _status = container_object.status
                if _status == "created":
                    self.verbose_log("Container still not running")
                    self.verbose_log(
                        f"Removing and re-running container {container_name}"
                    )
                    container_object.stop()
                    container_object.remove()
                    container_object = self.run_container(docker_client)
                wait_for_container_to_start = True
            if _status == "exited":
                self.verbose_log(f"Starting container {container_name}")
                container_object.remove()
                container_object = self.run_container(docker_client)
                wait_for_container_to_start = True

            if wait_for_container_to_start:
                self.verbose_log("Waiting for 30 seconds for the container to start")
                sleep(30)
                _status = container_object.status
                while _status != "created":
                    self.verbose_log(
                        "--> status: {}, trying again in 5 seconds".format(_status)
                    )
                    sleep(5)
                    _status = container_object.status
                self.verbose_log("--> status: {}".format(_status))

            if _status == "running" or "created":
                logger.debug("Container Created")
                self.active_resource = container_object
                self.active_resource_class = Container
                return True

        self.verbose_log("Container not found :(")
        return False

    def _read(self, docker_client: DockerApiClient) -> Optional[Container]:
        """Returns a Container object if the container is active on the docker_client"""

        logger.debug("Reading: {}".format(self.get_resource_name()))
        container_name: Optional[str] = self.name
        try:
            container_list: Optional[
                List[Container]
            ] = docker_client.api_client.containers.list(all=True)
            if container_list is not None:
                for container in container_list:
                    if container.name == container_name:
                        self.verbose_log(f"Container {container_name} exists")
                        self.active_resource = container
                        self.active_resource_class = Container
                        return container
        except Exception:
            self.verbose_log(f"Container {container_name} not found")

        return None

    def _delete(self, docker_client: DockerApiClient) -> bool:
        """Deletes the Container from docker

        Args:
            docker_client: The DockerApiClient for the current cluster
        """

        logger.debug("Deleting: {}".format(self.get_resource_name()))
        container_name: Optional[str] = self.name
        container_object: Optional[Container] = self._read(docker_client)
        # Return True if there is no Container to delete
        if container_object is None:
            return True

        # Delete Container
        try:
            self.active_resource = None
            _status: str = container_object.status
            self.status = _status
            self.verbose_log("Container Status: {}".format(_status))
            self.verbose_log("Stopping Container: {}".format(container_name))
            container_object.stop()
            print_info("Waiting 10 seconds for the container to stop")
            sleep(10)
            # If self.remove is set, then the container would be auto removed after being stopped
            # If self.remove is not set, we need to manually remove the container
            if not self.remove:
                self.verbose_log("Removing Container: {}".format(container_name))
                container_object.remove()
        except Exception as e:
            logger.exception("Error while deleting container: {}".format(e))

        # Validate that the Container is deleted
        self.verbose_log("Validating Container is deleted")
        try:
            self.verbose_log("Reloading container_object: {}".format(container_object))
            container_object.reload()
        except NotFound as e:
            self.verbose_log("Got NotFound Exception, Container is deleted")
            return True

        return False
