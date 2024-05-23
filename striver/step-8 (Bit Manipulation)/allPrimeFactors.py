#User function Template for python3
def isPrime(num):
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

class Solution:
    def AllPrimeFactors(self, N):
# Code here
        result = []
        for i in range(2,N+1):
            if N % i == 0 and isPrime(i):
                result.append(i)
        return result
    
print(Solution().AllPrimeFactors(4))