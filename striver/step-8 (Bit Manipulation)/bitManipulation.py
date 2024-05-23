from typing import *

def bitManipulation(num : int, i : int) -> List[int]:
    # Write your code here.
    i = i - 1
    firstAns = (num & (1 << i)) >> i
    secondAns = num | (1 << i)
    thirdAns = num & ~(1 << i)
    return [firstAns,secondAns,thirdAns]

print(bitManipulation(25,3))