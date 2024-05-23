def pow(x,n,ans):
    if n == 1:
        return x * ans
    
    if n & 1:
        return pow(x*x,n//2,ans*x)
    else:
        return pow(x*x,n//2,ans)

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1/x
            n = -n
        return pow(x,n,1)

print(Solution().myPow(2,-3))
