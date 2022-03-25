from pathlib import Path
from typing import Optional

from atoti_core import BaseSessionBound, Plugin

import atoti as tt
from atoti._local_session import LocalSession

from ._source import load_kafka

_JAR_PATH = (Path(__file__).parent / "data" / "atoti-kafka.jar").absolute()


class KafkaPlugin(Plugin):
    """Kafka plugin."""

    def static_init(self) -> None:
        """Init to be called only once."""
        # See https://github.com/python/mypy/issues/2427.
        tt.Table.load_kafka = load_kafka  # type: ignore[assignment]

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return _JAR_PATH

    def init_session(self, session: BaseSessionBound) -> None:
        """Initialize the session."""
        if not isinstance(session, LocalSession):
            return
        session._java_api.gateway.jvm.io.atoti.loading.kafka.KafkaPlugin.init()
