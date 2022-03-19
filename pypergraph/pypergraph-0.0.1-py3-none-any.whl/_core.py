"""Core functionality for hypergraph representation."""

from __future__ import annotations

import itertools as it
import sys
from abc import abstractmethod, abstractproperty
from contextlib import ExitStack, closing, contextmanager
from copy import copy
from typing import (
    TYPE_CHECKING,
    AbstractSet,
    Any,
    Collection,
    Counter,
    FrozenSet,
    Generic,
    Hashable,
    Iterable,
    Iterator,
    Mapping,
    MutableMapping,
    MutableSequence,
    NamedTuple,
    NewType,
    Optional,
    Sequence,
    Tuple,
    TypeVar,
    Union,
    cast,
)

from ._constants import EdgeAttr, EdgeNodeRole, EdgeType, NodeAttr
from ._tools import token_gen
from ._typing import _EdgeID, _EdgeID_co, _NodeID, _NodeID_co

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol


class INodeWrapper(Protocol[_NodeID]):
    """For type checking node wrappers."""

    @abstractproperty
    def name(self) -> _NodeID:
        """The node. A node and its name are a coupled concept."""

    @abstractproperty
    def cleaner(self) -> ExitStack:
        """Cleanup behaviour manager."""

    @abstractproperty
    def attr(self) -> MutableMapping[str, Any]:
        """Data mapping for the node."""

    @abstractmethod
    def register_with(self, dest: HypergraphContainer[_NodeID, Any]):
        """Register a node with a hypergraph."""

    @abstractmethod
    def deregister_from_all(self):
        """Deregister a node from all hypergraphs."""


NodeIncidenceHashable = NewType(
    "NodeIncidenceHashable", FrozenSet[Tuple[EdgeNodeRole, FrozenSet]]
)


class NodeIncidenceSet(Collection[_NodeID_co]):
    """The nodes on which a hyperedge is incident.

    Arguments:
        node_roles: A mapping object from node role to nodes having that role
            for the hyperedge.
    """

    roles: Mapping[EdgeNodeRole, Collection[_NodeID_co]]

    def __init__(
        self, node_roles: Mapping[EdgeNodeRole, Collection[_NodeID_co]]
    ) -> None:
        """Create a representation based on a mapping from role to nodes."""
        self.roles = node_roles

    def __contains__(self, __o: object) -> bool:
        """Test whether a node is incident to the hyperedge."""
        return any(__o in vs for vs in self.roles.values())

    def __iter__(self) -> Iterator[_NodeID_co]:
        """Create an iterator over the nodes incident to the hyperedge."""
        return it.chain.from_iterable(self.roles.values())

    def __len__(self) -> int:
        """Count the nodes incident to the hyperedge."""
        return len(set(self))

    def __eq__(self, __o: object) -> bool:
        """Test for equivalence of the node incidences."""
        if not isinstance(__o, NodeIncidenceSet):
            return NotImplemented

        return self.get_hashable() == __o.get_hashable()

    def __repr__(self) -> str:
        """Obtain a representation of the nodes and their roles."""
        V_repr = V.__qualname__
        rshift = ">>"
        if set(self.roles.keys()) <= {EdgeNodeRole.CANONICAL}:
            return f"{V_repr}({', '.join(sorted(repr(n) for n in self))})"
        elif set(self.roles.keys()) == {EdgeNodeRole.TAIL, EdgeNodeRole.HEAD}:
            tail_repr = ", ".join(
                sorted(repr(n) for n in self.roles[EdgeNodeRole.TAIL])
            )
            head_repr = ", ".join(
                sorted(repr(n) for n in self.roles[EdgeNodeRole.HEAD])
            )
            return f"{V_repr}({tail_repr}) {rshift} {V_repr}({head_repr})"
        return repr(self.roles)

    def _hash_impl(
        self,
    ) -> FrozenSet[Tuple[EdgeNodeRole, FrozenSet[_NodeID_co]]]:
        return frozenset(
            (role, frozenset(nodes)) for (role, nodes) in self.roles.items()
        )

    def get_hashable(self) -> NodeIncidenceHashable:
        """Get a representation which can be used as a dictionary key."""
        return NodeIncidenceHashable(self._hash_impl())

    pass


class V(NodeIncidenceSet[_NodeID_co]):
    """Syntactic sugar for representing sets of nodes."""

    @classmethod
    def _from_roles(
        cls, node_roles: Mapping[EdgeNodeRole, Collection[_NodeID_co]]
    ) -> V[_NodeID_co]:
        result: V[_NodeID_co] = V()
        super(V, result).__init__(node_roles)

        return result

    def __init__(self, *args: _NodeID_co) -> None:
        """Initialise the set of nodes as a base for manipulation."""
        super().__init__(
            # No entry if no arguments
            {EdgeNodeRole.CANONICAL: set(args) for _ in it.islice(args, 1)}
        )

    def __rshift__(self, __o: object) -> V[_NodeID_co]:
        """Use the left operand as the tail and right operand as head."""
        if not isinstance(__o, NodeIncidenceSet):
            return NotImplemented

        empty_set: Collection[_NodeID_co] = set()

        if set(self.roles.keys()).union(__o.roles.keys()) <= {
            EdgeNodeRole.CANONICAL
        }:
            return V._from_roles(
                {
                    EdgeNodeRole.TAIL: self.roles.get(
                        EdgeNodeRole.CANONICAL,
                        empty_set,
                    ),
                    EdgeNodeRole.HEAD: __o.roles.get(
                        EdgeNodeRole.CANONICAL,
                        empty_set,
                    ),
                }
            )

        return NotImplemented


class IEdgeSignature(Protocol[_NodeID_co, _EdgeID_co]):
    """For type checking hyperedge signatures."""

    @abstractproperty
    def nodes(self) -> NodeIncidenceSet[_NodeID_co]:
        """The nodes incident to the hyperedge."""

    @abstractproperty
    def label(self) -> Union[_EdgeID_co, AnonEdgeID]:
        """The distinguishing label for the hyperedge.

        The label is needed to distinguish between hyperedges incident on the
        same nodes in the same roles.
        """


