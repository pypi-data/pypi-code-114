"""Hypergraph data structure."""

from ._core import (
    EdgeDataAccess,
    EdgeIncidenceView,
    Hypergraph,
    NodeDataAccess,
    NodeIncidenceSet,
    ParallelEdgeView,
    SingleEdgeDataView,
    V,
)
from ._typing import _EdgeID, _NodeID

__all__ = (
    "Hypergraph",
    "NodeIncidenceSet",
    "V",
    "NodeDataAccess",
    "EdgeIncidenceView",
    "ParallelEdgeView",
    "SingleEdgeDataView",
    "EdgeDataAccess",
    "_NodeID",
    "_EdgeID",
)

for (_lname, _obj) in tuple(locals().items()):  # pragma: no cover
    if not getattr(_obj, "__module__", "").startswith(f"{__name__}."):
        continue
    try:
        _obj.__module__ = __name__
        _obj.__name__ = _lname
    except AttributeError:  # raised when `__module__` is read-only
        pass
