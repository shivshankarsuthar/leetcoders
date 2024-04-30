import math
def mypow(x,n,m):
    y = 1
    while n != 0:
        if n & 1:
            y = (y * x) % m
        x = (x * x) % m
        n = n // 2
    return y
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        y = 5 if n & 1 else 1
        return (mypow(20,n//2,10 ** 9 + 7) * y) % (10 ** 9 + 7)

    
print(Solution().countGoodNumbers(806166225460393))