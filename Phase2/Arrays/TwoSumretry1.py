
def twoSum(nums,target) :
    if len(nums)<2:
        return []
    res = []
    d={c:i for i,c in enumerate(nums)}
    for i in range(len(nums)):
        rem = target-nums[i]
        if rem in d and i!=d[rem]:
            res.append(i)
            res.append(d[rem])
            break
    return res