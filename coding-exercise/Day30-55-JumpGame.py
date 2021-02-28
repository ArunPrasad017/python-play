def canJump(nums):
    if nums[0] == 0:
        return 0
    reach = 0
    for i in range(len(nums)):
        if i > reach:
            return False
        reach = max(reach, i + nums[i])
    return True


# nums = [2,3,1,1,4]
nums = [3, 2, 1, 0, 4]
print(canJump(nums))
