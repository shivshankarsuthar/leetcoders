import time
from tkinter import N

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        func(*args,**kwargs)
        end = time.time()
        print(end-start)    
    return wrapper



def fibonacci(n):
    if dp[n] != -1:
        return dp[n]
    if n <= 2:
        return 1
    
    dp[n] = fibonacci(n-1) + fibonacci(n-2)
    return dp[n]

n = 100
dp = [-1]*(n+1)
print(fibonacci(n))

# 1,1,2,3,5,8