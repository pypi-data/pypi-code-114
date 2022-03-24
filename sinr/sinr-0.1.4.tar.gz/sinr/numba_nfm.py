# -*- coding: utf-8 -*-
import numpy as npy
import numba
from numba.typed import List
# import timeit as ti

# from node_fmeasure import NodeFMeasure

import warnings

warnings.filterwarnings("ignore")


@numba.njit  # (parallel=True)
def _fill(sum_degrees_com, int_degree, vector, src, dst, weight):
    # try:
    # to avoid counting twice edges inside a community
    if vector[src] == vector[dst]:
        #print("src :", src, "Vector at index:", vector[src])
        sum_degrees_com[vector[src]] += weight
    else:
        sum_degrees_com[vector[src]] += weight
        sum_degrees_com[vector[dst]] += weight
    int_degree[src][vector[dst]] += weight
    int_degree[dst][vector[src]] += weight
    # except: #IndexError:
    #    pass


@numba.njit  # (parallel=True)
def _do_node_fmeasure(edges, weighted_degrees, vector, size_partition, nb_nodes):
    sum_degrees_com = npy.zeros(size_partition, dtype=numba.int64)
    int_degree = npy.zeros((nb_nodes, size_partition), dtype=numba.float64)
    np = npy.zeros((nb_nodes, size_partition), dtype=numba.float64)
    nr = npy.zeros((nb_nodes, size_partition), dtype=numba.float64)
    '''sum_degrees_com=npy.zeros(size_partition, dtype=int)
    int_degree=npy.zeros((nb_nodes, size_partition), dtype=float)
    np=npy.zeros((nb_nodes,size_partition), dtype=float)
    nr=npy.zeros((nb_nodes,size_partition), dtype=float)'''

    for src, dst, weight in edges:
        _fill(sum_degrees_com, int_degree, vector, src, dst, weight)

    # seems that list comprehension if faster ONLY to build lists
    '''np = [ [ 0 if sum_degrees_com[com]== 0 else float(int_degree[u][com]) / sum_degrees_com[com] \
          for com in range(size_partition) ] for u in range(len(vector)) ]

    nr = [ [ 0 if weighted_degrees[u]==0 else float(int_degree[u][com]) / weighted_degrees[u] \
          for com in range(size_partition) ] for u in range(len(vector)) ]'''

    for u in range(len(vector)):
        for com in range(size_partition):
            if sum_degrees_com[com] == 0:
                np[u][com] = 0
            else:
                np[u][com] = int_degree[u][com] / sum_degrees_com[com]
            if weighted_degrees[u] == 0:
                nr[u][com] = 0
            else:
                nr[u][com] = int_degree[u][com] / weighted_degrees[u]

    return np, nr


# NOTE: maybe we can put partition back as argument
def get_nfm_embeddings(G, vector, size_partition, nodes):
    edges = List()
    [edges.append((edge[0], edge[1], G.weight(edge[0], edge[1]))) for edge in G.iterEdges()]
    # NEED O->n-1
    weighted = List()
    [weighted.append(G.weightedDegree(node)) for node in G.iterNodes()]
    np, nr = _do_node_fmeasure(edges, weighted, vector, size_partition, nodes)
    np = npy.asmatrix(np)
    nr = npy.asmatrix(nr)
    embedding_matrix = npy.concatenate((np, nr), axis=1)
    return np, nr, embedding_matrix


if __name__ == '__main__':
    import networkit as nk
    import time

    '''G=nk.graph.Graph(weighted=True)

    G.addNode()
    G.addNode()
    G.addNode()
    G.addNode()
    G.addEdge(0,1,1)
    G.addEdge(0,2,1)
    G.addEdge(0,3,1)
    G.addEdge(1,2,1)
    G.addEdge(1,3,1)
    G.addEdge(2,3,1)



    G.addNode()
    G.addNode()
    G.addNode()
    G.addEdge(3,4,1)
    G.addEdge(4,5,1)
    G.addEdge(4,6,1)
    G.addEdge(5,6,1)



    G.addNode()
    G.addNode()
    G.addNode()
    G.addEdge(6,7,1)
    G.addEdge(7,8,1)
    G.addEdge(7,9,1)
    G.addEdge(8,9,1)

    communities=nk.community.PLM(G)
    communities.run()
    start = time.time()
    partition=communities.getPartition()
    embedding_matrix=get_nfm_embeddings(G, List(partition.getVector()), len(partition.subsetSizes()), G.numberOfNodes())
    end = time.time()
    print("Parallel version, execution time ", end - start)'''

    from parallel_nfm import get_nfm_embeddings as gne

    medium_graphs = [
        # ("../../data/citeseer/citeseer.renum", nk.Format.EdgeListSpaceZero),
        # ("../../data/citeseer/citeseer.renum_clean", nk.Format.EdgeListSpaceZero),
        # ("../../data/cora/cora.renum", nk.Format.EdgeListSpaceZero),
        # ("../../data/cora/cora.renum_clean", nk.Format.EdgeListSpaceZero),
        # ("../../data/email_eu/email-Eu-core.txt", nk.Format.EdgeListSpaceZero),
        # ("../../data/email_eu/email-Eu-core.txt_clean", nk.Format.EdgeListSpaceZero),
        # ("../../data/ca-AstroPh/out.ca-AstroPh", nk.Format.EdgeListSpaceOne),
        ("../../data/ca-AstroPh/out.ca-AstroPh_clean", nk.Format.EdgeListSpaceZero)
    ]

    large_graphs = [
        ("../../data/facebook-wosn-links/out.facebook-wosn-links.ed_clean", nk.Format.EdgeListSpaceZero)
    ]

    for graph, formatnk in medium_graphs:
        G = nk.readGraph(graph, formatnk)
        # G=nk.readGraph("../../data/facebook-wosn-links/out.facebook-wosn-links.ed_clean", nk.Format.EdgeListSpaceZero)
        G.removeSelfLoops()
        communities = nk.community.PLM(G)
        communities.run()
        partition = communities.getPartition()
        print("Classic version on graph", graph.split("/")[-1], "execution time ", end='')
        # %timeit NodeFMeasure(G, partition)
        # nfm.do_embeddings()
        print("Numba version on graph", graph.split("/")[-1], ", execution time ", end='')
        # %timeit get_nfm_embeddings(G, List(partition.getVector()), len(partition.subsetSizes()), G.numberOfNodes())
        np, nr, embedding_matrix = get_nfm_embeddings(G, partition.getVector(), len(partition.subsetSizes()),
                                                      G.numberOfNodes())
        print("Parallel version on graph", graph.split("/")[-1], "execution time ", end='')
        np, nr, matrix = gne(G, partition)
        # %timeit gne(G,partition)
        print("Same results in parallel ? ", (matrix == embedding_matrix).all())
