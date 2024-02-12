from typing import *

def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    result = []
    for i in range(len(a)-1):
        found = 0
        for j in range(i+1,len(a)):
            if a[j] > a[i]:
                found = 1
                break
        if found == 0 and a[i] not in result:
            result.append(a[i])
    if a[-1] not in result:
        result.append(a[-1])

    return sorted(result)

def superiorElementsOptimised(a):
    result = []
    for i in range(len(a)-1,-1,-1):
        if len(result) == 0:
            result.append(a[i])
        elif result[-1] < a[i]:
            result.append(a[i])
    return result


print(superiorElements([142,145,41,13,41]))
print(superiorElementsOptimised([1,2,2,1]))