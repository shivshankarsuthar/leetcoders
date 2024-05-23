def intToBin(num):
    binary = ''
    while num:
        binary = str(num % 2) + binary
        num = num // 2
    return binary

def intToBinRecursively(num,ans):
    if num == 0:
        return ans

    ans = str(num%2) + ans
    return intToBinRecursively(num//2,ans)

def intToBinBacktracking(num):
    global ans
    if num == 0:
        return

    intToBinBacktracking(num//2)
    ans += str(num % 2)
    return ans
#print(intToBin(9))
ans = ''
print(intToBinBacktracking(9))