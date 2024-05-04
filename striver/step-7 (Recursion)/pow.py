
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        y = 1
        while n != 0:
            if n & 1:
                y *= x
            x = x * x
            n = n // 2
        return y
        
print(Solution().myPow(2,-5))