class IEdgeWrapper(Protocol[_NodeID, _EdgeID]):
    """For type checking hyperedge wrappers."""

    @abstractproperty
    def genus(self) -> EdgeType:
        """The hyperedge type."""

    @abstractproperty
    def cleaner(self) -> ExitStack:
        """Cleanup behaviour manager."""

    @abstractproperty
    def attr(self) -> MutableMapping[str, Any]:
        """Data mapping for the hyperedge."""

    @abstractmethod
    def register_with(self, dest: HypergraphContainer[_NodeID, _EdgeID]):
        """Register a hyperedge with a hypergraph."""

    @abstractmethod
    def deregister_from_all(self):
        """Deregister a hyperedge from all hypergraphs."""

    @abstractmethod
    def signature(self) -> IEdgeSignature[_NodeID, _EdgeID]:
        """Obtain the signature of the hyperedge.

        A signature consists of the node incidence information and the hyperedge
        label.
        """


T = TypeVar("T")


class DoublyLinkedListNode(Generic[T]):
    """Wrapper around an item in a linked list."""

    __slots__ = (
        "data",
        "prev_node",
        "next_node",
        "parent",
    )

    data: T
    prev_node: Optional[DoublyLinkedListNode[T]]
    next_node: Optional[DoublyLinkedListNode[T]]
    parent: DoublyLinkedList[T]

    def __init__(self, parent: DoublyLinkedList[T], data: T) -> None:
        """Initialise the linked list node given the data."""
        self.parent = parent
        self.data = data
        self.prev_node = None
        self.next_node = None

    def __irshift__(self, __o: object) -> DoublyLinkedListNode[T]:
        """Link this node to the right operand node."""
        if __o is not None and not isinstance(__o, DoublyLinkedListNode):
            return NotImplemented

        if __o is None:
            self.next_node = None
        else:
            assert __o.parent is self.parent

            self.next_node = __o
            __o.prev_node = self

        return self

    def __ilshift__(self, __o: object) -> DoublyLinkedListNode[T]:
        """Link the right operand node to this node."""
        if __o is not None and not isinstance(__o, DoublyLinkedListNode):
            return NotImplemented

        if __o is None:
            self.prev_node = None
        else:
            assert __o.parent is self.parent

            self.prev_node = __o
            __o.next_node = self

        return self

    def detach(self) -> T:
        """Remove the node from the parent linked list.

        Returns:
            The wrapped data.
        """
        try:
            self.parent
        except Exception:
            return self.data

        cls = DoublyLinkedListNode
        succ = self.next_node
        pred = self.prev_node
        has_succ = isinstance(succ, cls)
        has_pred = isinstance(pred, cls)

        if has_pred and has_succ:
            if TYPE_CHECKING:  # pragma: no cover
                assert isinstance(succ, cls)
                assert isinstance(pred, cls)
            pred >>= succ
        elif not has_pred and has_succ:
            if TYPE_CHECKING:  # pragma: no cover
                assert isinstance(succ, cls)
            assert self.parent._first is self
            self.parent._first = succ
            self.parent._first <<= None
        elif has_pred and not has_succ:
            if TYPE_CHECKING:  # pragma: no cover
                assert isinstance(pred, cls)
            assert self.parent._last is self
            self.parent._last = pred
            self.parent._last >>= None
        else:
            assert self.parent._first is self
            assert self.parent._last is self
            self.parent._first = None
            self.parent._last = None

        del self.parent
        return self.data

    pass


class DoublyLinkedList(Iterable[T]):
    """Doubly linked list.

    Access complexity:

    -   ``O(1)`` append
    -   ``O(1)`` removal by reference
    -   ``O(1)`` access to first element
    -   ``O(1)`` access to last element
    """

    __slots__ = (
        "_first",
        "_last",
    )

    _first: Optional[DoublyLinkedListNode[T]]
    _last: Optional[DoublyLinkedListNode[T]]

    @property
    def _invariant(self) -> bool:
        return (self._first is None) == (self._last is None)

    @property
    def first(self) -> Optional[T]:
        """The first item of the list.

        Returns:
            :py:const:`None` if the list is empty. Otherwise, the first item.
        """
        return self._first.data if self._first is not None else None

    @property
    def last(self) -> Optional[T]:
        """The last item of the list.

        Returns:
            :py:const:`None` if the list is empty. Otherwise, the last item.
        """
        return self._last.data if self._last is not None else None

    @property
    def sole(self) -> T:
        """The sole item of the list.

        Returns:
            The sole item.

        Raises:
            IndexError: If the list does not have exactly 1 item.
        """
        assert self._invariant
        if self._first is None:
            raise IndexError
        elif self._first is self._last:
            return cast(T, self.first)
        raise IndexError

    @property
    def empty(self) -> bool:
        """Whether the list is empty."""
        assert self._invariant
        return self._first is None

    @property
    def has_sole(self) -> bool:
        """Whether the list has exactly 1 item."""
        assert self._invariant
        return self._first is not None and self._first is self._last

    def __init__(self, base: Iterable[T] = ()) -> None:
        """Initialise the linked list with an iterable of items."""
        self._first = None
        self._last = None

        self.extend(base)

    def __iter__(self) -> Iterator[T]:
        """Create an iterator starting from the beginning of the list."""
        cur = self._first

        while cur is not None:
            yield cur.data
            cur = cur.next_node
        pass

    def __reversed__(self) -> Iterator[T]:
        """Create an iterator starting from the end of the list."""
        cur = self._last

        while cur is not None:
            yield cur.data
            cur = cur.prev_node
        pass

    def __len__(self) -> int:
        """Count the number of items in the list."""
        count = 0
        for (count, _) in zip(it.count(1), self):
            pass

        return count

    def _create_node(self, x: T) -> DoublyLinkedListNode[T]:
        return DoublyLinkedListNode(self, x)

    def extend(
        self, iterable: Iterable[T]
    ) -> Iterable[DoublyLinkedListNode[T]]:
        """Append items from the iterable to the end of the list."""
        first = self._first
        new_last = self._last
        old_last = None

        lresult: MutableSequence[DoublyLinkedListNode[T]] = []

        prog = iter(iterable)
        for x in it.islice(prog, 1):
            (old_last, new_last) = (new_last, self._create_node(x))
            if old_last is not None:
                old_last >>= new_last
            lresult.append(new_last)

        if old_last is None and new_last is not None:
            assert first is None
            first = new_last

        for x in prog:
            (old_last, new_last) = (
                cast(DoublyLinkedListNode[T], new_last),
                self._create_node(x),
            )
            old_last >>= new_last
            lresult.append(new_last)

        self._first = first
        self._last = new_last

        return (n for n in lresult)

    def extendleft(
        self, iterable: Iterable[T]
    ) -> Iterable[DoublyLinkedListNode[T]]:
        """Insert items from the iterable at the beginning of the list.

        Notes:
            The beginning of the list will resemble ``iterable`` in reverse.
        """
        old_first = self._first
        last = self._last
        new_first = None

        lresult: MutableSequence[DoublyLinkedListNode[T]] = []

        prog = iter(iterable)
        for x in it.islice(prog, 1):
            new_first = self._create_node(x)
            if old_first is not None:
                new_first >>= old_first
            lresult.append(new_first)

        if new_first is not None and old_first is None:
            assert last is None
            last = new_first

        for x in prog:
            (new_first, old_first) = (self._create_node(x), new_first)
            new_first >>= old_first
            lresult.append(new_first)

        self._first = new_first
        self._last = last

        return (n for n in lresult)

    def append(self, x: T) -> DoublyLinkedListNode[T]:
        """Append an item to the end of the list."""
        (n,) = self.extend((x,))
        return n

    def appendleft(self, x: T) -> DoublyLinkedListNode[T]:
        """Insert an item at the beginning of the list."""
        (n,) = self.extendleft((x,))
        return n

    pass


