from typing import List, Optional

from pydantic import validator

from phidata.app import PhidataApp
from phidata.app.devbox import default_devbox_name
from phidata.infra.base import InfraArgs
from phidata.infra.docker.resource.group import DockerResourceGroup


class DockerArgs(InfraArgs):
    network: str = "phi"
    endpoint: Optional[str] = None
    apps: Optional[List[PhidataApp]] = None
    resources: Optional[List[DockerResourceGroup]] = None
    devbox_name: str = default_devbox_name

    @validator("apps")
    def apps_are_valid(cls, apps):
        if apps is not None:
            for _app in apps:
                if not isinstance(_app, PhidataApp):
                    raise TypeError("App not of type PhidataApp: {}".format(_app))
        return apps
