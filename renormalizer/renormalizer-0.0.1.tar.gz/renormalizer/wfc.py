# -*- coding: utf-8 -*-import numpy as np

import math
import numpy as np

h = 1.0
J = 1.0
Jz = 1.0
D = 50
Length = 16


MPO_i = np.zeros((2, 2, 5, 5))
#0,0 == <alpha alpha>
#0,1 == <alpha beta>
#1,0 == <beta alpha>
#1,1 == <beta beta>
spinExpect = [[0., 0., 0.5],
            [1., 0., 0.],
            [0., 1., 0.],
            [0., 0., -0.5]]
#definition of MPO_i
for i in range(4):
    Splus  = spinExpect[i][0]
    Sminus = spinExpect[i][1]
    Sz = spinExpect[i][2]
    # XXX 这里的identity好像有问题，变成了[[1, 1],[1,1]]
    MPO_i[i//2, i%2, :, :] = [[1., 0., 0., 0., 0.],
            [Splus, 0., 0., 0., 0.],
            [Sminus, 0., 0., 0., 0.],
            [Sz, 0., 0., 0., 0.],
        [-h * Sz, J/2 * Sminus, J/2 * Splus, Jz * Sz, 1.]]
#initial guess of MPS
MPS = [] #MPS is a list
a_i = np.zeros(Length+1, dtype=int)
a_i[0] = a_i[Length] = 1
for i in range(Length):
    if a_i[i] * 2 <= D:
        a_i[i+1] = a_i[i] * 2
    else:
        a_i[i+1] = D
    if Length-i-1 < math.log(a_i[i+1], 2):
        a_i[i+1] = 2 ** (Length-i-1)
    M_i = np.ones((2, a_i[i], a_i[i+1]))
    # empty() function will produce big random numbers
    MPS.append(M_i)
#SVD normalization
#from right to left  PsiBBBBBBBB
#MPO_i (sigmai', sigmai, bi, bi+1)
MPO_i = np.swapaxes(np.swapaxes(MPO_i, 2, 3), 1, 3)  # MPO_i (sigmai', bi, bi+1, sigmai)
psi = np.eye((1))
R = np.ones((1,1,1))
L = np.ones((1,1,1))
Rs = []
Ls = []
for i in range(Length-1, 0, -1):
    print("进行第"+str(i+1)+"位点的计算")
    MPS[i][0] = np.dot(MPS[i][0], psi)
    MPS[i][1] = np.dot(MPS[i][1], psi)
    M = np.hstack((MPS[i][0],MPS[i][1]))

    u, s, vh = np.linalg.svd(M, full_matrices=False)
    psi = u*s

    MPS[i][0, :, :] = vh[:, :a_i[i+1]]
    MPS[i][1, :, :] = vh[:, a_i[i+1]:]
    #calculation of R matrix
    #R (ai+1', bi+1, ai+1)
    #Mi (sigma, ai, ai+1)
    break
    R = np.dot(R, np.swapaxes(MPS[i], 1, 2)) # R-Mi (ai+1', bi+1, sigmai, ai)
    R = np.reshape(R, (a_i[i+1], -1, a_i[i])) # R-Mi (aL', bL*sigmaL, aL-1)
    if (i == Length-1):
        R = np.dot(np.reshape(MPO_i[:,:,0,:], (2, 5, -1)), R) # R-Mi-MPO_i (sigmaL', bL-1, aL', aL-1)
    else:
        R = np.dot(np.reshape(MPO_i, (2, 5, -1)), R) # R-Mi-MPO_i (sigmaL', bL-1, aL', aL-1)
    R = np.dot(np.reshape(np.swapaxes(R, 0, 3), (a_i[i], 5, -1)), np.reshape(np.swapaxes(np.swapaxes(MPS[i], 0, 1), 0, 2), (-1, a_i[i])))
    # R-Mi-MPO_i-Mi (aL-1, bL-1, aL-1')
    Rs.append(R)
#local M matrix update