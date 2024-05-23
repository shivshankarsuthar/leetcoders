from typing import *

def setBits(N : int) -> int:
    # Write your code here.
    i = 0
    n = N
    while n % 2 != 0:
        n = n // 2
        if n == 0:
            return N
        i += 1
    return N | (1 << i)

print(setBits(10))