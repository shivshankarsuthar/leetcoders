class Solution:
    def reverse(self, x: int) -> int:        
        reversedInt = 0
        temp = abs(x)
        while temp != 0:
            reversedInt = temp % 10 + reversedInt * 10
            temp //= 10
        reversedInt = -reversedInt if x < 0 else reversedInt
        if reversedInt > 2**31-1 or reversedInt <-2**31:
            return 0
        return reversedInt
    
print(Solution().reverse(123142135))