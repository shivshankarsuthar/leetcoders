from typing import List

def swapNumber(a:list,  b: list) -> None:
    # write your code here
    a = a ^ b
    b = a ^ b
    a = a ^ b