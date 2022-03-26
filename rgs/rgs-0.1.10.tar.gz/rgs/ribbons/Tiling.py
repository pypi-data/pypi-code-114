'''
Created on Jan 20, 2021

@author: vladislavkargin
'''

import numpy as np
import matplotlib.pyplot as plt
from itu.algs4.graphs import digraph as dgr


import rgs.ribbons.Ribbon as rb
import rgs.ribbons.Utility as ut

class Tiling(object):
    '''
    Realizes a tiling, which is a list of non-intersecting ribbons.

    '''


    def __init__(self, ribbons):
        '''
        Constructor
        Parameters
        ---------------
        ribbons: a list of ribbons
        
        '''
        self.ribbons = ribbons
    
    def findRibbon(self, x, y):
        ''' find the ribbon that covers square (x, y) '''
        for ribbon in self.ribbons:
            if ribbon.contains(x,y):
                return ribbon
        return None
    
        
    def flip(self, i, j): 
        ''' flip tiles number i and number j and returns true, if possible,
        do nothing and returns false if not possible.
        
        Parameters
        --------------
        i, j: integers 
            the indices of ribbons to flip
        
        Returns:
            True if successful
            False if impossible
        '''
        
        A = self.ribbons[i]
        B = self.ribbons[j] 
        #print(A)
        #print(B)
        flag, A1, B1 = A.flip(B)
        #print(A1)
        #print(B1)
        if flag:
            self.ribbons[i] = A1
            self.ribbons[j] = B1
        return flag
          
        
    def __str__(self):
        ''' Returns a string representation of this tiling
        return the graph'''
        s = ''
        for ribbon in self.ribbons:
            s = s + '\n' + str(ribbon)
        return s 
    
    def draw(self, M, N, ax = None, 
                colormap = 'prism', colorType = "Shape",
                offset = [0, 0],
                MaxLength = None,
                block = False):
        ''' draw the tiling 
        Parameters
        --------------
        M, N : integers 
            the height and the width of the plot 
        ax : matplotlib axis
            axis in which to draw (default = None)
        colormap : 'prism' 
            the name of the coloring scheme ("palette"), used to color the tiling,
            default = "prism"
            other possibilities: "jet"and many others, see matplotlib docs.
        colorType : string
            defines the type of coloring. Possible choices:
            "Shape" -- color only depends on shape
            "ShapePosition" -- color depends on shape and level (mod n)
            "Length" -- color only depends on length of the ribbon
            (default = "Shape")
        offset: a list of two integers
            sets the origin of the axis at 0 - offset[0], 0 - offset[1]
            (default = [0, 0])
        MaxLength : integer 
            a fine-tuning parameter used in the choice of coloring (default = None)
        block: boolean
            if True, stops the execution and draws the graph (default = False)
        
        
        
        '''
        if (ax == None):
            fig, ax = plt.subplots()
        else:
            fig = ax.figure
            
        ax.set_xlim(0 - offset[0], N)
        ax.set_xticks(list(range(-offset[0],N)))
        ax.set_ylim(0 - offset[1], M)
        ax.set_yticks(list(range(-offset[1], M)))
        
        if MaxLength == None:
            if colorType == "Length":
                MN = 3 * int(np.log2(max([M, N])))
            else:
                MN = None #Let the ribbon itself decide what color to choose
                        #based on position and on the length
        else:
            MN = MaxLength
        #print(MN)
        for ribbon in self.ribbons:
            ribbon.draw(ax, MaxLength = MN, colorType = colorType,
                        colormap = colormap)
        
        #ax.grid()
        if block:            
            plt.show()
        else:
            plt.draw()
        return fig, ax


def fromString(s):
    '''
    initializes a tiling from a string like the following
    '(0,0), [1, 1]
    (2,1), [1, 0]
    (1,0), [1, 1]'
     '''
    #TODO
    pass

def standardAztec2(M):
    '''
    generate a standard tiling of an M-by-M Aztec Diamond by dominos
    '''
    ribbons = []
    
    for i in range(M): #the first half of the diamond
        for j in range(M - i): 
            ribbon = rb.Ribbon(i + j, i - j, [1])
            ribbons.append(ribbon)
    
    for i in range(M): #the second half of the diamond
        for j in range(i + 1): 
            ribbon = rb.Ribbon(M + j , - M + 2 * i - j + 1, [1])
            ribbons.append(ribbon)
            #print(str(ribbon))
    t = Tiling(ribbons)
    return t
    

