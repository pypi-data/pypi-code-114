'''
Created on Jan 23, 2021

@author: vladislavkargin
'''
import numpy as np
import matplotlib.pyplot as plt

import rgs.ribbons.Ribbon as rb
import rgs.ribbons.Tiling as tl



     
def findFlips(n, v, tiling, helpers):
    '''
    find all flips that involve the ribbon with index v
    
    Parameters
    -----------
    n: integer
        ribbon length
    v: integer 
        the index of the tile
    tiling: Tiling
        the tiling in which we looking for flips. 
    helpers: a tuple (levels, vertex2level)
        represent the structure of the tiling
        levels is a list of integer lists. Every list is the 
              collection of vertices in this level
        vertex2level is the map from the vertex to levels
             for example [0, 1, 2, 2, ...] means that the
             vertex 0 is in the 0 level, vertex 1 is in the 1 level
             vertices 2 and 3 are in the 2-nd level and so on.
        For a rectangle this structure is calculated by getHelpersRect
        function
        
    
    Returns:
    list of possible indices w. where w is the index of the tile that 
    can be flipped with v. The list can be empty 
    '''
    (levels, vertex2level) = helpers
    flips = []
    A = tiling.ribbons[v]
    level = vertex2level[v]
    a = max([0, level - n + 1])
    b = min([len(levels),level + n])
    for i in range(a, b):
        if i == level:
            continue
        else:
            for w in levels[i]:
                B = tiling.ribbons[w]
                flag, _, _ = A.flip(B)
                if flag:
                    flips.append(w)
    return flips
           
        
    
    #check what happens if we will switch from 0 to 1 or from 1 to 0 
    #in one of the shape locations for ribbon A
    

    #It looks that there are 4 different cub-cases:
    #shape of A = shape of B
    #beginning of A = end of B
    #beginning of A = end of B
    # remaining case. (which is always non-flippable)
    
    

def fibSequence(n, seed = None):
    ''' returns a random increasing sequence of indices (i1, i2, ..., ik)
    such that the indices are between 0 and n-1 and no two indices are 
    adjacent. The number of such sequence is Fibonacci number. The function 
    uses recursion
    '''
    if seed != None:
        np.random.seed(seed)
    seq = []
    if n <= 0:
        return seq
    else:
        x = np.random.randint(2)
        if x == 1: #n-1 is included
            seq = fibSequence(n - 2) + [n - 1]
        else:
            seq = fibSequence(n - 1)
        return seq

def getSquarePairs(sx0, sy0, dir0, sequence):
    ''' generates pairs of squares which should be included in a Stanley's 
    tiling. 
    parameters: s0x and s0y - coordinates of the original square
    dir0 - direction of original step : 'Down' or 'Right'
    sequence: sequence that regulates, which pairs should be included. '''
    sx = sx0
    sy = sy0
    direction = dir0
    #print(sequence)
    pairs = []
    if sequence == []:
        return pairs
    M = max(sequence) + 1
    for i in range(M):
        if i in sequence:
            if direction == 'Right':
                pairs = pairs + [(sx, sy, 'Right')]
                #print(sx, sy, 'Right') 
            else:
                pairs = pairs + [(sx, sy - 1, 'Up')]
                #print(sx, sy - 1, 'Up')
        if direction == 'Right':
            sx = sx + 1
            sy = sy
            direction = "Down"
        else:
            sx = sx
            sy = sy - 1
            direction = "Right"
    return pairs
    
def pairsForRectangle(M, N, seed = None):
    '''gets all marked pairs for an M-by-N rectangle. It is assumed that N >= M'''
    if seed != None:
        np.random.seed(seed)
    all_pairs =[]
    for i in range(M - 1):
        pairs = getSquarePairs(0, i + 1 , "Down", sequence = fibSequence(2 * i + 2))
        all_pairs = all_pairs + pairs
    for i in range (N - M):
        pairs = getSquarePairs(i, M - 1 , "Right", sequence = fibSequence(2 * M - 1))
        all_pairs = all_pairs + pairs
    for i in range (M - 1):
        pairs = getSquarePairs(N - M + i, M - 1 , "Right", sequence = fibSequence(2 * M - 2 - 2 * i))
        all_pairs = all_pairs + pairs
    return all_pairs

