def twoSum(nums, target):
    dict1, res = {}, []
    for i, num in enumerate(nums):
        dict1[num] = i
    for i in range(len(nums)):
        rem = target - nums[i]
        if rem in dict1 and i != dict1[rem]:
            res.append(i)
            res.append(dict1[rem])
            return res


print(twoSum([3, 2, 4], 5))
