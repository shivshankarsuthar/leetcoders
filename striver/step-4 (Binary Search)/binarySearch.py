def search(nums: [int], target: int):
    # write your code logic !!
    l = 0
    r = len(nums)-1
    while l <= r:
        m = (l+r)//2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1
    return -1

print(search([1,3,7,9,11,12,45],3))