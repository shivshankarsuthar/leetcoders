def isItEvenCoord(coord):
    if (ord(coord[0]) - ord('a')) % 2 == 0:
        return True
    return False

def isWhiteBox(coordinate):
    if (isItEvenCoord(coordinate) and int(coordinate[1]) % 2 == 0) or (not isItEvenCoord(coordinate) and not int(coordinate[1]) % 2 == 0):
        return True
    return False
        
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        if isWhiteBox(coordinate1) == isWhiteBox(coordinate2):
            return True
        return False
print(Solution().checkTwoChessboards('a1','h3'))