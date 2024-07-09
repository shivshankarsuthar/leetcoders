def getPowers(c):
    p1 = (-1 + (1+4*c) ** 0.5)/2
    p2 = (-1 - (1+4*c) ** 0.5)/2
    result = p1 if p1 >0 else p2
    return result

class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # blue first
        if blue < red:
            
        
print(Solution().maxHeightOfTriangle(4,6))