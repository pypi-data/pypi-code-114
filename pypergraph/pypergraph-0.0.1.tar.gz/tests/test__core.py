"""Test for core functionality."""

from copy import copy

import pytest

from pypergraph import Hypergraph as graph
from pypergraph import V


def test_add_node1():
    """`None` cannot be a node."""
    h = graph()

    # with pytest.raises(Exception):  # TODO: Rethink this.
    h.add_nodes((None,))

    pass


def test_add_node2():
    """Multiple node creation."""
    h = graph()
    h.add_node("A")

    assert set(h.nodes) == {"A"}


def test_add_node3():
    """Single node creation."""
    h = graph()
    h.add_nodes(*"ABCDEFG")

    assert set(h.nodes) == set("ABCDEFG")


def test_add_node4():
    """Node creation with underlying object."""
    import string

    from pypergraph._constants import NodeAttr

    h = graph()

    for (i, letter) in enumerate(string.ascii_lowercase):
        h.add_node(i, attr_dict={NodeAttr.INNER: letter})

    for (node_name, node_undl) in h.nodes.items():
        assert node_undl == string.ascii_lowercase[node_name]
    pass


def test_update_node1():
    """Updating data attributes for nodes."""
    h = graph()

    h.add_node("A", attr_dict={"SOURCE": "ALPHABET", "CODE": 64})
    h.add_node("A", attr_dict={"CODE": 65})

    view = h.nodes.data(attrs=("SOURCE", "CODE"))

    assert view["A"] == {"SOURCE": "ALPHABET", "CODE": 65}


def test_add_edge1():
    """Directed hyperedge creation with induced node creation."""
    h = graph()

    h.add_edge(V(*"AB") >> V("C"))

    assert set(h.nodes) == set("ABC")
    assert list(h.edges) == [V(*"AB") >> V("C")]


