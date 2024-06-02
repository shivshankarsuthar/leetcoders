from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        n = len(asteroids)
        for i in range(n):
            if asteroids[i] > 0 or len(stack) == 0:
                stack.append(asteroids[i])
            else:
                while len(stack) > 0 and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()
                if len(stack) > 0 and stack[-1] == abs(asteroids[i]):
                    stack.pop()
                else:
                    if len(stack) == 0 or stack[-1] < 0:
                        stack.append(asteroids[i])

        return stack
    
print(Solution().asteroidCollision([-2,-2,1,-2]))