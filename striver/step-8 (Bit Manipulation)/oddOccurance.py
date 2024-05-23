def find_odd_occurrences(arr):
    # Find XOR of all elements
    xor_result = 0
    for num in arr:
        xor_result ^= num
    
    # Find the rightmost set bit
    rightmost_set_bit = xor_result & -xor_result
    
    # Initialize the results
    result1 = 0
    result2 = 0
    
    # Partition the numbers based on the rightmost set bit
    for num in arr:
        if num & rightmost_set_bit:
            result1 ^= num
        else:
            result2 ^= num
    
    # Find all elements with odd occurrences
    odd_occurrences = []
    for num in arr:
        if num == result1:
            odd_occurrences.append(num)
        elif num == result2:
            odd_occurrences.append(num)
    
    return odd_occurrences

# Example usage:
arr = [10,8,2,5,5]
result = find_odd_occurrences(arr)
print("Elements with odd occurrences:", result)
