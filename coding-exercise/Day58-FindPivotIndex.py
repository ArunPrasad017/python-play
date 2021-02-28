def pivotIndex(nums):
    sum_val = sum(nums)
    leftsum = 0
    for i,c in enumerate(nums):
        if leftsum == sum_val - c - leftsum:
            return i
        leftsum+=c
    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))
