from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession

from .client_side_encryption import AwsKeyPair, AwsKmsConfig

_JAR_PATH = (Path(__file__).parent / "data" / "atoti-aws.jar").absolute()


class AWSPlugin(Plugin):
    """AWS plugin."""

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
            session._config.aws is not None
            and session._config.aws.client_side_encryption is not None
        ):
            if session._config.aws.client_side_encryption.kms is not None:
                session._set_client_side_encryption(
                    AwsKmsConfig(
                        region=session._config.aws.region,
                        key_id=session._config.aws.client_side_encryption.kms.key_id,
                    )
                )
            if session._config.aws.client_side_encryption.key_pair is not None:
                session._set_client_side_encryption(
                    AwsKeyPair(
                        region=session._config.aws.region,
                        private_key=session._config.aws.client_side_encryption.key_pair.private_key,
                        public_key=session._config.aws.client_side_encryption.key_pair.public_key,
                    )
                )
        session._java_api.gateway.jvm.io.atoti.loading.s3.AwsPlugin.init()
