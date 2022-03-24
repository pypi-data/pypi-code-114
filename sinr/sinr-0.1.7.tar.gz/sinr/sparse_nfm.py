# -*- coding: utf-8 -*-
import numpy as npy
from scipy.sparse import csr_matrix
import numba
from numba.core import types
from numba.typed import List, Dict
from numba import njit, prange
import timeit 

#from line_profiler import LineProfiler

 #from node_fmeasure import NodeFMeasure

import warnings, sys
warnings.filterwarnings("ignore")

@numba.njit(parallel=True)
def _fill(sum_degrees_com, int_degree_indptr, int_degree_indices, int_degree_data, vector, src,dst, weight):
    try:
        #to avoid counting twice edges inside a community
        if vector[src]==vector[dst]:
            sum_degrees_com[vector[src]]+=weight
        else:
            sum_degrees_com[vector[src]]+=weight
            sum_degrees_com[vector[dst]]+=weight
        int_degree_indptr.append(src)
        int_degree_indices.append(vector[dst])
        int_degree_data.append(weight)
        int_degree_indptr.append(dst)
        int_degree_indices.append(vector[src])
        int_degree_data.append(weight)
        '''int_degree[src][vector[dst]]+=weight
        int_degree[dst][vector[src]]+=weight'''
    except: #IndexError:
        pass
    
@numba.njit(parallel=True)
def _arrays_nfm(edges, vector, size_partition, nb_nodes):
    #sum_degrees_com=npy.zeros(size_partition, dtype=numba.int64)
    sum_degrees_com=[0]*size_partition
    
    '''int_degree_indptr = List.empty_list(item_type=numba.int64)
    int_degree_indices = List.empty_list(item_type=numba.int64)
    int_degree_data = List.empty_list(item_type=numba.float64)'''
    
    # UGLY trick to specify type of list to numba
    int_degree_indptr = [0]
    int_degree_indices = [0]
    int_degree_data = [0.0]
    
    int_degree_indptr.pop(0)
    int_degree_indices.pop(0)
    int_degree_data.pop(0)
    
    '''np=npy.zeros((nb_nodes,size_partition), dtype=numba.float64)
    nr=npy.zeros((nb_nodes,size_partition), dtype=numba.float64)'''
    '''int_degree=csr_matrix((nb_nodes, size_partition), dtype=numba.float64)
    np=csr_matrix((nb_nodes,size_partition), dtype=numba.float64)
    nr=csr_matrix((nb_nodes,size_partition), dtype=numba.float64)'''
            
    for src,dst,weight in edges:
        _fill(sum_degrees_com, int_degree_indptr, int_degree_indices, int_degree_data, vector, src, dst, weight)
                        
    return sum_degrees_com, int_degree_indptr, int_degree_indices, int_degree_data

#@numba.njit(parallel=True)
def _compute_nfm(sum_degrees_com, vector, size_partition, weighted,indptr,indices,data,positions):
    print(numba.get_num_threads())
    # UGLY trick to specify type of list to numba
    
    '''np_indptr = List.empty_list(item_type=numba.int64)
    np_indices = List.empty_list(item_type=numba.int64)
    np_data = List.empty_list(item_type=numba.float64)
    
    nr_indptr = List.empty_list(item_type=numba.int64)
    nr_indices = List.empty_list(item_type=numba.int64)
    nr_data = List.empty_list(item_type=numba.float64)'''
    
    np_indptr = [0]
    np_indices = [0]
    np_data = [0.0]
    np_indptr.pop(0)
    np_indices.pop(0)
    np_data.pop(0)

    nr_indptr = [0]
    nr_indices = [0]
    nr_data = [0.0]
    
    nr_indptr.pop(0)
    nr_indices.pop(0)
    nr_data.pop(0)

    # seems that list comprehension if faster ONLY to build lists
   # '''np = [ [ 0 if sum_degrees_com[com]== 0 else float(int_degree[u][com]) / sum_degrees_com[com] \
    #      for com in range(size_partition) ] for u in range(len(vector)) ] 
    #nr = [ [ 0 if weighted_degrees[u]==0 else float(int_degree[u][com]) / weighted_degrees[u] \
    #      for com in range(size_partition) ] for u in range(len(vector)) ]'''

    #for key,value in items.items():
    # print("Entering range")
    for i in range(len(positions)):
        u, com = positions[i]
        if sum_degrees_com[com] != 0:
            np_indptr.append(u)
            np_indices.append(com)
            np_data.append(get_item(u,com,indptr,indices,data) / sum_degrees_com[com])
            #np_data.append(items[(u,com)] / sum_degrees_com[com])
        if weighted[u] != 0:
            nr_indptr.append(u)
            nr_indices.append(com)
            nr_data.append(get_item(u,com,indptr,indices,data) / weighted[u])
            #nr_data.append(items[(u,com)] / weighted[u])
    return np_indptr, np_indices, np_data, nr_indptr, nr_indices, nr_data

