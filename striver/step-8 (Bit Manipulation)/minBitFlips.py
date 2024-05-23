class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        count = 0
        while goal or start:
            if goal % 2 != start % 2:
                count += 1
            goal = goal // 2
            start = start // 2
        return count
    
print(Solution().minBitFlips(10,5))