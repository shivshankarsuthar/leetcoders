def countSetBits(N: int) -> int:
    #Write your code here
    count = 0
    for i in range(N+1):
        binary = bin(i)[2:]
        for j in binary:
            if int(j) == 1:
                count += 1

    return count

print(countSetBits(4))