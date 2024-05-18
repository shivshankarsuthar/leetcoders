from typing import List

def generateString(N: int) -> List[str]:
    # write your code here
    if N == 0:
        return ['']
    elif N == 1:
        return ['0','1']
    gStrings = ['0','1']
    length = 0
    result = []
    for string in gStrings:
        if len(string) > N:
            break

        if len(string) == N:
            result.append(string)
        if string[-1] == '0':
            gStrings.append(string+'0')
            gStrings.append(string+'1')
        else:
            gStrings.append(string+'0')
    
    return result

print(generateString(4))