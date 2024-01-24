class Solution:
    def reverse(self, x: int) -> int:        
        reversedInt = 0
        temp = abs(x)
        while temp != 0:
            reversedInt = temp % 10 + reversedInt * 10
            temp //= 10
        reversedInt = -reversedInt if x < 0 else reversedInt
        return reversedInt
    
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        return self.reverse(x) == x
    
print(Solution().isPalindrome(-121))