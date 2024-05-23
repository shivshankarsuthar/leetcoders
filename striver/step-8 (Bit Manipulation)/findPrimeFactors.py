class Solution:
    def sieve(self):
      pass

    def findPrimeFactors(self, N):
        result = []
        i = 2
        while N != 1:
            if N % i == 0:
                result.append(i)
                N = N // i
            else:
                i += 1
        return result
    
print(Solution().findPrimeFactors(36))