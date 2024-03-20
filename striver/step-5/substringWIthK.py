from typing import *

def countSubStrings(s: str, k: int) -> int:
    # Write your code here
    count = 0
    result = []
    for i in range(len(s)-k):
        j = i
        records = set()
        while len(records) <= k and j < len(s):
            records.add(s[j])
            j += 1
            if len(records) == k:
                result.append(s[i:j])

    return len(result)

print(countSubStrings('qffds',4))