@numba.njit
def get_item(row_index, column_index, indptr, indices, data):
    # Get row values
    row_start = indptr[row_index]
    row_end = indptr[row_index + 1]
    row_values = data[row_start:row_end]

    # contains indices of occupied cells at a specific row
    row_indices = list(indices[row_start:row_end])

    # Find a positional index for a specific column index
    value_index = row_indices.index(column_index)
    return row_values[value_index]

# NOTE: maybe we can put partition back as argument
def get_nfm_embeddings(G, vector, size_partition, nodes):
    edges = List()
    [edges.append((edge[0],edge[1],G.weight(edge[0],edge[1]))) for edge in G.iterEdges()]
    # NEED O->n-1
    weighted = List()
    [weighted.append(G.weightedDegree(node)) for node in G.iterNodes()]
    sum_degrees_com,indptr,indices,data=_arrays_nfm(edges, vector, size_partition, nodes)
    # MAYBE the above matrices are enough
    int_degree=csr_matrix((data,(indptr,indices)), shape=(nodes,size_partition))
    positions=list(zip(*int_degree.nonzero()))
    #rows,cols = int_degree.nonzero()
    #items = dict()
    #items = Dict.empty(
    #key_type=types.UniTuple(types.int64, 2),
    #value_type=types.float64,
    #)
    #for  i, j in zip(*int_degree.nonzero()):
    #    items[(i,j)]=int_degree[i,j]
    #items = {(i,j): int_degree[i,j] for i, j in zip(*int_degree.nonzero())}
    
    #is the dict big? numpba can handle dict! need to check how
    #print(sys.getsizeof(items)/1024.,"kylobytes")
    # contains all non zero entries of the matrix
    # print("Compute NFM")
    # print("sum_deg_com", type(sum_degrees_com))
    # print("vector", type(vector))
    # print("type_partition", type(size_partition))
    # print("weighted", type(weighted))
    # print("int_degree.indptr", type(int_degree.indptr))
    # print("int_degree/indices", type(int_degree.indices))
    # print("int_degree.data", type(int_degree.data))
    # print("positions", type(positions))
    

    np_indptr, np_indices, np_data, nr_indptr, nr_indices, nr_data = _compute_nfm(sum_degrees_com, vector, size_partition, weighted, int_degree.indptr,int_degree.indices,int_degree.data,positions)
    np=csr_matrix((np_data,(np_indptr,np_indices)), shape=(nodes,size_partition))
    nr=csr_matrix((nr_data,(nr_indptr,nr_indices)), shape=(nodes,size_partition))
    
    # FIXME: works only on identical shape matrices!
    def concatenate_csr_matrices(matrix1, matrix2):
        new_ind_ptr = matrix2.indptr + len(matrix1.data)
        new_indptr = 2*matrix1.indptr
        new_indices = []
        new_data = []
        
        for r in range(len(matrix1.indptr)-1):
            row_start = matrix1.indptr[r]
            row_end = matrix1.indptr[r + 1]
            # contains indices of occupied cells at a specific row
            row_indices1 = list(matrix1.indices[row_start:row_end])
            row_indices2 = list(matrix2.indices[row_start:row_end])
            new_indices.extend(row_indices1)
            ri = [e+size_partition for e in row_indices2]
            new_indices.extend(ri)
            
            row_values1 = matrix1.data[row_start:row_end]
            row_values2 = matrix2.data[row_start:row_end]
            new_data.extend(row_values1)
            new_data.extend(row_values2)
    
        return csr_matrix((new_data, new_indices, new_indptr))
  
    return np, nr, concatenate_csr_matrices(np,nr)
    
