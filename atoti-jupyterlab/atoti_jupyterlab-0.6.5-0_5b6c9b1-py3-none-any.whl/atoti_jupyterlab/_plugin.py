from pathlib import Path
from typing import Optional

from atoti_core import BaseSession, BaseSessionBound, Plugin
from atoti_query import QueryResult

from ._link import link
from ._visualize import visualize
from ._widget_conversion import create_query_result_repr_mimebundle_method_
from ._widget_manager import WidgetManager


class JupyterLabPlugin(Plugin):
    """JupyterLab plugin."""

    _widget_manager: WidgetManager = WidgetManager()

    def static_init(self) -> None:
        """Init to be called only once."""

        # See https://github.com/python/mypy/issues/2427.
        BaseSession.link = link  # type: ignore[assignment]
        # See https://github.com/python/mypy/issues/2427.
        BaseSession.visualize = visualize  # type: ignore[assignment]

        # See https://github.com/python/mypy/issues/2427.
        QueryResult._repr_mimebundle_ = create_query_result_repr_mimebundle_method_(  # type: ignore[assignment]
            original_method=QueryResult._repr_mimebundle_
        )

    def get_jar_path(self) -> Optional[Path]:
        """Return the path to the JAR."""
        return None

    def init_session(self, session: BaseSessionBound) -> None:
        """Initialize the session."""
        session._widget_manager = self._widget_manager  # type: ignore
