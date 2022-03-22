import numpy as np
import math
from combineArrays import combine_arrays_v1
from combineArrays import combine_arrays_v2
from combineArrays import combine_arrays_v3

def print_test_result( y):
    print( "result: ", y)
    # Expected result: [1.00174553 0.74124027 1.20704145]
    expected_result = np.array([1.00174553, 0.74124027, 1.20704145])
    if np.array_equal( y, expected_result):
        print( "pass")
    else:
        print( "fail")
    

# columns
n = 3
#rows
m = 2
# elements 
k = n * m

# Array 1
# z = np.random.randint( 2, size=k)
# z = np.array([1, 1, 1, 1, 0, 1])
z = np.ones(k, np.intc)
z[4] = 0

# Array 2
# r = np.random.rand( k)
r = np.array([0.86404667, 0.74124027, 0.50154928, 0.13769886, 0.35504102, 0.70549217])

# Result
y = np.zeros(n, float)

# Test combining the arrays
print( "z: ", z)
print( "r: ", r)
print( "y: ", y)
print( "m: ", m)
print( "n: ", n)

# Test combine_arrays_v1()
print( "Test combine_arrays_v1()")
combine_arrays_v1( z, r, y, n, m)
print_test_result( y)


# Test combine_arrays_v2()
print( "Test combine_arrays_v2()")
y = np.zeros(n, float)
combine_arrays_v2( z, r, y, n, m)
print_test_result( y)


# Test combine_arrays_v3()
print( "Test combine_arrays_v3()")
y = np.zeros(n, float)
combine_arrays_v3( z, r, y, n, m)
print_test_result( y)