class HypergraphContainer(Generic[_NodeID, _EdgeID]):
    """Core container for *nodes* and *hyperedges* of a hypergraph.

    This is a mutable data container only and has no behaviour.

    Access complexity:

    -   ``O(1)`` node access by name
    -   ``O(1)`` hyperedge access by label
    -   ``O(1)`` hyperedge access by signature
    """

    _nodes: MutableMapping[_NodeID, INodeWrapper[_NodeID]]
    _edges: MutableMapping[
        Union[_EdgeID, AnonEdgeID], IEdgeWrapper[_NodeID, _EdgeID]
    ]

    _edge_node_incd_llist: MutableMapping[
        NodeIncidenceHashable,
        DoublyLinkedList[IEdgeSignature[_NodeID, _EdgeID]],
    ]

    def __init__(self) -> None:
        """Initialise a container with empty mappings."""
        self._nodes = {}
        self._edges = {}

        self._edge_node_incd_llist = {}

    def __eq__(self, __o: object) -> bool:
        """Check for equality in nodes and hyperedges.

        Data attributes associated with nodes and hyperedges must also match.
        """
        cls = HypergraphContainer  # Play nicely with subclassing

        if not isinstance(__o, cls):
            return NotImplemented

        nodes_match = self._nodes == __o._nodes
        edges_match = self._edges == __o._edges

        return nodes_match and edges_match


class NodeWrapper(NamedTuple):
    """Wrapper around a node for a given hypergraph.

    Arguments:
        name: The identifier for the node. Also identified as the node itself.
        attr: Data attributes for the node. Stored as a mutable mapping object.
        cleaner: A :py:class:`ExitStack` for managing cleanup behaviour.
    """

    name: Hashable  # Would have liked the class to be `Generic` for this
    attr: MutableMapping[str, Any]
    cleaner: ExitStack

    def __eq__(self, __o: object) -> bool:
        """Check for equality with another wrapped node."""
        if not isinstance(__o, self.__class__):
            return NotImplemented

        return (self.name, self.attr) == (__o.name, __o.attr)

    @classmethod
    def create(
        cls,
        node: Hashable,
        dest: HypergraphContainer,
        attr_dict: Mapping[str, Any],
    ) -> INodeWrapper[Hashable]:
        """Wrap a node."""
        result = cls(
            name=node,
            attr=dict(attr_dict),
            cleaner=ExitStack(),
        )
        result.register_with(dest)

        return result

    def register_with(self, dest: HypergraphContainer):
        """Register the node to a hypergraph.

        Registry of a node to a hypergraph is specific to the particular node
        wrapper.
        """
        self.cleaner.enter_context(self.__lifetime(dest))

    def deregister_from_all(self):
        """Deregister the node from all hypergraphs.

        The hypergraphs from which the node is deregistered is specific to the
        particular node wrapper.
        """
        self.cleaner.close()  # Idempotent

    @contextmanager
    def __lifetime(self, dest: HypergraphContainer):
        assert self.name not in dest._nodes

        dest._nodes[self.name] = self

        try:
            yield None
        finally:
            del dest._nodes[self.name]

        pass


AnonEdgeID = NewType("AnonEdgeID", str)


class EdgeSignature(NamedTuple):
    """Hyperedge signature.

    Arguments:
        nodes: The nodes incident to a hyperedge. Describes also the roles of
            the nodes in this hyperedge.
        label: The identifier for the hyperedge. Must be unique across all
            hyperedges for a given hypergraph.
    """

    nodes: NodeIncidenceSet
    label: Hashable  # Would have liked the class to be `Generic` for this


