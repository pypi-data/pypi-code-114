from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

from atoti._local_session import LocalSession

_JAR_PATH = (Path(__file__).parent / "data" / "atoti-gcp.jar").absolute()


class GCPPlugin(Plugin):
    """GCP plugin."""

    def static_init(self) -> None:
        """Init to be called only once."""

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return _JAR_PATH

    def init_session(self, session: BaseSessionBound) -> None:
        """Initialize the session."""
        if not isinstance(session, LocalSession):
            return
        session._java_api.gateway.jvm.io.atoti.loading.gcp.GcpPlugin.init()  # type: ignore
