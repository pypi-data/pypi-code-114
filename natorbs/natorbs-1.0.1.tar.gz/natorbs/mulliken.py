import numpy as np
from numpy import linalg as la

def mulliken_contribs(data, list_of_mos):
    mocoeffs = data.mocoeffs
    for spin,Ct in enumerate(mocoeffs):
        # get LCAO coefficients and reconstruct (approximate) overlap matrix
        C = np.transpose(Ct)
        U, w, Vt = la.svd(C)
        U1 = U[:,0:w.shape[0]]
        Cinv = np.dot(np.dot(np.transpose(Vt), np.diag(1/w)), np.transpose(U1))
        S = np.dot(np.transpose(Cinv), Cinv)

        # list of basis function per atom
        bf = []
        i = 0
        for basis_atom in data.gbasis:
            abf = []
            for contraction in basis_atom:
                ct = contraction[0]
                size = {'S': 1, 'P': 3, 'D': 5, 'F': 7, 'G': 9, 'H': 11, 'I': 13, 'J': 15}[ct]
                for _ in range(size):
                    abf.append(i)
                    i += 1
            bf.append(abf)

        m, n = C.shape
        n_atoms = len(data.atoms)
        n_orbs  = len(list_of_mos)
        f = np.zeros((n_atoms, n_orbs))
        for i in range(n_orbs):
            for atom in range(n_atoms):
                s = 0.0
                for a in bf[atom]:
                    for b in range(m):
                        s += C[a,list_of_mos[i]] * C[b,list_of_mos[i]] * S[a,b]
                f[atom, i] = s
                        
        return f
            
