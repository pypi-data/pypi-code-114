class ai:
    
    def bfs(self):
        print("""
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = [] # List for visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0) 
    print (m, end = " ") 

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')    # function calling
""")

    def dfs(self):
        print("""
graph = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = set() # Set to keep track of visited nodes of graph.

def dfs(visited, graph, node):  #function for dfs 
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
print("Following is the Depth-First Search")
dfs(visited, graph, '5')    """)
    
    
    def tictactoe(self):
        print("""
# Tic-Tac-Toe Program using
# random number in Python

# importing all necessary libraries
import numpy as np
import random
from time import sleep

# Creates an empty board
def create_board():
	return(np.array([[0, 0, 0],
					[0, 0, 0],
					[0, 0, 0]]))

# Check for empty places on board
def possibilities(board):
	l = []
	
	for i in range(len(board)):
		for j in range(len(board)):
			
			if board[i][j] == 0:
				l.append((i, j))
	return(l)

# Select a random place for the player
def random_place(board, player):
	selection = possibilities(board)
	current_loc = random.choice(selection)
	board[current_loc] = player
	return(board)

# Checks whether the player has three
# of their marks in a horizontal row
def row_win(board, player):
	for x in range(len(board)):
		win = True
		
		for y in range(len(board)):
			if board[x, y] != player:
				win = False
				continue
				
		if win == True:
			return(win)
	return(win)

# Checks whether the player has three
# of their marks in a vertical row
def col_win(board, player):
	for x in range(len(board)):
		win = True
		
		for y in range(len(board)):
			if board[y][x] != player:
				win = False
				continue
				
		if win == True:
			return(win)
	return(win)

# Checks whether the player has three
# of their marks in a diagonal row
def diag_win(board, player):
	win = True
	y = 0
	for x in range(len(board)):
		if board[x, x] != player:
			win = False
	if win:
		return win
	win = True
	if win:
		for x in range(len(board)):
			y = len(board) - 1 - x
			if board[x, y] != player:
				win = False
	return win

# Evaluates whether there is
# a winner or a tie
def evaluate(board):
	winner = 0
	
	for player in [1, 2]:
		if (row_win(board, player) or
			col_win(board,player) or
			diag_win(board,player)):
				
			winner = player
			
	if np.all(board != 0) and winner == 0:
		winner = -1
	return winner

# Main function to start the game
def play_game():
	board, winner, counter = create_board(), 0, 1
	print(board)
	sleep(2)
	
	while winner == 0:
		for player in [1, 2]:
			board = random_place(board, player)
			print("Board after " + str(counter) + " move")
			print(board)
			sleep(2)
			counter += 1
			winner = evaluate(board)
			if winner != 0:
				break
	return(winner)

# Driver Code
print("Winner is: " + str(play_game()))

""")


    def eightpuzzleproblem(self):
        print("""
# Python3 program to print the path from root
# node to destination node for N*N-1 puzzle
# algorithm using Branch and Bound
# The solution assumes that instance of
# puzzle is solvable

# Importing copy for deepcopy function
import copy

# Importing the heap functions from python
# library for Priority Queue
from heapq import heappush, heappop

# This variable can be changed to change
# the program from 8 puzzle(n=3) to 15
# puzzle(n=4) to 24 puzzle(n=5)...
n = 3

# bottom, left, top, right
row = [ 1, 0, -1, 0 ]
col = [ 0, -1, 0, 1 ]

# A class for Priority Queue
class priorityQueue:
	
	# Constructor to initialize a
	# Priority Queue
	def __init__(self):
		self.heap = []

	# Inserts a new key 'k'
	def push(self, k):
		heappush(self.heap, k)

	# Method to remove minimum element
	# from Priority Queue
	def pop(self):
		return heappop(self.heap)

	# Method to know if the Queue is empty
	def empty(self):
		if not self.heap:
			return True
		else:
			return False

# Node structure
class node:
	
	def __init__(self, parent, mat, empty_tile_pos,
				cost, level):
					
		# Stores the parent node of the
		# current node helps in tracing
		# path when the answer is found
		self.parent = parent

		# Stores the matrix
		self.mat = mat

		# Stores the position at which the
		# empty space tile exists in the matrix
		self.empty_tile_pos = empty_tile_pos

		# Storesthe number of misplaced tiles
		self.cost = cost

		# Stores the number of moves so far
		self.level = level

	# This method is defined so that the
	# priority queue is formed based on
	# the cost variable of the objects
	def __lt__(self, nxt):
		return self.cost < nxt.cost

# Function to calculate the number of
# misplaced tiles ie. number of non-blank
# tiles not in their goal position
def calculateCost(mat, final) -> int:
	
	count = 0
	for i in range(n):
		for j in range(n):
			if ((mat[i][j]) and
				(mat[i][j] != final[i][j])):
				count += 1
				
	return count

def newNode(mat, empty_tile_pos, new_empty_tile_pos,
			level, parent, final) -> node:
				
	# Copy data from parent matrix to current matrix
	new_mat = copy.deepcopy(mat)

	# Move tile by 1 position
	x1 = empty_tile_pos[0]
	y1 = empty_tile_pos[1]
	x2 = new_empty_tile_pos[0]
	y2 = new_empty_tile_pos[1]
	new_mat[x1][y1], new_mat[x2][y2] = new_mat[x2][y2], new_mat[x1][y1]

	# Set number of misplaced tiles
	cost = calculateCost(new_mat, final)

	new_node = node(parent, new_mat, new_empty_tile_pos,
					cost, level)
	return new_node

# Function to print the N x N matrix
def printMatrix(mat):
	
	for i in range(n):
		for j in range(n):
			print("%d " % (mat[i][j]), end = " ")
			
		print()

# Function to check if (x, y) is a valid
# matrix coordinate
def isSafe(x, y):
	
	return x >= 0 and x < n and y >= 0 and y < n

# Print path from root node to destination node
def printPath(root):
	
	if root == None:
		return
	
	printPath(root.parent)
	printMatrix(root.mat)
	print()

# Function to solve N*N - 1 puzzle algorithm
# using Branch and Bound. empty_tile_pos is
# the blank tile position in the initial state.
def solve(initial, empty_tile_pos, final):
	
	# Create a priority queue to store live
	# nodes of search tree
	pq = priorityQueue()

	# Create the root node
	cost = calculateCost(initial, final)
	root = node(None, initial,
				empty_tile_pos, cost, 0)

	# Add root to list of live nodes
	pq.push(root)

	# Finds a live node with least cost,
	# add its children to list of live
	# nodes and finally deletes it from
	# the list.
	while not pq.empty():

		# Find a live node with least estimated
		# cost and delete it form the list of
		# live nodes
		minimum = pq.pop()

		# If minimum is the answer node
		if minimum.cost == 0:
			
			# Print the path from root to
			# destination;
			printPath(minimum)
			return

		# Generate all possible children
		for i in range(n):
			new_tile_pos = [
				minimum.empty_tile_pos[0] + row[i],
				minimum.empty_tile_pos[1] + col[i], ]
				
			if isSafe(new_tile_pos[0], new_tile_pos[1]):
				
				# Create a child node
				child = newNode(minimum.mat,
								minimum.empty_tile_pos,
								new_tile_pos,
								minimum.level + 1,
								minimum, final,)

				# Add child to list of live nodes
				pq.push(child)

# Driver Code

# Initial configuration
# Value 0 is used for empty space
initial = [ [ 1, 2, 3 ],
			[ 5, 6, 0 ],
			[ 7, 8, 4 ] ]

# Solvable Final configuration
# Value 0 is used for empty space
final = [ [ 1, 2, 3 ],
		[ 5, 8, 6 ],
		[ 0, 7, 4 ] ]

# Blank tile coordinates in
# initial configuration
empty_tile_pos = [ 1, 2 ]

# Function call to solve the puzzle
solve(initial, empty_tile_pos, final)

""")

    def waterjug(self):
        print("""
# This function is used to initialize the
# dictionary elements with a default value.
from collections import defaultdict

# jug1 and jug2 contain the value
# for max capacity in respective jugs
# and aim is the amount of water to be measured.
jug1, jug2, aim = 4, 3, 2

# Initialize dictionary with
# default value as false.
visited = defaultdict(lambda: False)

# Recursive function which prints the
# intermediate steps to reach the final
# solution and return boolean value
# (True if solution is possible, otherwise False).
# amt1 and amt2 are the amount of water present
# in both jugs at a certain point of time.
def waterJugSolver(amt1, amt2):

	# Checks for our goal and
	# returns true if achieved.
	if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
		print(amt1, amt2)
		return True
	
	# Checks if we have already visited the
	# combination or not. If not, then it proceeds further.
	if visited[(amt1, amt2)] == False:
		print(amt1, amt2)
	
		# Changes the boolean value of
		# the combination as it is visited.
		visited[(amt1, amt2)] = True
	
		# Check for all the 6 possibilities and
		# see if a solution is found in any one of them.
		return (waterJugSolver(0, amt2) or
				waterJugSolver(amt1, 0) or
				waterJugSolver(jug1, amt2) or
				waterJugSolver(amt1, jug2) or
				waterJugSolver(amt1 + min(amt2, (jug1-amt1)),
				amt2 - min(amt2, (jug1-amt1))) or
				waterJugSolver(amt1 - min(amt1, (jug2-amt2)),
				amt2 + min(amt1, (jug2-amt2))))
	
	# Return False if the combination is
	# already visited to avoid repetition otherwise
	# recursion will enter an infinite loop.
	else:
		return False

print("Steps: ")

# Call the function and pass the
# initial amount of water present in both jugs.
waterJugSolver(0, 0)
""")

    def travellingsalesmanproblem(self):
        print("""
# Python3 program to implement traveling salesman
# problem using naive approach.
from sys import maxsize
from itertools import permutations
V = 4

# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):

	# store all vertex apart from source vertex
	vertex = []
	for i in range(V):
		if i != s:
			vertex.append(i)

	# store minimum weight Hamiltonian Cycle
	min_path = maxsize
	next_permutation=permutations(vertex)
	for i in next_permutation:

		# store current Path weight(cost)
		current_pathweight = 0

		# compute current path weight
		k = s
		for j in i:
			current_pathweight += graph[k][j]
			k = j
		current_pathweight += graph[k][s]

		# update minimum
		min_path = min(min_path, current_pathweight)
		
	return min_path


# Driver Code
if __name__ == "__main__":

	# matrix representation of graph
	graph = [[0, 10, 15, 20], [10, 0, 35, 25],
			[15, 35, 0, 30], [20, 25, 30, 0]]
	s = 0
	print(travellingSalesmanProblem(graph, s))
""")

    def towerofhanoi(self):
        print("""
# Recursive Python function to solve the tower of hanoi

def TowerOfHanoi(n , source, destination, auxiliary):
	if n==1:
		print ("Move disk 1 from source",source,"to destination",destination)
		return
	TowerOfHanoi(n-1, source, auxiliary, destination)
	print ("Move disk",n,"from source",source,"to destination",destination)
	TowerOfHanoi(n-1, auxiliary, destination, source)
		
# Driver code
n = 4
TowerOfHanoi(n,'A','B','C')
# A, C, B are the name of rods

# Contributed By Dilip Jain
""")
    def eightqueensproblem(self):
        print("""
# Taking number of queens as input from user
print ("Enter the number of queens")
N = int(input())
# here we create a chessboard
# NxN matrix with all elements set to 0
board = [[0]*N for _ in range(N)]
def attack(i, j):
    #checking vertically and horizontally
    for k in range(0,N):
        if board[i][k]==1 or board[k][j]==1:
            return True
    #checking diagonally
    for k in range(0,N):
        for l in range(0,N):
            if (k+l==i+j) or (k-l==i-j):
                if board[k][l]==1:
                    return True
    return False
def N_queens(n):
    if n==0:
        return True
    for i in range(0,N):
        for j in range(0,N):
            if (not(attack(i,j))) and (board[i][j]!=1):
                board[i][j] = 1
                if N_queens(n-1)==True:
                    return True
                board[i][j] = 0
    return False
N_queens(N)
for i in board:
    print (i)""")

    def help(self):
        print("""
Enter the following keywords to get code:
object.keyword()

KEYWORDS:-
bfs,
dfs,
tictactoe,
eightpuzzleproblem,
waterjug,
travellingsalesmanproblem,
towerofhanoi,
eightqueensproblem


Thank You ! <3"""
)
