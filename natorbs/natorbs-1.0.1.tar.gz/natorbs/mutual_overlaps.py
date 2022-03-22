import numpy as np
from numpy import linalg as la

def mutual_overlaps(data1, data2, range_of_mos):
    assert len(data1.mocoeffs) == 1 and len(data2.mocoeffs) == 1, 'no spin resolution yet'
    C1t = data1.mocoeffs[0]

    # get LCAO coefficients and reconstruct (approximate) overlap matrix
    C1 = np.transpose(C1t)
    U, w, Vt = la.svd(C1)
    U1 = U[:,0:w.shape[0]]
    # Generalized inverse
    C1_inv = np.dot(np.dot(np.transpose(Vt), np.diag(1/w)), np.transpose(U1))
    S = np.dot(np.transpose(C1_inv), C1_inv)

    # We assume that data2 is for identical basis set!

    C2t = data2.mocoeffs[0]
    C2 = np.transpose(C2t)

    i1, i2 = range_of_mos
    k = i2 - i1 + 1
    # G[i,j] = overlap of C1[i] with C2[j]
    G = np.zeros((k,k))
    for i in range(k):
        for j in range(k):
            G[i,j] = np.dot(np.transpose(C1[:, i1+i]), np.dot(S, C2[:, i1+j]))

    return G
    
        
