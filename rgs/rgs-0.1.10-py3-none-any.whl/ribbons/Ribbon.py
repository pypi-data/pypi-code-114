'''
Created on Jan 17, 2021

@author: vladislavkargin
'''

#import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

class Ribbon(object):
    '''
    This class realizes a ribbon tile for ribbon tilings.
    
    Ribbon is deetermined by its root square 
    s_{xy} (south-west corner is at (x, y)) and its shape:  
    a sequence of (n-1) zeros and ones. 
    0 means go right, 1 means go up. This list can be empty which will 
    corresponds to a ribbon tile that consist of a single square. 
    
    The ribbon has also attribute squares
    which is the list of squares in the ribbon.   
    '''


    def __init__(self, x, y, shape):
        '''
        creates a ribbon with root square s_{xy} (south-west corner is at (x, y))
        and a list of 0 and 1 that determines the shape.   
        Also creates a list of squares inside the ribbon. 
        '''
        self.x = x 
        self.y = y 
        self.shape = shape
        s = x
        t = y
        self.squares = [(s, t)]
        for d in shape:
            if d == 0:
                s = s + 1
                self.squares.append((s, t))
            else:
                t = t + 1
                self.squares.append((s, t))
     
    def __str__(self):
        '''
        Returns a string representation of this ribbon.
        return the graph
        '''
        s = '(' + str(self.x) + ',' + str(self.y) + '), ' + str(self.shape)
        return s   
                
    def level(self):
        ''' return the level of the ribbon '''
        return self.x + self.y
         
    def contains(self, x, y):
        ''' check if square (x, y) belong to ribbon 
        
        Parameters
        ----------
        x, y - integers
            The coordinates of the square
        Returns
        ----------
        boolean 
            true if the square is in the ribbon
        '''
        return (x, y) in self.squares
    
    def flip(self, B):
        ''' check if this ribbon can be flipped with ribbon B. If yes, returns (True, A1', B1')
        where A1', B1' is a flipped pair, if no, returns (False, A, B)
        In this version, ribbons are required to be of the same length, 
        although in principle, they can be define for ribbons of different 
        length as well
        
        Parameters
        -----------
        B: ribbon 
           required to  have the same length
        
        Returns
        ----------- 
        returns (True, A1', B1') where A1', B1' is a flipped pair, if the flip is possible;
        (False, A, B) if not possible
        
        '''
    
        n = len(self.shape) #Potential for confusion: n is NOT the size of the ribbon, it is 
                            #size of the shape. So for 3-ribbons, n = 2
        if len(B.shape)!= n:
            return (False, self, B)
        
        lA = self.x + self.y 
        lB = B.x + B.y
        if lA == lB:
            return (False, self, B) #the tiles at the same level can't be flipped
        
        if lA < lB: #we define X and Y so that X has the lower level than Y
            X = Ribbon(self.x, self.y, self.shape) 
            Y = Ribbon(B.x, B.y, B.shape)
        else:
            Y = Ribbon(self.x, self.y, self.shape) 
            X = Ribbon(B.x, B.y, B.shape)
        
        for i in range(n): #we are going along the X and checking what happens if we 
                        #change direction at certain step        
            #print("i = ", i)       
            s, t = X.squares[i]
            flag = True #if remains true after following checks then we can return a flip 
            if X.shape[i] == 0: #instead of going right, go up
                #print("First case")
                t = t + 1
                if Y.squares[0] != (s, t):
                    #print("Breaking because Y[0] != ", s, ",", t)
                    continue
                for j in range(n - i - 1): #for 3-ribbon (n = 2) and i = 0, it is only j = 0
                    #print("j = ", j)
                    if X.shape[i + j + 1] == 0:
                        s = s + 1
                    else: 
                        t = t + 1
                    #print((s,t))
                    if Y.squares[j + 1] != (s, t):
                        #print("Breaking because Y[j+1] != ", s, ",", t)
                        flag = False
                        break
                if flag and Y.shape[n - i - 1] == 0:
                    #print(i)
                    A1 = Ribbon(X.x, X.y, X.shape[:i] + [1] + X.shape[i+1:])
                    B1 = Ribbon(X.squares[i + 1][0], X.squares[i+1][1], Y.shape[:(n-i -1)] + [1] + Y.shape[(n-i):])
                    #print("first case of flippability satisfied at i = ", i)
                    #we want to make sure that the 
                    #the ribbons are returned in the correct order
                    #(without switching levels)
                    if A1.x + A1.y == self.x + self.y:
                        return (True, A1, B1)
                    else: 
                        return (True, B1, A1)
            else: #X.shape is 1, instead of going up, go right
                #print("Second case")
                s = s + 1
                if Y.squares[0] != (s, t):
                    #print("Breaking because Y[0] != ", s, ",", t)
                    continue
                for j in range(n - i - 1): #for certain amount of time, the new ribbon should go
                                           #along the squares of Y and then go up
                    #print("j = ", j)
                    if X.shape[i + j + 1] == 0:
                        s = s + 1
                    else: 
                        t = t + 1
                    #print((s,t))
                    if Y.squares[j + 1] != (s, t):
                        #print("Breaking because Y[j+1] != ", s, ",", t)
                        flag = False
                        break
                if flag and Y.shape[n - i - 1] == 1:
                    #print(i)
                    A1 = Ribbon(X.x, X.y, X.shape[:i] + [0] + X.shape[i+1:])
                    B1 = Ribbon(X.squares[i + 1][0], X.squares[i+1][1], Y.shape[:(n-i -1)] + [0] + Y.shape[(n-i):])
                    #print("second case of flippability satsified for i = ", i)
                    if A1.x + A1.y == self.x + self.y:
                        return (True, A1, B1)
                    else:
                        return (True, B1, A1)
                
        return (False, self, B)
    
    def draw(self, ax = None, 
            colormap = 'prism',
            colorType = "Shape", 
            block = False, MaxLength = None):
        '''
        draw the ribbon.
        
        Parameters:   
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
            
        MaxLength : integer 
            a fine-tuning parameter used in the choice of coloring (default = None)
        block: boolean
            if True, stops the execution and draws the graph (default = False)
        
        '''
        if (ax == None):
            fig, ax = plt.subplots()
            ax.set_xlim(0, self.x + len(self.shape) + 1)
            ax.set_ylim(0, self.y + len(self.shape) + 1)
        else:
            fig = ax.figure
        
        l = len(self.shape) # l = n - 1
        cmap = cm.get_cmap(colormap)
        if MaxLength == None:
            MaxLength = l + 2**l #this is actually not maxLength but 
                                #the max parameter for the number of 
                                #colors
        else: 
            MaxLength = max([MaxLength, l])
        
        if colorType == "Length":
            c = cmap(l/MaxLength) #for floats cmap converts interval [0,1]
                                #to the RGB range, so l should be comparable to 
                                # Maxlength
        elif colorType == "ShapePosition":
            #calculate a number that depends on the level and on 
            #the shape of the ribbon
            factor = (self.x + self.y) % (l + 1)
            i = 0
            for _, v in enumerate(self.shape):
                i = 2 * i + v 
            factor = ((factor + i) * 79) % cmap.N
            #print("Factor = ", factor)
            #print("Max Len = ", MaxLength)             
            #c = cmap(factor/MaxLength)
            c = cmap(factor) #for integers cmap converts its range 
                                    #(given by cmap.N) to RGB colors.
                                    #for prism the range is 256
        else: 
            #calculate a number that depends on 
            #the shape of the ribbon
            i = 0
            for _, v in enumerate(self.shape):
                i = 2 * i + v 
            factor = (i * 79) % cmap.N
            #print("Factor = ", factor)
            #print("Max Len = ", MaxLength)             
            #c = cmap(i/MaxLength)
            c = cmap(factor) #for integers cmap converts its range 
                                    #(given by cmap.N) to RGB colors.
            
        
        rectangle = plt.Rectangle((self.x,self.y), 1, 1, fc=c ,ec="black")
        ax.add_patch(rectangle)
        
        sx = self.x
        sy = self.y
        for i in range(len(self.shape)):
            if self.shape[i] == 0:
                rectangle = plt.Rectangle((sx,sy), 2, 1, fc=c,ec="black")
                ax.add_patch(rectangle)
                if i > 0 and self.shape[i - 1] == 0:
                    line = plt.Line2D((sx, sx),(sy, sy + 1), color = c)
                    ax.add_line(line)
                elif i > 0 and  self.shape[i - 1] == 1:
                    line = plt.Line2D((sx, sx + 1),(sy, sy), color = c)
                    ax.add_line(line) 
                sx = sx + 1 
            else:
                rectangle = plt.Rectangle((sx,sy), 1, 2, fc=c,ec="black")
                ax.add_patch(rectangle) 
                if i > 0 and self.shape[i - 1] == 0:
                    line = plt.Line2D((sx, sx),(sy, sy + 1), color = c)
                    ax.add_line(line)
                elif i > 0 and  self.shape[i - 1] == 1:
                    line = plt.Line2D((sx, sx + 1),(sy, sy), color = c)
                    ax.add_line(line) 
                sy = sy + 1
            
            
        if block:            
            plt.show()
        else:
            plt.draw()
        return fig, ax
    
    
