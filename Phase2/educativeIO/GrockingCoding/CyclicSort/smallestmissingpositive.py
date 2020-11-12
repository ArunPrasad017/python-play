def first_missing_positive(nums):
    i,n = 0, len(nums)
    while i<n:
        j=nums[i]-1
        if nums[i]>0 and nums[i]<n and nums[i]!=nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i+=1
    for i in range(n):
        if nums[i]!=i+1:
            return i+1
    return -1

nums = [3,-2,0,1,2]
print(first_missing_positive(nums))