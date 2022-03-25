from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession

from .client_side_encryption import AzureKeyPair

_JAR_PATH = (Path(__file__).parent / "data" / "atoti-azure.jar").absolute()


class AzurePlugin(Plugin):
    """Azure plugin."""

    def static_init(self) -> None:
        """Init to be called only once."""

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return _JAR_PATH

    def init_session(self, session: BaseSessionBound) -> None:
        """Initialize the session."""

        if not isinstance(session, LocalSession):
            return

        if (
            session._config.azure is not None
            and session._config.azure.client_side_encryption is not None
            and session._config.azure.client_side_encryption.key_pair
        ):
            session._set_client_side_encryption(
                AzureKeyPair(
                    key_id=session._config.azure.client_side_encryption.key_pair.key_id,
                    private_key=session._config.azure.client_side_encryption.key_pair.private_key,
                    public_key=session._config.azure.client_side_encryption.key_pair.public_key,
                )
            )
        session._java_api.gateway.jvm.io.atoti.loading.azure.AzurePlugin.init()