def standardT(n, M, N = None):
    '''
    generate a standard tiling of Mn - by - N rectangle (Mn - height,
    N - width)
    by vertical n-ribbons. If N = None, returns a square 
    with side M * n
    '''
    if N == None:
        N = n * M 
        
    ribbons = []
    #This should be changed. we need to add ribbons in standard order. 
    levels, vertex2level = _getHelpersRect(n, M, N)
    #print("vertex2level = ", vertex2level)
    for v, level in enumerate(vertex2level):
        position = levels[level].index(v)
        if level < M * n:
            #print("v = ", v, " level = ", level)
            #print("position = ", position)
            x = position * n + level % n
            y = level - x 
            #print("x = ", x, " y = ", y)
            ribbon = rb.Ribbon(x, y, [1] * (n - 1))
            ribbons.append(ribbon)
        else:
            x = position * n + level - (M - 1) * n
            y = level - x 
            ribbon = rb.Ribbon(x, y, [1] * (n - 1))
            ribbons.append(ribbon)
    t = Tiling(ribbons)
    return t

def randomT(n, M, N, ITER = 10, seed = None):
    '''
    generate a random tiling of Mn - by - N rectangle (Mn - height,
    N - width)
    by using a version of Markov Chain algorithm with flips
    
    Parameters
    ------------
    n: integer
        length of tile
    M, N: integers
        The region is Mn - by - N rectangle
    ITER: integer
        parameter that determines how long to run the algorithm
        typically every tile is touched around ITER times
    seed: integer
        the seed of the random generator, for reproducibility,
        default = None
    
    Returns
    ------------
    random ribbon tiling
    
    '''
    #There are some errors 
    
    if (seed != None):
        np.random.seed(seed)
    else:
        np.random.seed()
        
    t = standardT(n, M, N)
    V = len(t.ribbons)
    #for v in range(V):
    #    print(t.ribbons[v])
    helpers = _getHelpersRect(n, M, N)
    #print("Herlpers =", helpers)
    for count in range(ITER):
        for v in range(V):
            #print("v = ", v)
            flips = ut.findFlips(n, v, t, helpers)
            if len(flips) > 0:
                i = np.random.randint(len(flips))
                w = flips[i]
                #print("w = ", w)                
                t.flip(v,w)
    return t

def _getHelpersRect(n, M, N):
    '''
    create helper structures for a rectangle with number of rows M * N 
    and number of columns N
    
    (In this version I do not create a digraph.)
    
    The vertices are arranged in layers according to the level and ordered 
    inside the layer. 
    
    Parameters
    -------------
    n: integer
       the size of the ribbon
    M: integer
       determines the number of rows(the actual size is M * n)
    N: integer 
        the number of columns
       
    Returns
    --------------
    (levels, level_lengths, integer2level) where
       
    levels: a list of integer lists
          every inside list represents vertices in the level
    
    integer2level: a list of integers
            the k-th element is the level of vertex k.
       
    
    '''
    
    #digraph = dgr.Digraph(M * N * n)
    levels = []
    #create a list of levels
    nlevels = (M - 1) * n + N
    level_lengths = [0] * nlevels
    
    #make an auxiliary tiling
    ribbons = []
    for i in range(N):
        for j in range(M):
            ribbon = rb.Ribbon(i, j*n, [1] * (n - 1))
            ribbons.append(ribbon)
    st = Tiling(ribbons)
    #print(len(ribbons))
    #print("Auxiliary = ", st)
    
    for ribbon in st.ribbons:
        l = ribbon.level()
        level_lengths[l] += 1
    #print(level_lengths)
    x = 0
    for l in range(nlevels):
        level = list(range(x, x + level_lengths[l]))
        levels.append(level)
        x = x + level_lengths[l]
    #print(levels)

    vertex2level = [-1] * M * N                    
    for l in range(nlevels):
        for i in range(level_lengths[l]):
            vertex2level[levels[l][i]] = l 
         
    return levels, vertex2level


