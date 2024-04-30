def lengthOfSuperset(s):
    n = len(s)
    result = set()
    for i in range(2 ** n):
        seq = ''
        for j in range(n):
            if i & (1 << j):
                seq += s[j]
        result.add(seq)
    return len(result)

def moreSubsequence(n: int, m: int, a: str, b:str) -> str:
    # Write your code here.
    supersetA = lengthOfSuperset(a)
    supersetB = lengthOfSuperset(b)
    if supersetA > supersetB:
        return a
    else:
        return b
    
moreSubsequence(3,4,'abc','dddd')