def squares2ribbon(squares):
    ''' build a ribbon from a collection of squares.
    
    parameters
    -------------
    squares: a list of tuples (x,y)
        represent a ribbon as a collection of squares. 
        they should be in right order. (either x or y increases at each 
        step.)
    '''
    x0 = squares[0][0]
    y0 = squares[0][1]
    x = x0
    y = y0
    shape = []
    for i in range(1, len(squares)):
        if squares[i][0] - x == 1:
            shape.append(0)
            x += 1
        else: 
            shape.append(1)
            y  += 1      
    ribbon = Ribbon(x0, y0, shape)
    return ribbon
        
'''
For testing methods
'''
def main():
    print('Ribbon methods are used')  
    '''
    ribbon = Ribbon(0, 0, [0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]) 
    _, ax1 = plt.subplots()
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    print(ribbon)
    print(ribbon.squares)
    ribbon.draw(ax = ax1)
    '''
    
    '''
    checking squares to ribbon
    '''
    '''
    #squares = [(0,0), (0, 1), (1, 1)]
    squares = [(0, 2), (0, 3), (0, 4)]
    ribbon = squares2ribbon(squares)
    print(ribbon)
    _, ax2 = plt.subplots()
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ribbon.draw(ax = ax2)
    print(ribbon.contains(1, 4))
    '''
    
    ''' This is a couple of tests for the flip function 
    (seems to work OK)
    '''
    
    #a unit test 
    
    A = Ribbon(0, 0, [0, 0, 0, 1, 1, 0, 0, 1])
    B = Ribbon(2, 1, [1, 1, 0, 0, 1, 0, 0, 0])
    flag, A1, B1 = A.flip(B)
    print(flag)
    print(A1)
    print(B1)
    
    
    #some pictures
    from rgs.ribbons.Tiling import Tiling
    
    _, ax = plt.subplots(2, 2)
    
    #Case 1
    tiling = Tiling([A, B]) 
    print(tiling)
    tiling.draw(10, 10, ax = ax[0][0])
    
    if flag: 
        tiling = Tiling([A1, B1])
        tiling.draw(10, 10, ax = ax[0][1])
    
    #Case 2
    C = Ribbon(0, 0, [1, 1, 1, 1, 0])
    D = Ribbon(1, 2, [1, 0, 1, 1, 0])
    tiling = Tiling([C, D]) 
    print(tiling)
    tiling.draw(10, 10, ax = ax[1][0])
    
    flag, C1, D1 = C.flip(D)
    print(flag)
    print(C1)
    print(D1)
    if flag:
        tiling = Tiling([C1, D1])
        tiling.draw(10, 10, ax = ax[1][1])
        
    
    #simple cases
    
    #Case 3
    _, ax = plt.subplots(3, 2)
    A = Ribbon(0, 0, [0, 1])
    B = Ribbon(0, 1, [1, 0])
    
    tiling = Tiling([A, B]) 
    print(tiling)
    tiling.draw(10, 10, ax = ax[0][0])
    
    flag, A1, B1 = A.flip(B)
    print(flag)
    print(A1)
    print(B1)
    tiling = Tiling([A1, B1])
    tiling.draw(10, 10, ax = ax[0][1])
    
    
    #Case 4
    A = Ribbon(0, 0, [0, 0])
    B = Ribbon(0, 1, [0, 0])
    
    tiling = Tiling([A, B]) 
    print(tiling)
    tiling.draw(10, 10, ax = ax[1][0])
    
    flag, A1, B1 = B.flip(A)
    print(flag)
    print(A1)
    print(B1)
    tiling = Tiling([A1, B1])
    tiling.draw(10, 10, ax = ax[1][1])
    
    
    #Case 5
    A = Ribbon(0, 0, [1, 1])
    B = Ribbon(1, 0, [0, 1])
    
    tiling = Tiling([A, B]) 
    print(tiling)
    tiling.draw(10, 10, ax = ax[2][0])
    
    flag, A1, B1 = B.flip(A)
    print(flag)
    print(A1)
    print(B1)
    tiling = Tiling([A1, B1])
    tiling.draw(10, 10, ax = ax[2][1])
    
    
    
    '''
    checking the coloring scheme
    '''
    '''
    ribbon = Ribbon(0, 0, [0, 1]) 
    _, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    print(ribbon)
    print(ribbon.squares)
    ribbon.draw(ax = ax, colorByLength = False)
    
    ribbon = Ribbon(0, 0, [1, 1]) 
    _, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    print(ribbon)
    print(ribbon.squares)
    ribbon.draw(ax = ax, colorByLength = False)
    
    ribbon = Ribbon(1, 0, [1, 1]) 
    _, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    print(ribbon)
    print(ribbon.squares)
    ribbon.draw(ax = ax, colorByLength = False)
    
    ribbon = Ribbon(2, 0, [1, 1]) 
    _, ax = plt.subplots()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    print(ribbon)
    print(ribbon.squares)
    ribbon.draw(ax = ax, colorByLength = False)
    '''
    plt.show()
    
    
if __name__ == "__main__":
    main() 
    
    