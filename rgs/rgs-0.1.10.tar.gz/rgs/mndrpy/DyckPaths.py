'''
Created on Mar 12, 2021

@author: vladislavkargin

A collection of functions for Dyck paths.
A Dyck path is an array of +1 and -1, such that the total sum is zero and 
the partial sums are always non-negative. 
'''

import rgs.mndrpy.Pairing as pg
import rgs.mndrpy.Utility as ut

import numpy as np
import matplotlib.pyplot as plt
#from numpy.random import MT19937
#from numpy.random import RandomState, SeedSequence


def randomDyckPath(n, seed = None):
    '''
     * Generates a random Dyck path with 2n steps
     * 
     * @param n half-size of path
     * @return a sequence of -1 and 1 steps.
    '''
    
    if seed != None:
        #rs = RandomState(MT19937(SeedSequence(seed)))
        np.random.seed(seed)
    else:
        np.random.seed()    
        
        
    path = [1] * n + [-1] * (n + 1)   
    #shuffle randomly
    np.random.shuffle(path)
    
    #do a cyclic shift. 
    #Find the first occurrence of the minimum
    S = np.cumsum(np.array([0] + path))
    '''
    fig1, ax1 = plt.subplots(nrows=1, ncols=1)
    ax1.plot(S)
    ax1.grid(True)
    '''
    m = np.min(S)
    positions = np.where(S == m)[0]
    pos = positions[0]
    #print(pos)
    path1 = path[pos:] + path[:pos]
    del path1[-1]
    return path1

def allDyckPaths(n):   
    '''returns a list of all pairings of length 2n'''     
    A = []
    for pairing in ut.allPairings(n):
        path = pg.prng2path(pairing)
        #print(path)
        A.append(path)
    return A


def plotDyckPath(path, ax = None, method = "upperLatticePath"):
    ''' plots a Dyck path. Path is either list of 1, -1 or numpy array
    of 1, - 1'''
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    X, Y = buildPlanePath(path, method = method)
    if ax == None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
    major_ticks = np.arange(0, n + 1, 1)
    #minor_ticks = np.arange(0, 101, 5)
    ax.set_xticks(major_ticks)
    #ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    #ax.set_yticks(minor_ticks, minor=True)
    # And a corresponding grid
    ax.grid(which='both')
    ax.plot(X, Y)
    Z = range(n + 1)
    ax.plot(Z)
    return ax  

    
def jeulin_transform(path):
    ''' jeulin transform of the path '''
    L = profile(path)
    H = inv_profile_cdf(path)
    T = []
    for x in H:
        T.append(L[x])
    return T


def inv_profile_cdf(path):
    '''
    "right-continuous" inverse of the profile cdf"
    ''' 
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    H = profile_cdf(path)
    H_inv = []
    for x in range (2 * n + 1):
        pos = np.where(H >= x)[0]
        H_inv.append(pos[0])
    return np.array(H_inv)
    

def profile_cdf(path):
    ''' the array [H(1), H(2), H(x) ] where H(x) is the sum of 
    local times l(t) for t <= x '''
    H = np.cumsum(profile(path))
    return H

def GS_statistic(path):
    ''' calculate the Gorin-Shkolnikov statistic '''
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    x = (area(path) - sum_squared_profile(path)/2)/(n ** (3/2))
    return x
    
def sum_squared_profile(path):    
    ''' calculate the sum of l(x) where l(x) is occupation time for x defined
    in profile(path)'''
    prfl = profile(path)
    S = np.sum(np.square(prfl))
    return S

def profile(path):
    '''
    calculate the occupation times for the Dyck path
    (for the excursion it would be local times l(x))
    The first zero is not counted.
    '''
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    S = np.cumsum(np.array(path))
    #print(S)
    prfl = []
    for x in range(n):
        pos = np.where(S == x)[0]
        l = np.size(pos)
        #print(l)
        if l > 0:
            prfl.append(l)
        else:
            break
    return np.array(prfl)    


