from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return (nums + nums)


result = Solution().getConcatenation([1,2,3,4])
print(result)


# DOne in 5mins