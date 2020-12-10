def productExceptSelf(nums):
    length = len(nums)
    left = [1] * length
    right = [1] * length
    center = [1] * length

    for i in range(0, length):
        if i == 0:
            left[i] = 1
        else:
            left[i] = nums[i - 1] * left[i - 1]

    for j in reversed(range(length - 1)):
        if j == length - 1:
            right[j] = 1
        else:
            right[j] = nums[j + 1] * right[j + 1]

    for k in range(length - 1, -1, -1):
        if k == length - 1:
            center[k] = 1
        else:
            center[k] = nums[k + 1] * center[k + 1]

    ans = [a * b for a, b in zip(left, right)]
    return ans


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
