from typing import *
import time
def factorial(n,sum):
    if n == 0:
        return sum
    sum = sum * n
    return factorial(n-1,sum)

def factorialNumbers(n: int) -> List[int]:
    # Write your code here
    result = []
    dp = [-1] * (n+1)
    for i in range(1,n+1):
        if dp[i-1] != -1:
            fact = i * dp[i-1]
        else:
            fact = factorial(i,1)
        dp[i] = fact
        if fact <= n:
            result.append(fact)
        else:
            break
    return result
print(factorialNumbers(101466824))