def test_add_edge2():
    """Directed hyperedge creation with induced node creation."""
    import string

    h = graph()

    h.add_nodes(*string.ascii_uppercase)
    h.add_edge(V(0, "A") >> V(1))

    assert set(h.nodes) == {0, 1}.union("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert list(h.edges) == [V(0, "A") >> V(1)]


def test_add_edge3():
    """Directed hyperedge creation with explicit label."""
    import string

    h = graph()
    h.add_edge(V(*"ABCD") >> V(10, 11), label="FOO")
    h.add_nodes(*string.ascii_uppercase)

    assert set(h.nodes) == {10, 11}.union("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    assert list(h.edge_labels) == ["FOO"]
    assert list(h.edges) == [V(*"ABCD") >> V(10, 11)]


def test_add_edge4():
    """Parallel directed hyperedge creation."""
    h = graph()

    e = V(*"ABC") >> V(*"DEF")
    en = h.add_edge(e)
    h.add_edge(e, label="BETTER")

    assert list(h.edges) == [e]
    assert list(h.edge_labels) == [en, "BETTER"]


def test_add_edge5():
    """Undirected hyperedge creation."""
    h = graph()

    h.add_edge(V(1, 2, 3))

    assert set(h.nodes) == {1, 2, 3}
    assert list(h.edges) == [V(1, 2, 3)]


def test_add_edge6():
    """Parallel undirected hyperedge creation."""
    h = graph()

    e = V(1, 2, 3)
    en = h.add_edge(e)
    h.add_edge(e, label="BETTER")

    assert list(h.edges) == [e]
    assert list(h.edge_labels) == [en, "BETTER"]


def test_add_edge7():
    """Creation of different types of hyperedges."""
    from pypergraph._constants import EdgeType

    h = graph()

    el1 = h.add_edge(V(1))  # Loop
    el2 = h.add_edge(V(1, 3))  # Simple undirected edge
    el3 = h.add_edge(V(1) >> V(3))
    el4 = h.add_edge(V(1) >> V())
    el5 = h.add_edge(V(1, 3, 5) >> V(3, 4, 5))
    el6 = h.add_edge(V(1) >> V(1))

    ew1 = h._data._edges[el1]
    ew2 = h._data._edges[el2]
    ew3 = h._data._edges[el3]
    ew4 = h._data._edges[el4]
    ew5 = h._data._edges[el5]
    ew6 = h._data._edges[el6]

    assert ew1.genus == EdgeType.SIMPLE_UNDIRECTED | EdgeType.LOOP
    assert ew2.genus == EdgeType.SIMPLE_UNDIRECTED
    assert ew3.genus == EdgeType.DIRECTED
    assert ew4.genus == EdgeType.DIRECTED | EdgeType.HYPER
    assert ew5.genus == EdgeType.DIRECTED | EdgeType.HYPER | EdgeType.LOOP
    assert ew6.genus == EdgeType.DIRECTED | EdgeType.LOOP


def test_add_edge8():
    """Hyperedge creation with underlying object."""
    from pypergraph._constants import EdgeAttr

    h = graph()

    e = V(6) >> V(*range(7, 10))
    h.add_edge(e, attr_dict={EdgeAttr.INNER: 10, "MAX": 9})

    el = h.edges[e].label
    view = h.edge_labels.data(attrs=False)

    assert h.edge_labels[el] == 10
    assert h.edges[e].inner == 10
    assert view[el]["MAX"] == 9


def test_add_edge9():
    """Mass anonymous hyperedge creation."""
    import itertools as it
    import string

    from pypergraph._constants import EdgeAttr

    h = graph()
    ALPHABET = string.ascii_uppercase
    COUNT = 150

    for i in range(COUNT):
        m5 = i % 5
        m7 = i % 7
        m11 = i % 11

        h.add_edge(
            V(*it.chain(ALPHABET[m5::5], ALPHABET[m7::7]))
            >> V(*ALPHABET[m11::11]),
            attr_dict={EdgeAttr.INNER: i},
        )

    assert len(h.edges) == COUNT


def test_update_edge1():
    """Update data attributes of existing hyperedge."""
    h = graph()

    e1 = V("NO") >> V("YES")
    h.add_edge(e1)

    with pytest.raises(KeyError):
        h.edges[e1]["FORGOT"]

    h.add_edge(e1, attr_dict={"FORGOT": 113})

    assert h.edges[e1]["FORGOT"] == 113


def test_update_edge2():
    """No action on ambiguous hyperedge data attribute update."""
    h = graph()

    e = V("NOT") >> V("AFRAID")

    h.add_edge(e, label="1IC")
    h.add_edge(e, label="2IC")

    with pytest.raises(Exception):
        h.add_edge(e, attr_dict={"RANK": "BEST"}, exception_on_inaction=True)
    pass


def test_update_edge3():
    """Targeting by label when updating data attributes."""
    h = graph()

    e = V("LA") >> V("LA")

    h.add_edge(e, label="LAND")
    h.add_edge(e, label="COUNTRY")

    h.add_edge(e, attr_dict={"CLIMATE": "DRY"})
    h.add_edge(e, label="LAND", attr_dict={"CLIMATE": "DRY"})

    view = h.edge_labels.data(attrs="CLIMATE")

    assert list(h.edges) == [e]  # Unique node incidences
    assert view["LAND"] == "DRY"


def test_update_edge4():
    """Label misspecification when updating data attributes."""
    h = graph()

    e1 = V("PUSH") >> V("PULL")
    e2 = V("PULL") >> V("PUSH")

    h.add_edge(
        e1, label="DOOR1", attr_dict={"QUALITY": "HIGH", "REVERSED": False}
    )
    h.add_edge(
        e1, label="DOOR2", attr_dict={"QUALITY": "LOW", "REVERSED": False}
    )
    h.add_edge(e2, label="DOORS", attr_dict={"QUALITY": "HIGH"})

    # Core of test
    h.add_edge(e1, label="DOORS", attr_dict={"REVERSED": True})
    with pytest.raises(Exception):
        h.add_edge(
            e1,
            label="DOORS",
            attr_dict={"REVERSED": True},
            exception_on_inaction=True,
        )

    view = h.edge_labels.data(attrs=("QUALITY", "REVERSED"))

    assert list(h.edges) == [e1, e2]

    with pytest.raises(KeyError):
        view["DOORS"]
    pass


def test_remove_node1():
    """Single node removal."""
    import datetime as dt

    nn = dt.date(2021, 7, 31)

    h = graph()
    h.add_node(nn)

    assert set(h.nodes) == {nn}

    h.remove_nodes(nn)

    assert set(h.nodes) == set()


def test_remove_node2():
    """Single node removal with induced hyperedge removal."""
    import datetime as dt

    nn1 = dt.date(2021, 7, 31)
    nn2 = dt.date(2021, 8, 31)

    h = graph()
    h.add_edge(V(nn1, nn2) >> V("WORLD_END"))
    h.remove_nodes("WORLD_END")

    assert set(h.nodes) == {nn1, nn2}
    assert list(h.edges) == []


def test_remove_node3():
    """Multiple node removal with induced hyperedge removal."""
    h = graph()
    h.add_edge(V(1, 3, 5) >> V(2, 4))
    h.add_edge(V(2, 3) >> V(4, 5))
    h.add_edge(V(1, 4) >> V(3))

    h.remove_nodes(2)

    assert set(h.nodes) == {1, 3, 4, 5}
    assert list(h.edges) == [V(1, 4) >> V(3)]


def test_remove_edge1():
    """Directed hyperedge removal."""
    import datetime as dt

    nn1 = dt.date(2021, 7, 31)
    nn2 = dt.date(2021, 8, 31)

    h = graph()

    h.add_edge(V(0.5, -0.5) >> V(1.0, -1.0))
    h.add_edge(V(nn1, nn2) >> V(1.0))

    en = h.edges[V(0.5, -0.5) >> V(1, -1)].label
    h.remove_edges(en)

    assert set(h.nodes) == {-0.5, 0.5, 1, -1, nn1, nn2}
    assert list(h.edges) == [V(nn1, nn2) >> V(1.0)]


def test_remove_edge2():
    """Directed hyperedge removal."""
    h = graph()

    h.add_edge(V(3.1) >> V(3.14), label="FOO")
    h.add_edge(V(3.1) >> V(3.141), label="BAR")

    h.remove_edges("FOO")

    assert set(h.nodes) == {3.1, 3.14, 3.141}
    assert list(h.edge_labels) == ["BAR"]
    assert list(h.edges) == [V(3.1) >> V(3.141)]


def test_remove_edge3():
    """Undirected hyperedge removal."""
    h = graph()

    en = h.add_edge(V(*range(6)))

    assert list(h.edges) == [V(0, 1, 2, 3, 4, 5)]

    h.remove_edges(en)

    assert len(h.edges) == 0


def test_remove_edge_parallel1():
    """Removal of hyperedges parallel to an undirected hyperedge."""
    from pypergraph._constants import EdgeAttr

    h = graph()

    for i in range(4):
        h.add_edge(V(*range(6)), label=f"e_{i}", attr_dict={EdgeAttr.INNER: i})

    assert len(h.edges) == 1
    assert len(h.edge_labels) == 4

    h.remove_parallel_edges(V(*range(6)))

    assert len(h.edges) == 0
    assert len(h.edge_labels) == 0


def test_remove_edge_parallel2():
    """Removal of hyperedges parallel to a directed hyperedge."""
    from pypergraph._constants import EdgeAttr

    h = graph()
    e = V(1, 3) >> V(0, 2)

    for i in range(4):
        h.add_edge(e, label=f"e_{i}", attr_dict={EdgeAttr.INNER: i})

    assert len(h.edges) == 1
    assert len(h.edge_labels) == 4

    h.remove_parallel_edges(e)

    assert len(h.edges) == 0
    assert len(h.edge_labels) == 0


def test_comparison_empty_graph():
    """Equality comparison of hypergraphs."""
    h1 = graph()
    h2 = graph()

    assert h1 == h2


def test_comparison_type_mismatch1():
    """Equality comparison under type mismatch."""
    h = graph()
    o = object()

    assert h != o


def test_comparison_type_mismatch2():
    """Equality comparison under type mismatch of internal container."""
    from unittest.mock import Mock

    h1 = graph()
    h2 = Mock(spec=h1, _data=1)

    assert h1 != h2


def test_sequential_add_edge1():
    """Sequential edge creation."""
    h1 = graph()
    h2 = graph()

    e1 = V("A") >> V("B")
    e2 = V("A") >> V("C")
    e3 = V("A") >> V("BC")
    e4 = V("AB") >> V("DE")
    e5 = V("AC") >> V("DE")
    e6 = V("BC") >> V("DE")

    h1.add_edges(e1, e2)
    h1.add_edges(e3, e4, e5, e6)

    h2.add_edges(e1, e2, e3, e4, e5, e6)

    assert h1 == h2


def test_sequential_add_edge2():
    """Bulk testing of sequential edge creation."""
    import itertools as it

    e1 = V(1, 3) >> V(4, 6)
    e2 = V(1, 2) >> V(3)
    e3 = V(3, 5) >> V(1, 6)
    e4 = V(1) >> V(4, 5)

    for order in it.permutations((e1, e2, e3, e4)):
        h1 = graph()
        h2 = graph()

        h1.add_edges(*order[:2])
        h1.add_edges(*order[2:])

        h2.add_edges(*order)

        assert h1 == h2

        del h1
        del h2

    pass


def test_shallow_copy1():
    """Shallow copy of empty hypergraph."""
    h1 = graph()
    h2 = copy(h1)

    assert h1 == h2


def test_shallow_copy2():
    """Shallowness of shallow copy."""
    data1 = {"main": [1, 2]}

    h1 = graph()
    h1.add_node("MUTANT", attr_dict=data1)
    h2 = copy(h1)

    data1["main"].append(-1)
    (data2,) = h2.nodes.data(attrs=False).values()

    assert data1 == data2
    assert h1 == h2


def test_shallow_copy3():
    """Shallowness of nonempty hypergraph."""
    e1 = V(*"ABC") >> V(*"DEF")
    e2 = V(*"DEF") >> V(*"ABC")
    e3 = V(1) >> V(2)
    e4 = V(2) >> V(1)

    h1 = graph()
    (el1, el2) = h1.add_edges(e1, e2)
    h2 = copy(h1)

    h1.remove_edges(el1, el2)
    h3 = copy(h1)

    h1.add_edges(e3, e4)
    h3.add_edges(e3, e4)

    assert h1 == h3

    assert list(h2.edges) == [e1, e2]


def test_nodeview_contains():
    """Membership test for node view."""
    harry = graph()

    harry.add_node("WIZARD")

    assert "WIZARD" in harry.nodes


def test_nodeview_iter():
    """Iteration exhaustion of node view."""
    h = graph()

    h.add_nodes(*"123XYZ")

    iter_node = iter(h.nodes)
    set_node_names = frozenset(iter_node)

    assert set_node_names == {"1", "2", "3", "X", "Y", "Z"}


def test_nodeview_getitem1():
    """Retrieve data from node view."""
    h = graph()

    h.add_node("Willy Wonka", attr_dict={"alignment": "CHAOTIC_NEUTRAL"})

    (alignment,) = h.nodes.data(attrs="alignment").values()

    assert alignment == "CHAOTIC_NEUTRAL"


def test_nodeview_getitem2():
    """Exception on retrieving nonexistent node."""
    h = graph()
    h.add_nodes("Ay", "Bee", "See")

    with pytest.raises(KeyError):
        h.nodes["Dee"]
    pass


def test_nodeview_getitem3():
    """No support for slice indexing for node views."""
    h = graph()
    h.add_nodes("Ay", "Bee", "See")

    with pytest.raises(NotImplementedError):
        h.nodes["Ay":"See"]
    pass


def test_nodeview_mutate():
    """Mutation of node data attributes."""
    h = graph()
    h.add_nodes(*"AB")

    data_mod = h.nodes.data(attrs=True)
    data_mod["A"]["special"] = True

    special_view = h.nodes.data(attrs="special", default=False)

    assert special_view["A"]
    assert not special_view["B"]


def test_nodeview_len():
    """Count nodes."""
    import string

    h = graph()
    h.add_nodes(*string.ascii_uppercase)

    assert len(h.nodes) == len(string.ascii_uppercase)


def test_nodeview_repr():
    """String representation of node view object."""
    h = graph()
    h.add_nodes(*"ABC145")

    s = repr(h.nodes)

    assert isinstance(s, str)


def test_edgeincdview_getitem1():
    """No support for slice indexing for hyperedge view."""
    h = graph()

    with pytest.raises(NotImplementedError):
        h.edges[1:3]
    pass


def test_edgeincdview_getitem2():
    """No support for slice indexing for hyperedge view."""
    h = graph()

    h.add_edge(V(1, 3, 5), label="DOG")

    assert h.edges[1, 3, 5].label == "DOG"


def test_edgeincdview_getitem3():
    """Support only node incidence sets for hyperedge view indexing."""
    h = graph()

    h.add_edge(V(2, 4, 3, 5), label="CAT")

    with pytest.raises(NotImplementedError):
        h.edges[object()]
    pass


def test_edgeincdview_getitem4():
    """Failure when multiple parallel hyperedges."""
    h = graph()

    e = V(4, 3) >> V()
    h.add_edge(e, label="FISH")
    h.add_edge(e, label="SHEEP")

    with pytest.raises(KeyError):
        h.edges[e]
    pass


def test_edgeincdview_membership():
    """Check whether a hyperedge exists with a given node incidence."""
    h = graph()

    e1 = V(1, 4, 5) >> V(2, 3)
    e2 = V(5, 1) >> V(*"ENERGY")
    h.add_edge(e1)
    h.add_edge(V(1, 2, 5, 4, 3))

    assert e1 in h.edges
    assert e2 not in h.edges
    assert tuple(range(1, 6)) in h.edges

    with pytest.raises(NotImplementedError):
        23947 not in h.edges
    pass


def test_edgeincdview_transform():
    """Expand a hyperedge view into a hyperedge label view."""
    from pypergraph._constants import EdgeAttr

    h = graph()
    el1 = h.add_edge(V(2) >> V(3), attr_dict={EdgeAttr.INNER: "FIRST"})

    view = h.edges.data()

    assert view[el1] == "FIRST"


def test_edgeincdview_repr():
    """String representation of hyperedge view."""
    h = graph()

    h.add_edge(V(2) >> V(6))
    h.add_edge(V(6) >> V(3))

    s = repr(h.edges)

    assert isinstance(s, str)


def test_edgeincdview_parallel():
    """Parallel hyperedge iterator."""
    from pypergraph._constants import EdgeAttr

    h = graph()

    e = V(*"DOG") >> V(*"CAT")
    for i in range(5):
        h.add_edge(e, label=f"e_{i}", attr_dict={EdgeAttr.INNER: i})

    para_iterable = h.edges.parallel_to(e)
    view = h.edge_labels

    assert set(view[pe] for pe in para_iterable) == set(range(5))
    assert set(view[pe] for pe in reversed(para_iterable)) == set(range(5))


def test_edgelabelview_getitem():
    """No support for slice indexing for hyperedge label view."""
    h = graph()
    h.add_edge(V(*range(6)) >> V(*range(6, 10)))

    with pytest.raises(NotImplementedError):
        h.edge_labels[1:10]
    pass


def test_edgelabelview_mutate():
    """Mutation of hyperedge data attributes."""
    h = graph()
    (el0, el1) = h.add_edges(
        V(0) >> V(2, 3),
        V(1, 3) >> V(0, 2),
    )

    data_mod = h.edge_labels.data(attrs=True)
    data_mod[el0]["weight"] = 10.0

    weight_view = h.edge_labels.data(attrs="weight", default=1.0)

    assert weight_view[el0] == 10.0
    assert weight_view[el1] == 1.0


def test_edgelabelview_membership():
    """Existence of hyperedge with given label."""
    h = graph()
    h.add_edge(V(*"XYZ") >> V(*range(5)), label="FIRST")

    assert "FIRST" in h.edge_labels
    assert "SECOND" not in h.edge_labels


def test_edgelabelview_repr():
    """String representation of hyperedge label view."""
    h = graph()
    h.add_edge(V(4, 7, 10) >> V(*"UVW"))

    s = repr(h.edge_labels)

    assert isinstance(s, str)


def test_singleedgeview_sig():
    """Single hyperedge view signature reproduction."""
    import datetime as dt

    h = graph()

    dates = [dt.date(2021, 7, 31), dt.date(2021, 8, 31)]
    e = V(*dates)
    h.add_edge(e, label="EVENT")

    view = h.edges[e]
    assert view.nodes == e
    assert view.label == "EVENT"


def test_singleedgeview_data_attr():
    """Counting data attributes with a single hyperedge view."""
    h = graph()

    e = V(5, 8) >> V()
    h.add_edge(e, attr_dict={"DEGENERATE": False, "filler": 1})

    view = h.edges[e]

    assert len(view) == 2
    assert frozenset(view.items()) == {("DEGENERATE", False), ("filler", 1)}
    assert "filler" in view


def test_node_incd_repr1():
    """String representation of node incidence set."""
    s1 = repr(V(1, 4, 7))
    s2 = repr(V(1) >> V(*"ABCDEFG"))

    assert isinstance(s1, str) and isinstance(s2, str)


def test_node_incd_repr2():
    """String representation of general node incidence set."""
    from pypergraph._core import NodeIncidenceSet

    node_incd = NodeIncidenceSet(
        {
            "CUSTOM_0": (1, 3, 5),
            "CUSTOM_1": (2, 4, 6),
        }
    )

    s = repr(node_incd)

    assert isinstance(s, str)


def test_node_incd_membership():
    """Node incidence check."""
    e = V(1) >> V(2)
    assert 1 in e


def test_node_incd_count():
    """Node incidence node count."""
    e = V(*"ABCDEF") >> V("A", 2)
    assert len(e) == 7


def test_node_incd_equality():
    """Node incidence comparison."""
    e1 = V(*"ABCDEF") >> V("A", 2)
    e2 = V(*"FABEDC") >> V(2, "A")
    o = object()

    assert e1 == e2
    assert e1 != o


def test_sugar_node_incd_connect_type_mismatch1():
    """Syntactic sugar on badly typed node incidence set."""
    with pytest.raises(TypeError):
        V(1) >> 5
    with pytest.raises(TypeError):
        V(1) << 5
    pass


def test_sugar_node_incd_connect_type_mismatch2():
    """Syntactic sugar on badly typed node incidence set."""
    with pytest.raises(TypeError):
        V(1) >> V(2) >> V(3)
    pass


def test_llist_node_link_to_type_mismatch():
    """Syntactic sugar to connect linked list nodes."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    n = llist.append(1)

    with pytest.raises(TypeError):
        n >>= 1
    with pytest.raises(TypeError):
        n <<= 1
    pass


def test_llist_node_link_from():
    """Syntactic sugar to connect linked list nodes."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    n1 = llist.append(1)
    llist.append(2)
    n3 = llist.append(3)

    n3 <<= n1

    assert len(llist) == 2


def test_llist_node_break_right():
    """Syntactic sugar to right-terminate a linked list."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    llist.append(1)
    n = llist.append(2)
    llist.append(3)

    n >>= None

    assert len(llist) == 2


def test_llist_node_break_left():
    """Syntactic sugar to left-terminate a linked list."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    llist.append(1)
    n = llist.append(2)
    llist.append(3)
    llist.append(4)

    n <<= None

    for (i, _) in enumerate(reversed(llist)):
        pass
    length = i + 1

    assert length == 3


def test_llist_node_redetach():
    """Syntactic sugar to left-terminate a linked list."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    llist.append(1)
    n = llist.append(2)
    llist.append(3)
    llist.append(4)

    n.detach()
    n.detach()

    assert len(llist) == 3


def test_llist_node_detach_ends():
    """Popping the endpoint items from a linked list."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()

    with pytest.raises(IndexError):
        llist.sole

    n0 = llist.append(0)
    llist.extend(range(1, 6))
    n6 = llist.append(6)

    n0.detach()
    n6.detach()

    assert len(llist) == 5
    assert llist.first == 1
    assert llist.last == 5

    with pytest.raises(IndexError):
        llist.sole
    pass


def test_llist_extendleft():
    """Insertion of items at the beginning of a linked list."""
    from pypergraph._core import DoublyLinkedList

    llist = DoublyLinkedList()
    llist.extendleft(range(6))

    assert llist.first == 5

    llist.appendleft(6)

    assert len(llist) == 7
    assert llist.first == 6
    assert llist.last == 0


def test_wrapper_equality():
    """Node and hyperedge wrapper equality comparison."""
    h = graph()
    h.add_edge(V("HELLO") >> V("WORLD"), label="demo")
    nw = h._data._nodes["HELLO"]
    ew = h._data._edges["demo"]

    assert not (nw == 1)  # Want explicit usage of `__eq__`
    assert not (ew == 2)


def test_edge_wrapper_unsupported_node_role():
    """Hyperedge wrapper creation with unrecognised node roles."""
    from pypergraph._core import EdgeWrapper

    h = graph()

    with pytest.raises(NotImplementedError):
        EdgeWrapper.create(
            {"CUSTOM_0": (1,), "CUSTOM_1": (2, 3)}, "demo", h._data, {}
        )
    pass
