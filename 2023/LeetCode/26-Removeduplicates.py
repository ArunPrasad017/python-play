def removeDuplicates(nums):
    i, idx = 0, 1
    for i in range(len(nums) - 1):
        if nums[i] != nums[i + 1]:
            nums[idx] = nums[i + 1]
            idx += 1
    return idx


print(removeDuplicates([1, 1, 2]))
