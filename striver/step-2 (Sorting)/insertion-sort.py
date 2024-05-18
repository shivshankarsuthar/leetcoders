
import os
import sys
from copy import deepcopy
input = lambda: sys.stdin.readline().rstrip("\r\n")
sys.setrecursionlimit(10 ** 7)
def insertionSort(arr):
    # write your code here !!!
    for i in range(len(arr)-1):
        j = i + 1
        while(j > 0 and arr[j] < arr[j-1]):
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
    return arr

print(insertionSort([2,1,3,4,1,3,6,28]))