from sys import *
from collections import *
from math import *

def largestElement(arr: [], l,r) -> int:
    if l >= r:
        return
    m = (l+r)//2
    largestElement(arr,l,m)
    largestElement(arr,m+1,r)
    maximum = max(arr[l:r+1])
    return maximum

def largestElement2(arr,n,maximum):
    if n == 1:
        return arr[n]
    maximum = max(arr[n],largestElement2(arr,n-1,maximum))
    return maximum

print(largestElement([1,5,23,17,3,86,24,4],0,7))
print(largestElement2([1,5,23,17,3,86,24,4],7,-1))
