class Solution:
    def countPrimes(self, n: int) -> int:
        nums = {}
        for i in range(2,n):
            nums[i] = True
        i = 2
        while i < n:
            if nums[i]:
                j = i
                while j*i < n:
                    nums[j*i] = False
                    j += 1
            i += 1
        count = 0
        for i in range(2,n):
            if nums[i]:
                count += 1
        return count
print(Solution().countPrimes(2))