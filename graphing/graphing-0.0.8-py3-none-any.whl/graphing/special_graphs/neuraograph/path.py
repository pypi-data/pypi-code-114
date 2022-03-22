import numpy as np
from collections import defaultdict
from graphing.special_graphs.neural_trigraph.rand_graph import neur_trig_edges, rep_graph
from graphing.special_graphs.neurograph.toy_graph import NeuralGraphVert, ToyGraphs
from functools import cmp_to_key


def dfs_search(g, v, t, path=[], visited_dict=set()):
    if v.key not in visited_dict:
        visited_dict.add(v.key)
    if v.key == t.key:
        path.append(t.key)
        return path
    elif v.layer < t.layer:
        path.append(v.key)
        for u in g[v.key]:
            if u.key not in visited_dict:
                res = dfs_search(g, u, t, path, visited_dict)
                if res is not None:
                    return res


def dfs_targeted(g, v, t, path=[], visited_dict=set()):
    if v.key not in visited_dict:
        visited_dict.add(v.key)
    if v.key == t.key:
        path.append(t.key)
        return path
    elif v.layer < t.layer:
        path.append(v.key)

        # Comparator for preferring vertices close in index to target.
        def compare(x, y):
            return abs(x.layer_ix - t.layer_ix)\
                        - abs(y.layer_ix - t.layer_ix)
        for u in sorted(g[v.key], key=cmp_to_key(compare)):
            if u.key not in visited_dict:
                res = dfs_targeted(g, u, t, path, visited_dict)
                if res is not None:
                    return res


def tst():
    g = ToyGraphs.toy_graph_1()
    v1 = NeuralGraphVert(1, 1, 1)
    v7 = NeuralGraphVert(7, 3, 2)
    visited_dict = set()
    path = dfs_search(g, v1, v7, visited_dict=visited_dict)
    print(path)
    print(visited_dict)


def tst2():
    g = ToyGraphs.toy_graph_2()
    v1 = NeuralGraphVert(1, 1, 1)
    v11 = NeuralGraphVert(11, 4, 4)
    visited_dict = set()
    path = dfs_search(g, v1, v11, visited_dict=visited_dict)
    print(path)
    print(visited_dict)


if __name__ == "__main__":
    tst2()


# Demonstration of call-stack behavior and how None is returned
# if nothing found.
def fn1(a):
    if a == 1:
        return a
    else:
        return fn2(a)


def fn2(a):
    if a == 1:
        return a


def tst_call_stack():
    a = fn1(2)
    print(a is None)


# [1] https://stackoverflow.com/questions/29863851/python-stop-recursion-once-solution-is-found
