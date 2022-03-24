from typing import Any, Dict, Tuple

from laituri.docker.credential_manager.docker_v1 import docker_v1_credential_manager
from laituri.docker.credential_manager.registry_credentials_callback_v1 import (
    registry_credentials_callback_v1_credential_manager,
)

NameAndVersion = Tuple[str, str]

credential_managers: Dict[NameAndVersion, Any] = {
    ('docker', '1'): docker_v1_credential_manager,
    ('registry-credentials-callback', '1'): registry_credentials_callback_v1_credential_manager,
}