def _compute_sparse_emb(pathG,formatnk,emb=get_nfm_embeddings):
    G=nk.readGraph(pathG, formatnk)
    G.removeSelfLoops()
    communities=nk.community.PLM(G)
    communities.run()
    partition=communities.getPartition()
    emb(G, List(partition.getVector()), len(partition.subsetSizes()), G.numberOfNodes())

if __name__ == '__main__':
    import networkit as nk
    
    
    def get_sparse_size(matrix,sparse=False):
    # get size of a sparse matrix
        if sparse:
            return int((matrix.data.nbytes + matrix.indptr.nbytes + matrix.indices.nbytes) / 1024.)
        else:
            return int(matrix.nbytes / 1024.)
    
    from numba_nfm import get_nfm_embeddings as gne
    
    small_graphs = [
                        ("../../data/dolphins/dolphins.ed",nk.Format.EdgeListSpaceZero)
            ]
    
    medium_graphs = [
                    #("../../data/citeseer/citeseer.renum", nk.Format.EdgeListSpaceZero),
                    ("../../data/citeseer/citeseer.renum_clean", nk.Format.EdgeListSpaceZero),
                    #("../../data/cora/cora.renum", nk.Format.EdgeListSpaceZero),
                    #("../../data/cora/cora.renum_clean", nk.Format.EdgeListSpaceZero),
                    #("../../data/email_eu/email-Eu-core.txt", nk.Format.EdgeListSpaceZero), 
                    #("../../data/email_eu/email-Eu-core.txt_clean", nk.Format.EdgeListSpaceZero),
                    #("../../data/ca-AstroPh/out.ca-AstroPh", nk.Format.EdgeListSpaceOne),
                    ("../../data/ca-AstroPh/out.ca-AstroPh_clean", nk.Format.EdgeListSpaceZero) 
                ]
    
    large_graphs = [
                    #("../../data/facebook-wosn-links/out.facebook-wosn-links.ed_clean", nk.Format.EdgeListSpaceZero),
                    ("../../data/youtube/youtube-links.txt", nk.Format.EdgeListTabOne),
                    #("../../data/flickr/flickr-links.txt", nk.Format.EdgeListTabOne),
                ]
    
    print(min(timeit.repeat("[_compute_sparse_emb(g,f) for g,f in large_graphs]", setup="from __main__ import _compute_sparse_emb", globals=globals(), repeat=5, number=1)))
    print(min(timeit.repeat("[_compute_sparse_emb(g,f,emb=gne) for g,f in large_graphs]", setup="from __main__ import _compute_sparse_emb", globals=globals(), repeat=5, number=1)))
  
    '''for graph, formatnk in medium_graphs:
        G=nk.readGraph(graph, formatnk)
        G.removeSelfLoops()
        communities=nk.community.PLM(G)
        communities.run()
        partition=communities.getPartition()
        
        nps,nrs,embedding_matrix = get_nfm_embeddings(G, partition.getVector(), len(partition.subsetSizes()), G.numberOfNodes())
        #print(get_sparse_size(nps,sparse=True))
        print("done.")
        np,nr,matrix = gne(G, partition.getVector(), len(partition.subsetSizes()), G.numberOfNodes())
        #print(get_sparse_size(np))
        print("Same results in parallel ? ",(matrix==embedding_matrix.toarray()).all(),(nr==nrs.toarray()).all(),(np==nps.toarray()).all())'''
    