def height(path):
    ''' calculate the height of the given Dyck path'''
    S = np.cumsum(np.array(path))
    return max(S)
    


def area(path):
    ''' calculate the area of the given Dyck path, defined as the number
    of unit squares under the path but above the line y = x'''
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    x = 0
    y = 0
    S = [(x, y)]
    for i in range(2 * n):
        if path[i] == 1:
            y += 1
        else:
            x += 1
        S.append((x,y))
    area = 0
    y_prev = 0
    for p in S: #every time as y increases, we add y - x - 1 to the area
        if p[1] > y_prev:
            area += p[1] - p[0]- 1
            y_prev = p[1]
    return area

def rank(path):
    ''' calculates the rank of the path, defined as the number of parts in 
    the corresponding non-crossing partition
    '''
    prtn = pg.prng2prtn(path2prng(path))
    rank = len(prtn)
    return rank

def valleys(path):
    '''return the list of valleys in the path'''
    if isinstance(path, list):
        n = len(path)//2 
    else:
        n = path.shape[0]//2
    valleys = []
    for i in range(2 * n - 1):
        if path[i] == - 1 and path[i + 1] == 1:
            valleys.append(i)
    return valleys

def peaks(path):
    '''find peaks of the given Dyck path,
    and returns their list'''
    if isinstance(path, list):
        n = len(path)//2 
    else:
        n = path.shape[0]//2
    peaks = []
    for i in range(2 * n - 1):
        if path[i] == 1 and path[i + 1] == -1:
            peaks.append(i)
    return peaks


def buildPlanePath(path, method = 'upperLatticePath'):
    ''' creates the path in the plane '''
    if isinstance(path, list):
        n = int(len(path)/2)
    else:
        n = int(path.shape[0]/2)
    x = 0
    y = 0
    S = [(x, y)]
    if method == "upperLatticePath":
        for i in range(2 * n):
            if path[i] == 1:
                y += 1
            else:
                x += 1
            S.append((x,y))
    else:         
        for i in range(2 * n):
            if path[i] == 1:
                x += 1
            else:
                y += 1
            S.append((x,y))
    #print(S)
    X, Y = list(zip(*S)) 

    return X, Y

def pathTo231perm(path):
    '''converts a Dyck path to 231 avoiding permutation
    I am using the description of the bijection from Peterson's "Eulerian paths"
    '''
    #first build the reflected path 
    X, Y = buildPlanePath(path, method = 'lowerLatticePath')
    n = (len(X) - 1)//2
    #One-by-one, for every column from right to left,
    #Find the lowest unoccupied row
    perm = [0] * n 
    used_rows = []
    for x in reversed(range(1, n + 1)):
        y = Y[X.index(x)] # this is the bound from below that the path gives us
        while y in used_rows:
            y += 1
        used_rows.append(y)
        perm[x - 1] = y
    return perm
    
def path2prng(path):
    '''converts a Dyck path to a non-crossing paring.
    '''
    prng = pg.Pairing(path = path)
    return prng


'''
For testing methods
'''
def main():
    
    n = 5
    seed = 3
    path = randomDyckPath(n, seed = seed)
    pks = peaks(path)
    print(path)
    print(pks)
    plotDyckPath(path, method = 'upperLatticePath')
    perm = pathTo231perm(path)
    print(perm)
    
    paths = allDyckPaths(n)
    print(len(paths))
    
    n = 400
    path = randomDyckPath(n)
    plotDyckPath(path)
    prng = path2prng(path)
    prng.draw()
    
    
    print("Height = ", height(path))
    print("Area = ", area(path))
    print("Rank = ", rank(path))
    print("Profile = ", profile(path))
    print("Profile_cdf = ", profile_cdf(path))
    print("Inverse_profile_cdf = ", inv_profile_cdf(path))
    T = jeulin_transform(path)
    #print("Jeulin = ", T)
    print("GS = ", GS_statistic(path))
    #It looks that GS is not centered. 
    plt.figure()
    plt.plot(T)
    
    
    plt.show()
    
    pass

if __name__ == '__main__':
    main()