class EdgeWrapper(NamedTuple):
    """Wrapper around a hyperedge for a given hypergraph.

    Arguments:
        nodes: The nodes incident to a hyperedge. Describes also the roles of
            the nodes in this hyperedge.
        label: The identifier for the hyperedge. Must be unique across all
            hyperedges for a given hypergraph.
        genus: The type of hyperedge.
        attr: Data attributes for the hyperedge. Stored as a mutable mapping
            object.
        cleaner: A :py:class:`ExitStack` for managing cleanup behaviour.
    """

    nodes: NodeIncidenceSet
    label: Hashable  # Would have liked the class to be `Generic` for this
    genus: EdgeType
    attr: MutableMapping[str, Any]
    cleaner: ExitStack

    def __eq__(self, __o: object) -> bool:
        """Check for equality with another wrapped hyperedge."""
        if not isinstance(__o, self.__class__):
            return NotImplemented

        return (self.signature(), self.attr) == (__o.signature(), __o.attr)

    @classmethod
    def create(
        cls,
        node_roles: Mapping[EdgeNodeRole, Collection[_NodeID]],
        label: Hashable,
        dest: HypergraphContainer,
        attr_dict: Mapping[str, Any],
    ) -> IEdgeWrapper[_NodeID, Hashable]:
        """Wrap a hyperedge based on the incident nodes and a label."""
        set_roles = set(node_roles.keys())

        genus = EdgeType.INVALID
        if set_roles <= {EdgeNodeRole.CANONICAL}:
            genus = EdgeType.SIMPLE_UNDIRECTED
            for nodes in node_roles.values():
                assert len(nodes) > 0  # Normalised form for undirected edge
                if len(nodes) == 1:
                    genus |= EdgeType.LOOP
                elif len(nodes) >= 3:
                    genus |= EdgeType.HYPER
        elif set_roles == {EdgeNodeRole.TAIL, EdgeNodeRole.HEAD}:
            genus = EdgeType.DIRECTED
            ctr: Counter[_NodeID] = Counter()
            for nodes in node_roles.values():
                if len(nodes) != 1:
                    genus |= EdgeType.HYPER
                ctr.update(set(nodes))

            [(_, max_count)] = ctr.most_common(1)
            if max_count > 1:
                genus |= EdgeType.LOOP
        else:
            raise NotImplementedError("Unsupported hyperedge type")

        result = cls(
            nodes=NodeIncidenceSet(node_roles=node_roles),
            label=label,
            genus=genus,
            cleaner=ExitStack(),
            attr=dict(attr_dict),
        )
        result.register_with(dest)

        return result

    def signature(self) -> EdgeSignature:
        """Obtain the signature of the hyperedge."""
        return EdgeSignature(nodes=self.nodes, label=self.label)

    def register_with(self, dest: HypergraphContainer):
        """Register the hyperedge to a hypergraph.

        Registry of a hyperedge to a hypergraph is specific to the particular
        hyperedge wrapper.

        Nodes are created on the fly if they are not yet registered.
        """
        for node in self.nodes:
            if node not in dest._nodes:
                NodeWrapper.create(node, dest, {})
            # If any of the nodes is deregistered, this edge is deregistered
            dest._nodes[node].cleaner.push(self.cleaner)

        self.cleaner.enter_context(self.__lifetime(dest))

    def deregister_from_all(self):
        """Deregister the hyperedge from all hypergraphs.

        The hypergraphs from which the hyperedge is deregistered is specific to
        the particular hyperedge wrapper.
        """
        self.cleaner.close()  # Idempotent

    @contextmanager
    def __lifetime(self, dest: HypergraphContainer[Hashable, Hashable]):
        ep = dest._edges
        d_llist = dest._edge_node_incd_llist
        node_incd_hash = self.nodes.get_hashable()
        sig = self.signature()  # or `self`?

        assert self.label not in ep
        ep[self.label] = self

        llist = (
            d_llist[node_incd_hash]
            if node_incd_hash in d_llist
            else d_llist.setdefault(node_incd_hash, DoublyLinkedList())
        )
        llist_wrapper = llist.append(sig)

        try:
            yield None
        finally:
            llist_wrapper.detach()
            if llist.empty:
                del d_llist[node_incd_hash]
            del ep[self.label]

        pass


