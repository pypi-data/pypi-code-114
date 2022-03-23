from paka.cmark import lowlevel

from .types import NodeType, EventType
from .node import Node


class NodeIter:

    def __init__(self, root: Node) -> None:
        self._root = root
        self._iter = lowlevel.iter_new(root._node)

    def __iter__(self):
        return self

    def __next__(self):
        if self.next() != EventType.EVENT_DONE:
            return self.get_node()
        raise StopIteration

    def free(self):
        lowlevel.iter_free(self._iter)

    def next(self):
        """Advance to next node and return event type.

        :returns: One of :ref:`iteration event types <iteration_event_types>`.

        """
        return EventType(lowlevel.iter_next(self._iter))

    def get_node(self):
        """Return current node."""
        return Node(lowlevel.iter_get_node(self._iter))

    def get_event_type(self):
        """Return current event type.

        :returns: One of :ref:`iteration event types <iteration_event_types>`.

        """
        return NodeType(lowlevel.iter_get_event_type(self._iter)) 

    def get_root(self):
        """Return root node."""
        return Node(lowlevel.iter_get_root(self._iter))

    def iter_reset(self, node: Node, event: EventType):
        """Reset the iterator.

        Parameters
        ----------
        iter_
            "Iterator".
        node
            Node to make current.
        event
            :ref:`Event type <iteration_event_types>` to make current.

        """
        return lowlevel.iter_reset(self._iter, node._node, event)
