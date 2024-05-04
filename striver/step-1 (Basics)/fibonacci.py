class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        previous = 0
        current = 1
        next = 1
        for step in range(n-1):
            next = previous + current
            previous = current
            current = next

        return next
    
    def regressionFib(self,n:int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        return self.regressionFib(n-1) + self.regressionFib(n-2)
    
print(Solution().fib(10))
print(Solution().regressionFib(10))