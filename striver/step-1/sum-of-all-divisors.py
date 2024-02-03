
def findAllDivisors(n):
    divisors = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n//i)
    return divisors

def sumOfAllDivisors(n: int) -> int:
    # Write your code here
    sum_of_divisors = 0
    for i in range(1,n+1):
        sum_of_divisors += sum(findAllDivisors(i))
    return sum_of_divisors

result = sumOfAllDivisors(5)
print(result)