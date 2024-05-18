from os import *
from sys import *
from collections import *
from math import *

def rowMaxOnes(mat, n, m):
    # Write your code here.
    minimum = 10000000000000
    minIndex = -1
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                if j == 0:
                    return i 
                if j < minimum:
                    minIndex = i
                    minimum = min(minimum,j)
    return minIndex
                
print(rowMaxOnes([[1, 1, 1], [0, 0, 1], [0, 0, 0]],3,3))