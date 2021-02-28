def threeSumClosest(nums, target):
    minRes = float("inf")
    if not nums or len(nums) < 3:
        return 0
    nums.sort()
    for i in range(len(nums)):
        low, high = i + 1, len(nums) - 1
        while low < high:
            sumVal = nums[i] + nums[low] + nums[high]
            if sumVal == target:
                minRes = 0
                break
            elif abs(target - sumVal) < abs(minRes):
                minRes = target - sumVal
            if sumVal < target:
                low += 1
            else:
                high -= 1
        if minRes == 0:
            break
    return target - minRes
