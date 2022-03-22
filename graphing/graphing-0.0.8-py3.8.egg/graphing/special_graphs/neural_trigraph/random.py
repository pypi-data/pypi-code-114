import numpy as np
import networkx as nx


def bipartite_edges(l=5,r=6):
    edges1 = set()
    l_set={}; r_set={}
    while len(l_set)<l or len(r_set)<r:
        l_v = np.random.choice(l)+1
        r_v = np.random.choice(r)+l
        edges1.add((l_v,r_v))
    edges1=[]
    for ed in edges1:
        edges1.append([ed[0],ed[1]])
    return edges1


if __name__=="__main__":
    be = bipartite_edges(5,4)
    print(be)
