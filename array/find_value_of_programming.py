from typing import List
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for x in operations:
            if '+' in x:
                result += 1
            elif '-' in x:
                result -= 1
        return result
    
result = Solution().finalValueAfterOperations( ["++X","++X","X++"])
print(result)