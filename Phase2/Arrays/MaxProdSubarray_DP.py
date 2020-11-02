def maxProduct(nums):
    # example of arrays and DP - using parallel arrays for min and max
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    minVal = maxVal = curr = nums[0]
    res = maxVal
    for i in range(1,len(nums)):
        curr = nums[i]
        tempMax = max(curr,curr*minVal,curr*maxVal)
        minVal = min(curr,curr*minVal,curr*maxVal)
        maxVal = tempMax
        res = max(maxVal,res)
    return res

s = [2,3,-2,4]
print(maxProduct(s))