class Hypergraph(Generic[_NodeID, _EdgeID]):
    """Represents a generic hypergraph."""

    _data: HypergraphContainer[_NodeID, _EdgeID]

    # Private state. Try to limit the level of unexposed state.
    _anon_edge_total: int  # Running total of number of anonymous edges added

    def __init__(self) -> None:
        """Initialise an empty hypergraph."""
        self._data = HypergraphContainer()

        self._anon_edge_total = 0

    def __eq__(self, __o: object) -> bool:
        """Test whether the underlying nodes and hyperedges match.

        The following aspects must also match:

        -   Hyperedge labels
        -   Data attributes
        """
        if not isinstance(__o, Hypergraph):
            # Play nicely with subclassing.
            # We don't need the other type to match exactly.
            return NotImplemented

        return self._data == __o._data

    def __copy__(self) -> Hypergraph[_NodeID, _EdgeID]:
        """Create a shallow copy."""
        cls = self.__class__
        clone = cls()

        # Nodes before edges
        for (node_name, node_wrapper) in self._data._nodes.items():
            clone.add_node(node_name, attr_dict=node_wrapper.attr)

        # Edges
        for (edge_label, edge_wrapper) in self._data._edges.items():
            sig = edge_wrapper.signature()
            clone.add_edge(sig.nodes, edge_label, attr_dict=edge_wrapper.attr)

        # Make unobservable state consistent
        clone._anon_edge_total = self._anon_edge_total

        return clone

    def _consume_anon_edge_label(self) -> AnonEdgeID:
        with closing(token_gen()) as g:
            next(g)
            n0 = self._anon_edge_total

            (cand, last_used) = next(
                filter(
                    lambda tpl: tpl[0] not in self._data._edges,
                    ((g.send(n), n) for n in it.count(n0)),
                )
            )

            # TODO: Look at
            #   https://github.com/graphology/graphology/blob/master/src/graphology/src/graph.js#L623-L645

        result = f"_lbl_{cand}"

        self._anon_edge_total = 1 + last_used
        return AnonEdgeID(result)

    @property
    def nodes(self) -> NodeDataAccess[_NodeID]:
        """Access the data attributes of nodes."""
        return NodeDataAccess(self._data._nodes, attrs=NodeAttr.INNER)

    @property
    def edges(self) -> EdgeIncidenceView[_NodeID, _EdgeID]:
        """Obtain a hyperedge view of the hypergraph.

        This view is useful when there are few or no parallel hyperedges.
        """
        return EdgeIncidenceView(
            self._data._edges,
            self._data._edge_node_incd_llist,
        )

    @property
    def edge_labels(self) -> EdgeDataAccess[_NodeID, _EdgeID]:
        """Access the data attributes of hyperedges by label.

        This view is useful when there are parallel hyperedges.
        """
        return EdgeDataAccess(self._data._edges, attrs=EdgeAttr.INNER)

    def add_node(
        self,
        node_name: _NodeID,
        attr_dict: Mapping[str, Any] = None,
    ):
        """Add the specified node into the hypergraph.

        Arguments:
            node_name: The node's name. Must be hashable.
            attr_dict: Data attributes to be set for the node. May be
                :py:const:`None` if no data attributes need to be set.

        Notes:
            If the node is registered with the hypergraph already, its data
            attributes are updated by ``attr_dict``.
        """
        attr_dict = attr_dict if attr_dict is not None else {}
        if node_name not in self._data._nodes:
            NodeWrapper.create(node_name, self._data, attr_dict)
        else:
            self._data._nodes[node_name].attr.update(attr_dict)
        pass

    def add_edge(
        self,
        node_incidence: NodeIncidenceSet[_NodeID],
        label: Union[_EdgeID, AnonEdgeID] = None,
        attr_dict: Mapping[str, Any] = None,
        exception_on_inaction: bool = False,
    ) -> Optional[Union[_EdgeID, AnonEdgeID]]:
        """Add or modify the specified hyperedge.

        There are 3 outcomes of this method:

        (1) A new hyperedge is created with data attributes given by
            ``attr_dict``; or

        (2) An existing hyperedge has its data attributes updated by
            ``attr_dict``;

        (3) Nothing happens.


        If ``label`` is :py:const:`None`, then the following take place
        depending on the number of hyperedges incident on ``node_incidence``:

        -   ``== 0``: A hyperedge incident on ``node_incidence`` is created with
            data attributes ``attr_dict``. (1)

        -   ``== 1``: The hyperedge will have its data attributes updated by
            ``attr_dict``. (2)

        -   ``>= 2``: Nothing happens. (3)

        If ``label`` is not :py:const:`None`, then the following take place:

        -   If no hyperedge has label ``label``, then a hyperedge incident on
            ``node_incidence`` is created. The hyperedge has label ``label`` and
            data attributes ``attr_dict``. (1)

        -   If there is a hyperedge with label ``label`` (and a priori exactly
            one), and that hyperedge is incident on ``node_incidence``, then its
            data attributes are updated by ``attr_dict``. (2)

        -   If there is a hyperedge with label ``label`` (and a priori exactly
            one), and that hyperedge is incident on something other than
            ``node_incidence``, nothing happens. (3)

        Arguments:
            node_incidence: The edge's node incidence. This is an annotated
                collection of nodes.
            label: :py:const:`None` or hashable hyperedge label.
            attr_dict: Data attributes to be set for the hyperedge. May be
                :py:const:`None` if no data attributes need to be set.
            exception_on_inaction: Whether to raise an error if nothing would be
                done.

        Returns:
            :py:const:`None` or label of hyperedge

            The hyperedge is either

            (1) the one that was newly created, or
            (2) the existing one whose data attributes were updated.

            :py:const:`None` is returned only if ``exception_on_inaction`` is
            :py:const:`False` and nothing is done by the method.

        Raises:
            ValueError: If ``exception_on_inaction`` is :py:const:`True` and
                nothing would be done.

        Notes:
            If a hyperedge is to be created (necessarily incident on
            ``node_incidence``) and ``node_incidence`` refers to nodes which do
            not already exist, then those nodes will be created on the fly.
        """
        attr_dict = attr_dict if attr_dict is not None else {}

        create_edge = False
        mutate_data = False
        ep = self._data._edges
        if label is None:
            node_incd_hash = node_incidence.get_hashable()
            edge_node_incd_llist = self._data._edge_node_incd_llist
            llist = (
                edge_node_incd_llist[node_incd_hash]
                if node_incd_hash in edge_node_incd_llist
                else DoublyLinkedList()
            )
            if llist.has_sole:
                # Sole edge with this node incidence
                target_label = llist.sole.label
                mutate_data = True
            elif node_incd_hash not in self._data._edge_node_incd_llist:
                # No edge with this node incidence exists
                target_label = self._consume_anon_edge_label()
                create_edge = True
            else:
                # Multiple edges with this node incidence
                target_label = None
                if exception_on_inaction:
                    raise ValueError
                # pass
            # pass
        else:
            edge_wrapper = ep.get(label)
            if edge_wrapper is None:
                # No edge exists with the label
                target_label = label
                create_edge = True
            elif edge_wrapper.signature().nodes == node_incidence:
                # An edge with this node incidence has the right label
                target_label = label
                mutate_data = True
            else:
                # Some edge incident on different nodes has the label
                target_label = None
                if exception_on_inaction:
                    raise ValueError
                pass
            pass

        if create_edge:
            assert target_label is not None
            EdgeWrapper.create(
                node_incidence.roles,
                target_label,
                self._data,
                attr_dict,
            )
        elif mutate_data:
            assert target_label is not None
            ep[target_label].attr.update(attr_dict)

        return target_label

    def remove_edges(self, *edge_labels: Union[_EdgeID, AnonEdgeID]):
        """Remove hyperedges by label.

        Arguments:
            edge_labels: The labels of hyperedges to be removed.

        Notes:
            Any nodes to which these hyperedges refer remain in the hypergraph.
        """
        ep = self._data._edges
        for label in (lbl for lbl in edge_labels if lbl in ep):
            ep[label].deregister_from_all()
        pass

    def remove_parallel_edges(self, *node_incidence: NodeIncidenceSet[_NodeID]):
        """Remove hyperedges by node incidence.

        Arguments:
            node_incidence: The node incidences of hyperedges to be removed.

        Notes:
            For any two parallel hyperedges, either they are both removed or
            they both remain in the hypergraph.
        """
        ev = self.edges
        self.remove_edges(
            *it.chain.from_iterable(
                ev.parallel_to(node_incd)
                for node_incd in node_incidence
                if node_incd in ev
            )
        )

    def remove_nodes(self, *node_names: _NodeID):
        """Remove nodes by name.

        Arguments:
            node_names: The names of nodes to be removed.

        Notes:
            Any hyperedges referring to these nodes are also removed.
        """
        np = self._data._nodes
        for node in (n for n in node_names if n in np):
            np[node].deregister_from_all()
        pass

    # Convenience functions

    def add_nodes(self, *node_names: _NodeID):
        """Add multiple nodes.

        Arguments:
            node_names: The names of the new nodes.
        """
        for node_name in node_names:
            self.add_node(node_name)
        pass

    def add_edges(
        self, *edges: NodeIncidenceSet[_NodeID]
    ) -> Sequence[Optional[Union[_EdgeID, AnonEdgeID]]]:
        """Add multiple hyperedges without explicit labels.

        Arguments:
            edges: The node incidences of the new hyperedges.
        """
        lresult = []
        for edge in edges:
            lresult.append(self.add_edge(edge, exception_on_inaction=False))
        return tuple(lresult)


