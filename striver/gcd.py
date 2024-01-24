def calcGCD(n:int, m: int) -> int:
    # Write your code here
    if n < m:
        n,m = m,n
    
    if m == 0:
        return n
    
    return calcGCD(m , n%m)

print(calcGCD(18,45))