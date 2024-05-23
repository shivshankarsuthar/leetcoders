def isKthBitSet(n: int, k: int) -> bool:
    # Write your code from here.
    if n & (1 << (k-1)):
        return True
    return False