class NodeDataAccess(Mapping[_NodeID, Any], AbstractSet[_NodeID]):
    """Access to and iteration over hypergraph nodes and data attributes.

    The extent of access is determined upon instantiation and cannot be changed
    afterwards.

    There is a mechanism to fallback to default values. This is helpful if nodes
    do not uniformly specify the same set of data attributes.

    Additional instances with different access or different default values can
    be created with :py:func:`NodeDataAccess.data`.
    """

    __slots__ = ("_nodes", "_attrs", "_default")

    _nodes: Mapping[_NodeID, INodeWrapper[_NodeID]]
    _attrs: Union[bool, str, Collection[str]]

    def __init__(
        self,
        node_dict: Mapping[_NodeID, INodeWrapper[_NodeID]],
        attrs: Union[bool, str, Collection[str]] = NodeAttr.INNER,
        default=None,
    ) -> None:
        """Wrap node data from a :py:class:`Hypergraph`."""
        default_is_set = default is not None
        if isinstance(attrs, (bool, str)):
            pass
        else:
            default = default if default_is_set else {}
            assert isinstance(default, Mapping)

        self._nodes = node_dict
        self._attrs = attrs
        self._default = default

    # `Mapping` abstract methods
    def __len__(self) -> int:
        """Count the number of nodes in the hypergraph."""
        return len(self._nodes)

    def __iter__(self) -> Iterator[_NodeID]:
        """Create an iterator over node names."""
        return iter(self._nodes)

    def __getitem__(self, node_name: _NodeID) -> Any:
        """Access underlying object or data attribute by node name.

        Arguments:
            node_name: The name of the node to be accessed.

        Raises:
            KeyError: If no node exists with the specified name.
        """
        if isinstance(node_name, slice):
            raise NotImplementedError

        attrs = self._attrs
        attr_dict = self._nodes[node_name].attr
        default = self._default

        if attrs == NodeAttr.INNER:
            return attr_dict.get(NodeAttr.INNER, node_name)  # No `default`
        elif isinstance(attrs, bool):
            # Treat `attrs` as whether mutation is allowed
            if attrs:
                return attr_dict
            else:
                return copy(attr_dict)
        elif isinstance(attrs, str):
            return (
                attr_dict.get(attrs, default)
                if default is not None
                else attr_dict[attrs]
            )

        return {
            a: (attr_dict[a] if a in attr_dict else default[a]) for a in attrs
        }

    # `AbstractSet` abstract methods that are not `Mapping` abstract methods
    def __contains__(self, node_name: object) -> bool:
        """Test whether a node exists with the provided name."""
        return node_name in self._nodes

    # Concrete methods
    def data(
        self,
        attrs: Union[bool, str, Collection[str]] = NodeAttr.INNER,
        default=None,
    ) -> NodeDataAccess[_NodeID]:
        """Use different access or default values.

        Arguments:
            attrs: What to access. This should take one of the following forms.

                .. list-table::
                    :align: left
                    :header-rows: 1

                    *   -   Form
                        -   Access
                    *   -   ``"inner"``
                        -   The object underlying the node.
                    *   -   :py:const:`True`
                        -   All data attributes can be read and modified.
                    *   -   :py:const:`False`
                        -   All data attributes can be read but not modified.
                    *   -   a :py:class:`str` value other than ``"inner"``
                        -   The data attribute with this value as its name can
                            be read but not modified.
                    *   -   a collection of :py:class:`str` values
                        -   The data attributes with these values as their name
                            can be read but not modified.

                In the case where multiple attributes could be read, indexing by
                node name returns a map over data attributes, mapping name to
                value. Otherwise, indexing by node name returns directly the
                value for the data attribute.

            default: Specification of what to return when a node lacks a
                requested data attribute.

                This should be a map if ``attrs`` is a collection of
                :py:class:`str` values.

                This is unused if ``attrs`` is any of the following:
                ``"inner"``, :py:const:`True`, or :py:const:`False`.

        Returns:
            A new :py:class:`NodeDataAccess` instance with the specified access
            and default values.
        """
        return NodeDataAccess(self._nodes, attrs=attrs, default=default)

    def __repr__(self) -> str:
        """Obtain a readable string representation of the node names."""
        return f"{self.__class__.__qualname__}({list(self)})"

    pass