def _getHelpers(n, M):
    '''
    create a generic digraph of a tiling for a square
    with side M * n and other helper structures
    
    The generic means that only the forced edges are included.
    (and not all of them, only those that generate the structure of the graph)
    in particular, those between vertices in the same level are not included.
    
    The vertices are arranged in layers according to the level and ordered 
    inside the layer. 
    
    Parameters
    -------------
    n: integer
       the size of the ribbon
    M: integer
       the size of the square side (actual size is M * n)
       
    Returns
    --------------
    (digraph, levels, level_lengths, integer2level) where
    
    digraph : itu.algs4.Digraph 
        digraph of the tiling where only forced edges are included
        NOTE: I use the convention from Yinsong's algorithm, v -> w 
        if w is on the right of v
    
    levels: a list of integer lists
          every inside list represents vertices in the level
          
    level_lengths: list of integers
        the length of each level
    
    integer2level: a list of integers
            the k-th element is the level of vertex k.
       
    
    '''
    N = M 
    
    digraph = dgr.Digraph(M * N * n)
    levels = []
    #create a list of levels
    st = standardT(n, M)
    nlevels = (N + M - 1) * n
    level_lengths = [0] * nlevels
    for ribbon in st.ribbons:
        l = ribbon.level()
        level_lengths[l] += 1
    #print(level_lengths)
    x = 0
    for l in range(nlevels):
        level = list(range(x, x + level_lengths[l]))
        levels.append(level)
        x = x + level_lengths[l]
    #print(levels)
    #Now we want make a digraph
    for l in range(nlevels):
        level = levels[l]
        for i, v in enumerate(level): 
            if l < (M - 1) * n: #lower levels
                if l < n:
                    w = levels[l + n][i + 1]
                    digraph.add_edge(v, w)
                else:
                    if i + 1 < level_lengths[l + n]:
                        w = levels[l + n][i + 1]
                        digraph.add_edge(v, w)
                    if i < level_lengths[l - n]:
                        #print("v = ", v, "i = ", i, "l = ", l)
                        w = levels[l - n][i]
                        digraph.add_edge(v, w)
            elif l < M * n: #middle level
                    if i < level_lengths[l + n]:
                        w = levels[l + n][i]
                        #print("v = ", v, "i = ", i, "l = ", l, "w = ", w)
                        digraph.add_edge(v, w)
                    if i < level_lengths[l - n]:
                        #print("v = ", v, "i = ", i, "l = ", l)
                        w = levels[l - n][i]
                        digraph.add_edge(v, w)
            else: #upper levels
                if l >= nlevels - n:
                    w = levels[l - n][i + 1]
                    digraph.add_edge(v, w)
                else:
                    if i + 1 < level_lengths[l - n]:
                        w = levels[l - n][i + 1]
                        digraph.add_edge(v, w)
                    if i < level_lengths[l + n]:
                        #print("v = ", v, "i = ", i, "l = ", l)
                        w = levels[l + n][i]
                        digraph.add_edge(v, w)   
    vertex2level = [-1] * M * N * n                    
    for l in range(nlevels):
        for i in range(level_lengths[l]):
            vertex2level[levels[l][i]] = l 
         
    return digraph, levels, level_lengths, vertex2level

def buildFromTilingSeq(seq, n, M):
    '''build a tiling of a rectangle from a tiling sequence
    
    Parameters
    -----------
    seq: a list of integers, 
    represents the permutation of tiles/graph vertices [0, len(seq) - 1]
    which induces an acyclic orientation on graph in agreement 
    with the forced partial orientation. 
    
    n: integer
       the size of the ribbon
    M: integer
       the size of the square side (actual size is M * n)
    
    Returns: a tiling 
    '''
    (_, levels, _, vertex2level) = _getHelpers(n,M)
    
    ribbons = []
    
    for i, v in enumerate(seq): #for every vertex build a tile
        #print("v = ", v)
        squares = []
        l = vertex2level[v]
        for lt in range(l, l+n): #for every level of the tile
            #print("lt = ", lt)
            #count the number of vertices which are comparable
            #and precede v in the sequence
            counter = 0
            for j in range(lt - n + 1, lt + 1): #comparable levels
                if j >= 0 and j < len(levels):
                    #print("j = ", j)
                    for w in levels[j]:
                        if w in seq and seq.index(w) < i:
                            #print("w = ", w)
                            counter += 1
            #print("counter = ", counter)               
            if (lt < M * n):                
                square = (counter, lt - counter)               
            else:
                square = (counter + lt - M * n + 1, M * n - counter - 1)
            #print("square = ", square)
            squares.append(square)
        #print(squares)
        ribbon = rb.squares2ribbon(squares)
        ribbons.append(ribbon)
    tiling = Tiling(ribbons)
    return tiling


