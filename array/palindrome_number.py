class Solution:
    def isPalindrome(self, x: int) -> bool:
        new_number:int = 0
        old_number = x
        if x < 0:
            return False
        while x != 0:
            last_digit = x % 10
            new_number = new_number * 10 + last_digit
            x = x // 10
        return new_number == old_number
    
result = Solution().isPalindrome(2112)
print(result)