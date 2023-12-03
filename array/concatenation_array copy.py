from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        for i,string in enumerate(words):
            if x in string:
                result.append(i)

        return result

result = Solution().findWordsContaining(["abc","bcd","aaaa","cbc"],'a')
print(result)


# DOne in 4 mins