def makeRandomTS(n, M):
    '''create a random tiling sequence for a square with the
    side n * M
    
    The tiling sequence is build using Yinsong Chen's algorithm. 
    It is NOT uniform on the space of all tiling sequences. 
    
    Parameters
    -----------
    n: integer
       the size of the ribbon
    M: integer
       the size of the square side (actual size is M * n)
       
    Returns 
    -------
    
    tiling sequence: integer array
        this sequence can be used to create 
        a tiling using buildFromTilingSequence
    
    '''
    
    (digraph, _, _, vertex2level) = _getHelpers(n,M)
    #initiate a sequence
    rev_digraph = digraph.reverse()
    ts = list(np.random.permutation(n))
    #print(ts)
    
    num_vertices = M * M * n
    for v in range(n, num_vertices):
        #print("v = ", v)
        #find bounds from the level below
        lb = -1
        ub = num_vertices
        for w in digraph.adj(v):
            if vertex2level[w] == vertex2level[v] - n:
                ub = w
        for w in rev_digraph.adj(v):
            if vertex2level[w] == vertex2level[v] - n:
                lb = w 
        #print(f'(lb, ub) = ({lb}, {ub})')
        #find the positions of all the points 
        #in the sequence which are between the bounds and
        #are comparable with v (the list can be empty)
        l_index = -1 #location of lower bound
        u_index = len(ts) #location of upper bound vertex
        positions = []
        if lb in ts:
            l_index = ts.index(lb)
        if ub in ts:
            u_index = ts.index(ub)
        #print(f'(l_index, u_index) = ({l_index}, {u_index})')
        for i in range(l_index + 1, u_index):
            x = ts[i]
            if vertex2level[x] > vertex2level[v] - n:
                positions.append(i)
        #print("positions = ", positions)
        if len(positions) == 0:
            ts.insert(l_index + 1, v)
        else:
            j = np.random.randint(len(positions) + 1)
            #print("j = ", j)
            if j < len(positions):
                ts.insert(positions[j], v)
            else:
                ts.insert(positions[-1] + 1, v)  #insert after the 
                                                #last one in positions
        #print("ts = ", ts)                                         
    return ts

def _getHelpersAztec2(M):
    '''
    create a generic digraph of a domino tiling for an Aztec
    Diamond with side M and other helper structures.
    
    
    The generic means that only the forced edges are included.
    (and not all of them, only those that generate the structure of the graph)
    in particular, those between vertices in the same level are not included,
    except perhaps for the first level
    
    The vertices are arranged in layers according to the level and ordered 
    inside the layer. 
    
    Parameters
    -------------
    M: integer
       the size of the square side (actual size is M * n)
       
    Returns
    --------------
    (digraph, levels, level_lengths, integer2level) where
    
    digraph : itu.algs4.Digraph 
        digraph of the tiling where only forced edges are included
        NOTE: I use the convention from Yinsong's algorithm, v -> w 
        if w is on the right of v
    
    levels: a list of integer lists
          every inside list represents vertices in the level
          
    level_lengths: list of integers
        the length of each level
    
    integer2level: a list of integers
            the k-th element is the level of vertex k.
       
    
    '''
    digraph = dgr.Digraph(M * (M + 1))
    levels = []
    #create a list of levels
    az = standardAztec2(M)
    nlevels = 2 * M
    level_lengths = [0] * nlevels 
    for ribbon in az.ribbons:
        l = ribbon.level()
        #print("l = ", l)
        level_lengths[l] += 1
    #print(level_lengths)
    x = 0
    for l in range(nlevels):
        level = list(range(x, x + level_lengths[l]))
        levels.append(level)
        x = x + level_lengths[l]
    #print(levels)
    #building digraph
    #first, we go along all vertices in even levels (except the last one)
    for l in range(0, 2 * (M - 1), 2):
        for i in range(level_lengths[l]):
            v = levels[l][i]
            if i > 0 and i < level_lengths[l] - 1:
                #print("l = ", l, "i = ", i)
                #print(levels[l + 2])
                w1 = levels[l + 2][i - 1]
                w2 = levels[l + 2][i]
                #digraph.add_edge(v,w1)
                #digraph.add_edge(w2,v)
                digraph.add_edge(v,w2)
                digraph.add_edge(w1,v)
            elif i == 0:
                w2 = levels[l + 2][i]
                #digraph.add_edge(w2,v)
                digraph.add_edge(v, w2)
            else:
                w1 = levels[l + 2][i - 1]
                #digraph.add_edge(v,w1)
                digraph.add_edge(w1,v)
        #additional adjustment for level 0
        #if l == 0:
        #    for i in range(1, level_lengths[l]):
        #        digraph.add_edge(i - 1, i)
                
    #second, we will go along the odd levels (except the last one)
    for l in range(1, 2 * (M - 1), 2):
        for i in range(level_lengths[l]):
            v = levels[l][i]
            #print("l = ", l, "i = ", i)
            #print(levels[l + 2])
            w1 = levels[l + 2][i]
            w2 = levels[l + 2][i + 1]
            #digraph.add_edge(v,w1)
            #digraph.add_edge(w2,v)
            digraph.add_edge(v, w2)
            digraph.add_edge(w1,v)
    #print(digraph)
    vertex2level = [-1] * M * (M + 1)                  
    for l in range(nlevels):
        for i in range(level_lengths[l]):
            vertex2level[levels[l][i]] = l 
    #print(vertex2level)
    return digraph, levels, level_lengths, vertex2level