class EdgeDataAccess(
    Mapping[Union[_EdgeID, AnonEdgeID], Any],
    AbstractSet[Union[_EdgeID, AnonEdgeID]],
    Generic[_NodeID, _EdgeID],
):
    """Access to and iteration over hyperedges and data attributes.

    The extent of access is determined upon instantiation and cannot be changed
    afterwards.

    There is a mechanism to fallback to default values. This is helpful if
    hyperedges do not uniformly specify the same set of data attributes.

    Additional instances with different access or different default values can
    be created with :py:func:`EdgeDataAccess.data`.
    """

    __slots__ = ("_edges", "_attrs", "_default")

    _edges: Mapping[Union[_EdgeID, AnonEdgeID], IEdgeWrapper[_NodeID, _EdgeID]]
    _attrs: Union[bool, str, Collection[str]]

    def __init__(
        self,
        edge_dict: Mapping[
            Union[_EdgeID, AnonEdgeID], IEdgeWrapper[_NodeID, _EdgeID]
        ],
        attrs: Union[bool, str, Collection[str]] = True,
        default=None,
    ) -> None:
        """Wrap hyperedge data from a :py:class:`Hypergraph`."""
        default_is_set = default is not None
        if isinstance(attrs, (bool, str)):
            pass
        else:
            default = default if default_is_set else {}
            assert isinstance(default, Mapping)

        self._edges = edge_dict
        self._attrs = attrs
        self._default = default

    # `Mapping` abstract methods
    def __len__(self) -> int:
        """Count the number of hyperedges in the hypergraph."""
        return len(self._edges)

    def __iter__(self) -> Iterator[Union[_EdgeID, AnonEdgeID]]:
        """Create an iterator over hyperedge labels."""
        return iter(self._edges)

    def __getitem__(self, edge_label: Union[_EdgeID, AnonEdgeID]) -> Any:
        """Access underlying object or data attribute by hyperedge label.

        Arguments:
            edge_label: The label of the hyperedge to be accessed.

        Raises:
            KeyError: If no hyperedge exists with the specified label.
        """
        if isinstance(edge_label, slice):
            raise NotImplementedError

        attrs = self._attrs
        attr_dict = self._edges[edge_label].attr
        default = self._default

        if attrs == EdgeAttr.INNER:
            return attr_dict.get(EdgeAttr.INNER, edge_label)  # No `default`
        elif isinstance(attrs, bool):
            # Treat `attrs` as whether mutation is allowed
            if attrs:
                return attr_dict
            else:
                return copy(attr_dict)
        elif isinstance(attrs, str):
            return (
                attr_dict.get(attrs, default)
                if default is not None
                else attr_dict[attrs]
            )

        # Collection[str]
        return {
            a: (attr_dict[a] if a in attr_dict else default[a]) for a in attrs
        }

    # `AbstractSet` abstract methods that are not `Mapping` abstract methods
    def __contains__(self, edge_label: object) -> bool:
        """Test whether a hyperedge exists with the specified label."""
        return edge_label in self._edges

    # Concrete methods
    def data(
        self,
        attrs: Union[bool, str, Collection[str]] = NodeAttr.INNER,
        default=None,
    ) -> EdgeDataAccess[_NodeID, _EdgeID]:
        """Use different access or default values.

        Arguments:
            attrs: What to access. This should take one of the following forms:

                .. list-table::
                    :align: left
                    :header-rows: 1

                    *   -   Form
                        -   Access
                    *   -   ``"inner"``
                        -   The object underlying the hyperedge.
                    *   -   :py:const:`True`
                        -   All data attributes can be read and modified.
                    *   -   :py:const:`False`
                        -   All data attributes can be read but not modified.
                    *   -   a :py:class:`str` value other than ``"inner"``
                        -   The data attribute with this value as its name can
                            be read but not modified.
                    *   -   a collection of :py:class:`str` values
                        -   The data attributes with these values as their name
                            can be read but not modified.

                In the case where multiple attributes could be read, indexing by
                node name returns a map over data attributes, mapping name to
                value. Otherwise, indexing by hyperedge label returns directly
                the value for the data attribute.

            default: Specification of what to return when a hyperedge lacks a
                requested data attribute.

                This should be a map if ``attrs`` is a collection of
                :py:class:`str` values.

                This is unused if ``attrs`` is any of the following:
                ``"inner"``, :py:const:`True`, or :py:const:`False`.

        Returns:
            A new :py:class:`EdgeDataAccess` instance with the specified access
            and default values.
        """
        return EdgeDataAccess(self._edges, attrs=attrs, default=default)

    def __repr__(self) -> str:
        """Obtain a readable string representation of the hyperedge labels."""
        return f"{self.__class__.__qualname__}({list(self)})"


class SingleEdgeDataView(
    Mapping[str, Any],
    AbstractSet[str],
    IEdgeSignature[_NodeID, _EdgeID],
    Generic[_NodeID, _EdgeID],
):
    """Access of data attributes for a single hyperedge."""

    __slots__ = (
        "_attr_dict",
        "_node_incd",
        "_label",
    )

    _attr_dict: Mapping[str, Any]
    _node_incd: NodeIncidenceSet[_NodeID]
    _label: Union[_EdgeID, AnonEdgeID]

    def __init__(
        self,
        label: Union[_EdgeID, AnonEdgeID],
        nodes: NodeIncidenceSet[_NodeID],
        attr_dict: Mapping[str, Any],
    ) -> None:
        """Initialise a data view for a single hyperedge."""
        self._label = label
        self._node_incd = nodes
        self._attr_dict = attr_dict

    @property
    def nodes(self) -> NodeIncidenceSet[_NodeID]:
        """The nodes incident to the hyperedge."""
        return self._node_incd

    @property
    def label(self) -> Union[_EdgeID, AnonEdgeID]:
        """The distinguishing label for the hyperedge."""
        return self._label

    @property
    def inner(self) -> Any:
        """The object underlying the hyperedge."""
        return self._attr_dict.get(EdgeAttr.INNER, self.label)

    # `Mapping` abstract methods
    def __len__(self) -> int:
        """Count the number of data attributes."""
        return len(self._attr_dict)

    def __iter__(self) -> Iterator[str]:
        """Create an iterator over the data attribute names."""
        return iter(self._attr_dict)

    def __getitem__(self, attr_name: str) -> Any:
        """Obtain the value for a given data attribute.

        Arguments:
            attr_name: The name of the data attribute.

        Raises:
            KeyError: If the hyperedge lacks the specified data attribute.
        """
        return self._attr_dict[attr_name]

    # `AbstractSet` abstract methods that are not `Mapping` abstract methods
    def __contains__(self, attr_name: object) -> bool:
        """Test existence of a given data attribute."""
        return attr_name in self._attr_dict

    pass


