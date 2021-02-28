def majorityElement(nums):
    dict1 = {}
    # comment on usage of dict comprehension
    # can use the counter from default dict
    for num in nums:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num] += 1
    n = len(nums) // 2 + 1
    for k, v in dict1.items():
        if v >= n:
            return k
    return None
