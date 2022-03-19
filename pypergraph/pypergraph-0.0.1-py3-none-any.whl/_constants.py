"""Literals."""

from enum import Enum, Flag, auto, unique

DEFAULT_TOKEN_PAD_LENGTH = 1


@unique
class Event(Enum):
    """:py:class:`Enum` class of :py:class:`Hypergraph` events."""

    NODE_CREATION = "add_nodes"
    EDGE_CREATION = "add_edges"
    NODE_CREATION_INDUCED_BY_EDGE = "add_nodes_by_edge"

    EDGE_REMOVAL = "remove_edges"
    NODE_REMOVAL = "remove_nodes"
    EDGE_REMOVAL_INDUCED_BY_NODE = "remove_edges_by_node"

    GRAPH_MAKING_COPY = "copy_graph"


class EdgeType(Flag):
    """:py:class:`Flag` class of hyperedge types."""

    SIMPLE_UNDIRECTED = 0
    DIRECTED = auto()
    HYPER = auto()
    LOOP = auto()
    INVALID = auto()


@unique
class EdgeNodeRole(Enum):
    """Different possible roles for a node in the context of a hyperedge."""

    INVALID = "__invalid__"

    CANONICAL = "nodes"

    TAIL = "tail"
    HEAD = "head"

    def __repr__(self) -> str:
        """Gets a string representation of the node role."""
        return f"{self.__class__.__qualname__}.{self.name}"


class NodeAttr:
    """Node data attributes with special treatment."""

    INNER = "inner"


class EdgeAttr:
    """Hyperedge data attributes with special treatment."""

    INNER = "inner"
