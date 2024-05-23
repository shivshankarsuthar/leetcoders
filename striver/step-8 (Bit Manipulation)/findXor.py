from typing import *

def findXOR(L : int, R : int) -> int:
    # Write your code here.
    result = 0
    for i in range(L,R+1):
        result ^= i
    return result