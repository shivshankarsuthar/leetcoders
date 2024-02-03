from typing import *
import os
def countFrequency(n: int, m: int, edges: List[List[int]]):
    hashMap = {}
    for i in range(m+1):
        hashMap[i] = 0
    for i in range(n):
        hashMap[edges[i]] += 1
    
    return list(hashMap.values())[1:n+1]

print(countFrequency(6,9,[1,3,1,9,2,7]))