def thirdMax(nums):
    # easy pythonic way
    new_set = set(nums)
    if len(new_set)<3:
        return max(nums)
    return sorted(new_set)[-3]

def thirdMax2(nums):
    # more space optimized pythonic way using set
    new_set = set()
    for num in nums:
        new_set.add(num)
        if len(new_set)>3:
            new_set.remove(min(new_set))
    return max(nums) if len(new_set)<3 else min(new_set)

nums = [2, 2, 3, 1]
print(thirdMax(nums))
print(thirdMax2(nums))