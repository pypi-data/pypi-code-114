from typing import List, Optional
from typing_extensions import Literal

from phidata.app import PhidataApp
from phidata.app.devbox import default_devbox_name
from phidata.infra.base import InfraConfig
from phidata.infra.docker.args import DockerArgs
from phidata.infra.docker.manager import DockerManager
from phidata.infra.docker.resource.group import DockerResourceGroup
from phidata.utils.log import logger


class DockerConfig(InfraConfig):
    def __init__(
        self,
        name: Optional[str] = None,
        env: Optional[Literal["dev", "stg", "prd"]] = "dev",
        version: Optional[str] = None,
        enabled: bool = True,
        network: str = "phi",
        endpoint: Optional[str] = None,
        apps: Optional[List[PhidataApp]] = None,
        resources: Optional[List[DockerResourceGroup]] = None,
        devbox_name: str = default_devbox_name,
    ):
        super().__init__()
        try:
            self.args: DockerArgs = DockerArgs(
                name=name,
                env=env,
                version=version,
                enabled=enabled,
                network=network,
                endpoint=endpoint,
                apps=apps,
                resources=resources,
                devbox_name=devbox_name,
            )
        except Exception as e:
            raise

    @property
    def network(self) -> str:
        if self.args and self.args.network:
            return self.args.network
        raise NotImplementedError

    @property
    def endpoint(self) -> Optional[str]:
        if self.args and self.args.endpoint:
            return self.args.endpoint
        return None

    @property
    def apps(self) -> Optional[List[PhidataApp]]:
        if self.args and self.args.apps:
            return self.args.apps
        return None

    @property
    def resources(self) -> Optional[List[DockerResourceGroup]]:
        if self.args and self.args.resources:
            return self.args.resources
        return None

    @property
    def devbox_name(self) -> Optional[str]:
        if self.args and self.args.devbox_name:
            return self.args.devbox_name
        return None

    def apps_are_valid(self) -> bool:
        if self.apps is None:
            return False
        for _app in self.apps:
            if not isinstance(_app, PhidataApp):
                raise TypeError("Invalid App: {}".format(_app))
        return True

    def resources_are_valid(self) -> bool:
        if self.resources is None:
            return False
        for _resource in self.resources:
            if not isinstance(_resource, DockerResourceGroup):
                raise TypeError("Invalid Resource: {}".format(_resource))
        return True

    def is_valid(self) -> bool:
        return self.apps_are_valid() or self.resources_are_valid()

    def get_docker_manager(self) -> DockerManager:
        return DockerManager(docker_args=self.args)

    def get_app_by_name(self, app_name: str) -> Optional[PhidataApp]:

        if self.apps is None:
            return None

        for _app in self.apps:
            try:
                if app_name == _app.name:
                    return _app
            except Exception as e:
                logger.exception(e)
                continue
        return None
