def maxProfit(nums):
    res = 0
    for i in range(1,len(nums)):
        if nums[i-1]<nums[i]:
            res+=(nums[i]-nums[i-1])
    return res

lst = [7,1,5,3,6,4]
print(maxProfit(lst))
lst = [1,2,3,4,5]
print(maxProfit(lst))