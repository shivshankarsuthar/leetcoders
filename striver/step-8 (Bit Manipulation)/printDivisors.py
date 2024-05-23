class Solution:
    def print_divisors(self, N):
        result = []
        for i in range(1,N+1):
            if N % i == 0:
                result.append(i)
        return result
    
print(Solution().print_divisors(1))