class EdgeIncidenceView(
    Mapping[NodeIncidenceSet[_NodeID], SingleEdgeDataView[_NodeID, _EdgeID]],
    AbstractSet[NodeIncidenceSet[_NodeID]],
    Generic[_NodeID, _EdgeID],
):
    """Read-only access of hyperedge labels by node incidence.

    This view is useful when there are few or no parallel hyperedges.
    """

    __slots__ = ("_edges", "_edge_node_incd_llist")

    _edges: Mapping[Union[_EdgeID, AnonEdgeID], IEdgeWrapper[_NodeID, _EdgeID]]
    _edge_node_incd_llist: Mapping[
        NodeIncidenceHashable,
        DoublyLinkedList[IEdgeSignature[_NodeID, _EdgeID]],
    ]

    def __init__(
        self,
        edge_dict: Mapping[
            Union[_EdgeID, AnonEdgeID], IEdgeWrapper[_NodeID, _EdgeID]
        ],
        edge_node_incd_llist: Mapping[
            NodeIncidenceHashable,
            DoublyLinkedList[IEdgeSignature[_NodeID, _EdgeID]],
        ],
    ) -> None:
        """Wrap hyperedge data from a :py:class:`Hypergraph`."""
        self._edges = edge_dict  # To accommodate for creating a label view
        self._edge_node_incd_llist = edge_node_incd_llist

    # `Mapping` abstract methods
    def __len__(self) -> int:
        """Count the distinct node incidence sets in the hypergraph."""
        return len(self._edge_node_incd_llist)

    def __iter__(self) -> Iterator[NodeIncidenceSet[_NodeID]]:
        """Create an iterator over node incidence sets."""
        return (
            NodeIncidenceSet(dict(node_incd_hash))
            for node_incd_hash in self._edge_node_incd_llist
        )

    def __getitem__(
        self, node_incidence: NodeIncidenceSet[_NodeID]
    ) -> SingleEdgeDataView[_NodeID, _EdgeID]:
        """View the hyperedge with the provided node incidence.

        Arguments:
            node_incidence: The nodes with which the desired hyperedge should be
                incident.

        Raises:
            KeyError: If no hyperedge exists with the specified node incidence.
            KeyError: If two or more hyperedges exist with the specified node
                incidence.
        """
        if isinstance(node_incidence, slice):
            raise NotImplementedError
        elif isinstance(node_incidence, tuple):
            return self[V(*node_incidence)]

        if not isinstance(node_incidence, NodeIncidenceSet):
            raise NotImplementedError

        llist = self._edge_node_incd_llist[node_incidence.get_hashable()]

        try:
            edge_label = llist.sole.label
            return SingleEdgeDataView(
                edge_label, node_incidence, self._edges[edge_label].attr
            )
        except IndexError:
            raise KeyError
        # pass

    # `AbstractSet` abstract methods that are not `Mapping` abstract methods
    def __contains__(self, node_incidence: object) -> bool:
        """Test whether there a hyperedge exists with a given node incidence."""
        if isinstance(node_incidence, tuple):
            return V(*node_incidence) in self

        if not isinstance(node_incidence, NodeIncidenceSet):
            raise NotImplementedError

        node_incd_hash = node_incidence.get_hashable()
        return (
            node_incd_hash in self._edge_node_incd_llist
            and not self._edge_node_incd_llist[node_incd_hash].empty
        )

    # Concrete methods
    def data(
        self,
        attrs: Union[bool, str, Collection[str]] = EdgeAttr.INNER,
        default=None,
    ) -> EdgeDataAccess[_NodeID, _EdgeID]:
        """Create an object to access hyperedge data attributes.

        An :py:class:`EdgeDataAccess` instance is created by calling
        :py:func:`EdgeDataAccess.data` with the same arguments.

        Arguments:
            attrs: What to access. See :py:func:`EdgeDataAccess.data`.
            default: Specification of what to return when a hyperedge lacks a
                requested data attribute. See :py:func:`EdgeDataAccess.data`.
        """
        return EdgeDataAccess(self._edges, attrs=attrs, default=default)

    def __repr__(self) -> str:
        """Obtain a readable string representation of the hyperedges."""
        return f"{self.__class__.__qualname__}({list(self)})"

    def parallel_to(
        self, node_incidence: NodeIncidenceSet[_NodeID]
    ) -> ParallelEdgeView[_NodeID, _EdgeID]:
        """Return an iterable of parallel hyperedges.

        Arguments:
            node_incidence: The nodes with which the parallel hyperedge should
                be incident.

        Raises:
            KeyError: If no hyperedge exists with the specified node incidence.
        """
        return ParallelEdgeView(
            self._edge_node_incd_llist[node_incidence.get_hashable()]
        )


class ParallelEdgeView(
    Iterable[Union[_EdgeID, AnonEdgeID]], Generic[_NodeID, _EdgeID]
):
    """An iterable over the labels of one family of parallel hyperedges."""

    __slots__ = ("_llist",)

    _llist: DoublyLinkedList[IEdgeSignature[_NodeID, _EdgeID]]

    def __init__(
        self,
        llist: DoublyLinkedList[IEdgeSignature[_NodeID, _EdgeID]],
    ) -> None:
        """Initialise a parallel edge iterator.

        Iteration is enabled by a doubly-linked list structure.
        """
        self._llist = llist

    def __iter__(self) -> Iterator[Union[_EdgeID, AnonEdgeID]]:
        """Create an iterator over the hyperedges in creation order."""
        for sig in self._llist:
            yield sig.label
        pass

    def __reversed__(self) -> Iterator[Union[_EdgeID, AnonEdgeID]]:
        """Create an iterator over the hyperedges in reverse creation order."""
        for sig in reversed(self._llist):
            yield sig.label
        pass