def tilingFromPairs(M, N, pairs):
    ''' creates a tiling of an M-by-N rectangle from a collection of pairs '''
    marked = np.zeros((N,M)) #contains information if a particular cell is in the tiling
    ribbons = []
    pairs_set = set(pairs)
    for y0 in range(M):
        for x0 in range(N):
            if marked[x0, y0] == 0: #this cell is not yet explored.
                marked[x0, y0] = 1
                x = x0
                y = y0
                shape = []
                while (x, y, 'Up') in pairs_set or (x, y, 'Right') in pairs_set:
                    #print("x = ", x, "y = ", y)
                    if (x, y, 'Up') in pairs_set:
                        shape.append(1)
                        y = y + 1
                        marked[x, y] = 1
                    else:
                        shape.append(0)
                        x = x + 1
                        marked[x, y] = 1
                ribbon = rb.Ribbon(x0, y0, shape)
                ribbons.append(ribbon)
    tiling = tl.Tiling(ribbons)
    return tiling
                    
    
    
    
def drawPairs(M, N, pairs):
    '''draws all marked pairs for M-by-N rectangle'''
    fig, ax = plt.subplots()
    ax.set_xlim(0, N + 1)
    ax.set_ylim(0, M + 1)
    for (sx, sy, dr) in pairs:
        if dr == "Up":
            line = plt.Line2D((sx + 0.5, sx + 0.5),(sy + 0.5, sy + 1.5), color = 'black')
            ax.add_line(line)
        else: 
            line = plt.Line2D((sx + 0.5, sx + 1.5),(sy + 0.5, sy + 0.5), color = 'black')
            ax.add_line(line)
    return fig, ax    

def randomStanleyTiling(M, N):
    ''' creates a random ribbon tiling of an M-by-N rectangle using Stanley's 
    algorithm'''
    all_pairs = pairsForRectangle(M, N)
    tiling = tilingFromPairs(M,N, all_pairs)
    return tiling


def lengthCounts(tiling):
    '''creates a dictionary that measures lengths of the ribbons in the tiling. 
    Example: {1:3, 2:5, 7:1} means that there are three 1-ribbons, five two ribbons and 1 7-ribbon.'''
    
    length_counts = {}
    for ribbon in tiling.ribbons:
        l = len(ribbon.shape)
        if l + 1 not in length_counts.keys(): 
            length_counts[l + 1] = 1
        else:
            length_counts[l + 1] = length_counts[l + 1] + 1
    return length_counts    
    

'''
For testing methods
'''
def main():
    
    
    ''' some test for functions used in generating Stanley's tilings
    '''
    '''
    n = 20
    seed = 123
    seq = fibSequence(n, seed = seed)
    print(seq)
    
    pairs = getSquarePairs(10, 10, 'Right', seq)
    print(pairs)
    .'''
    
    
    '''some illustration for the Stanley tilings
    '''
    '''
    M= 9
    N = 9
    all_pairs = pairsForRectangle(M, N)
    #print("All pairs = ", all_pairs)
    drawPairs(M, N, all_pairs)
    
    tiling = tilingFromPairs(M,N, all_pairs)
    #print(tiling)
    tiling.draw(M, N, colorType = "ShapePosition")
    length_counts = lengthCounts(tiling)
    print('Length Counts = ', length_counts)
    '''
    
    
    
    '''Testing findFlips function'''
    
    n = 3
    M = 2
    N = 3
    t = tl.standardT(n, M, N)
    print(t)
    #print(t)
    _, ax = plt.subplots(1, 2)
    
    t.draw(M * n, N, ax = ax[0])
    
    #let us look at some helper structures
    levels, vertex2level = tl.getHelpersRect(n, M, N)
    print(levels)
    print(vertex2level)
    
    v = 1
    flips = findFlips(n, v, t, (levels, vertex2level))
    for flip in flips:
        print("w = ", flip)
    
    
    t.flip(v, flips[1])
    print(t)
    t.draw(M * n, N, ax = ax[1])
    
    
    plt.show()

if __name__ == '__main__':
    main()