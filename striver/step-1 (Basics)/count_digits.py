def countDigits(n: int) -> int:
    # Write your code here
    count = 0
    while n != 0:
        count += 1
        n = n // 10
    return count

print(countDigits(123))