def buildAztec2FromTilingSeq(seq, M):
    '''build a domino tiling of an Aztec diamond  from a tiling sequence
    
    Parameters
    -----------
    seq: a list of integers, 
    represents the permutation of tiles/graph vertices [0, len(seq) - 1]
    which induces an acyclic orientation on graph in agreement 
    with the forced partial orientation. 

    M: integer
       the size of the Aztec diamond 
    
    Returns: a tiling 
    '''
    #TODO (smth not OK)
    (_, levels, _, vertex2level) = _getHelpersAztec2(M)
    
    ribbons = []
    n = 2 #we are working with dominos
    for i, v in enumerate(seq): #for every vertex build a tile
        #print("v = ", v)
        squares = []
        l = vertex2level[v]
        for lt in range(l, l+n): #for every level of the tile
            #print("lt = ", lt)
            #count the number of vertices which are comparable
            #and precede v in the sequence
            counter = 0
            for j in range(lt - n + 1, lt + 1): #comparable levels
                if j >= 0 and j < len(levels):
                    #print("j = ", j)
                    for w in levels[j]:
                        if w in seq and seq.index(w) < i:
                            #print("w = ", w)
                            counter += 1
            #print("counter = ", counter)
            if lt < 2 * M: 
                square = (lt//2 + counter, lt - (lt//2 + counter))   
            else:
                square = (l//2 + counter + 1, lt - (l//2 + counter + 1))   
            # we should work with odd and even l separately
            #if l % 2 == 0:
            #    square = (l//2 + counter, lt - (l//2 + counter))
            #else: 
            #    square = (l//2 + counter, lt - (l//2 + counter))
            #print("square = ", square)
            squares.append(square)
        #print(squares)
        ribbon = rb.squares2ribbon(squares)
        ribbons.append(ribbon)
    tiling = Tiling(ribbons)
    return tiling

def makeRandomTS_Aztec2(M):
    '''create a random domino tiling sequence for an Aztec Diamond with the
    side M
    
    Parameters
    -----------
    M: integer
       the size of the Aztec Diamond side 
       
    Returns 
    -------
    
    tiling sequence: integer array
        this sequence can be used to create 
        a tiling using buildAztecFromTilingSeq
    
    '''
    #the specific 
    (digraph, _, _, vertex2level) = _getHelpersAztec2(M)
    #initiate a sequence
    rev_digraph = digraph.reverse()
    ts = list(range(M))
    #print(ts)
    
    num_vertices = digraph.V()
    n = 2
    for v in range(M, num_vertices):
        #print("v = ", v)
        #find bounds from the level below
        lb = -1 #default values for upper and lower bounds
        ub = num_vertices
        for w in digraph.adj(v):
            if vertex2level[w] == vertex2level[v] - n:
                ub = w
        for w in rev_digraph.adj(v):
            if vertex2level[w] == vertex2level[v] - n:
                lb = w 
        #print(f'(lb, ub) = ({lb}, {ub})')
        #find the positions of all the points 
        #in the sequence which are between the bounds and
        #are comparable with v (the list can be empty)
        l_index = -1 #location of lower bound
        u_index = len(ts) #location of upper bound vertex
        positions = []
        if lb in ts:
            l_index = ts.index(lb)
        if ub in ts:
            u_index = ts.index(ub)
        #print(f'(l_index, u_index) = ({l_index}, {u_index})')
        for i in range(l_index + 1, u_index):
            x = ts[i]
            if vertex2level[x] > vertex2level[v] - n:
                positions.append(i)
        #print("positions = ", positions)
        if len(positions) == 0:
            ts.insert(l_index + 1, v)
        else:
            j = np.random.randint(len(positions) + 1)
            #print("j = ", j)
            if j < len(positions):
                ts.insert(positions[j], v)
            else:
                ts.insert(positions[-1] + 1, v)  #insert after the 
                                                #last one in positions
        #print("ts = ", ts)                                         
    return ts



'''
For testing methods
'''
def main():
    print('Ribbon tiling methods are used')  
    
    ''' testing basic construction '''
    '''
    ribbon1 = rb.Ribbon(0, 0, [0, 1])
    ribbon2 = rb.Ribbon(0, 1, [1, 0])
    
    tiling = Tiling([ribbon1, ribbon2]) 
    _, ax1 = plt.subplots()
    print(tiling)
    tiling.draw(10, 10, ax = ax1, MaxLength = 3, 
                colorByLength = False, colormap = "prism")
    '''
    
    
    A = rb.Ribbon(0, 0, [0, 0, 0, 1, 1, 0, 0, 1])
    B = rb.Ribbon(2, 1, [1, 1, 0, 0, 1, 0, 0, 0])
    
    tiling = Tiling([A, B]) 
    print(tiling)

    '''
    (0,0), [1, 1]
    (2,1), [1, 0]
    (1,0), [1, 1]
    (1,3), [1, 1]
    (2,0), [0, 1]
    (2,4), [1, 0]
    (0,3), [1, 1]
    (2,3), [0, 1]
     '''   
    
    '''testing building a standard tiling'''
    
    n = 3
    M = 2
    N = 3
    #t = standardT(n, M, N)
    #print(t)
    _, ax2 = plt.subplots(1,1)
    #t.draw(M * n, N, ax = ax2)
    
    #let us look at some helper structures
    '''
    levels, vertex2level = _getHelpersRect(n, M, N)
    print(levels)
    print(vertex2level)
    '''
    
    '''testing building a random tiling'''
    n = 5
    M = 1
    N = 30
    helpers = _getHelpersRect(n, M, N)
    t = randomT(n, M, N, ITER = 100)
    #print(t)
    t.draw(M * n, N, ax = ax2)
    flips = ut.findFlips(n, 4, t, helpers)
    
    A = t.ribbons[4]
    print("A = ", A)
    print(flips)
    #B = t.ribbons[5]
    #(flag, C, D)= A.flip(B)
    #print(flag)
    #_, ax = A.draw()
    #B.draw(ax = ax)
    #print(flips)
    
    
    
    #t.flip(4,5)
    #t.draw(M * n, N, ax = ax2[1])
    
    '''
    Testing Yinsong's algorithm for the random generation of a rectangle tiling
    '''
    '''
    n = 3
    M = 3
    digraph, levels, level_lengths, vertex2level = getHelpers(n, M)
    
    print(digraph)
    print(level_lengths)
    print(levels)
    print(vertex2level)
    
    #seq = [2, 1, 0]
    #seq = [1, 2, 0]
    #seq = [7, 2, 5, 3, 0, 1, 4, 6]
    #num_vertices = M * M * n
    #seq = list(range(3, -1, -1))
    #print(seq)
    seq = [5, 7, 3, 1, 0, 2, 9, 10, 11, 6, 4, 8]
    tiling = buildFromTilingSeq(seq, n, M)
    tiling.draw(M * n, M * n)
    
    
    ts = makeRandomTS(n, M)
    tiling = buildFromTilingSeq(ts, n, M)
    tiling.draw(M * n, M * n)
    '''
    
    
    '''
    Testing Yinsong's algorithm for the random generation of
     an Aztec Diamond tiling. Here it is clear that the tiling is not 
     sampled from the uniform distribution. 
    '''
    
    '''
    M = 4
    t = standardAztec2(M)
    t.draw(M + 2, 2 * M, offset = (0, M))
    '''
    
    '''
    #getHelpersAztec2(M)
    M = 40
    #seq = [0, 4, 1, 9, 8, 6, 5, 3, 2, 10, 7, 11]
    #seq = [0, 4, 9, 6, 3, 1, 10, 7, 11, 8, 5, 2]
    #seq =  [19, 14, 18, 3, 1, 9, 13, 7, 5, 0, 4, 2, 8, 11, 15, 17, 6, 10, 12, 16]
    seq = makeRandomTS_Aztec2(M)
    print("seq = ", seq)
    tiling = buildAztec2FromTilingSeq(seq, M)
    #print("tiling = ", tiling)
    tiling.draw(M + 2, 2 * M + 1, offset = (1, M))
    
    #1) is it possible that 3 is before 0 in tiling with M = 3?
    '''

    
    
    
    plt.show()
    
    
    
if __name__ == "__main__":
    main() 