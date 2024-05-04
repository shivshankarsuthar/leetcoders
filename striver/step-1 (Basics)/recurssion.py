from typing import List

result = []
i = 1
def printNos(x: int) -> List[int]: 
    # Write your code here
    global i
    if i > x:
        return
    result.append(i)
    i += 1
    printNos(x)
    return result

print(printNos(5))