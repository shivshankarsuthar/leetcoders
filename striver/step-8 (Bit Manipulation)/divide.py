class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if (dividend == -2147483648 and divisor == -1): return 2147483647
        dividend = dividend if dividend <= (2 ** 31)-1 else (2 ** 31)-1
        divisor = divisor if divisor <= (2**31)-1 else (2**31)-1
        dividend = dividend if dividend >= -2**31 else -2**31
        divisor = divisor if divisor >= -2**31 else -2**31
        dividendSign = 1 if dividend > 0 else -1
        divisorSign = 1 if divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend - divisor >= 0:
            dividend -= divisor
            result += 1
        result = dividendSign * divisorSign * result
        return result
    
print(Solution().divide(-2147483648,-1))