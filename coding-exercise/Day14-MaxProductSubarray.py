def maxProductSubarray(nums):
    # we use kadane's algorithm to solve this and 
    # this algorithm is an extension of dynamic programming

    if len(nums) == 1:
        return nums[0]

    max_prod = nums[0]
    current_prod = nums[0]
    min_prod = nums[0]

    for i in range(1,len(nums)):
        if nums[i]<0:
            temp = current_prod
            current_prod = min_prod
            min_prod = temp

        current_prod = max((current_prod*nums[i]), nums[i])
        min_prod = min((min_prod*nums[i]), nums[i])

        max_prod = max(current_prod, max_prod)

    return max_prod

nums = [-4,-3,-2]
print(maxProductSubarray(nums))