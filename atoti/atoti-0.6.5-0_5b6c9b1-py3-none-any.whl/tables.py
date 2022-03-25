import logging
from pathlib import Path
from typing import Any, Dict, Mapping

from atoti_core import ReprJson, ReprJsonable, running_in_ipython

from ._delegate_mutable_mapping import DelegateMutableMapping
from ._java_api import JavaApi
from .exceptions import AtotiJavaException
from .table import Table

_GRAPHVIZ_MESSAGE = (
    "Missing Graphviz library which is required to display the graph. "
    "It can be installed with Conda: `conda install graphviz` or by following the download instructions at https://www.graphviz.org/download/."
)


class Tables(DelegateMutableMapping[str, Table], ReprJsonable):
    """Manage the tables."""

    def __init__(self, java_api: JavaApi):
        self._java_api = java_api

    def _repr_json_(self) -> ReprJson:
        return (
            dict(
                sorted(
                    {
                        table.name: table._repr_json_()[0] for table in self.values()
                    }.items()
                )
            ),
            {"expanded": False, "root": "Tables"},
        )

    def _update(self, other: Mapping[str, Table]) -> None:
        raise NotImplementedError(
            "Use `Session.create_table()` or other methods such as `Session.read_pandas()` to create a table."
        )

    def _get_underlying(self) -> Dict[str, Table]:
        return {
            table_name: self[table_name] for table_name in self._java_api.get_tables()
        }

    def __getitem__(self, key: str) -> Table:
        return Table(_name=key, _java_api=self._java_api)

    def __delitem__(self, key: str) -> None:
        self._java_api.delete_table(key)

    @property
    def schema(self) -> Any:
        """Schema of the tables as an SVG graph.

        Note:
            Graphviz is required to display the graph.
            It can be installed with Conda: ``conda install graphviz`` or by following the `download instructions <https://www.graphviz.org/download/>`__.

        Returns:
            An SVG image in IPython and a Path to the SVG file otherwise.
        """
        try:
            path = self._java_api.generate_datastore_schema_image()
            if running_in_ipython():
                from IPython.display import SVG  # pylint: disable=undeclared-dependency

                return SVG(filename=path)
            return Path(path)
        except AtotiJavaException:
            logging.getLogger("atoti.tables").warning(_GRAPHVIZ_MESSAGE)
