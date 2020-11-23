def productExceptSelf(nums):
    left = [1]*len(nums)
    right = [1]*len(nums)
    for i in range(1,len(nums)):
        left[i]=left[i-1]*nums[i-1]
    for i in range(len(nums)-1,-1,-1):
        right[i] = 1 if i==len(nums)-1 else right[i+1]*nums[i+1]
    return [i*j for i,j in zip(left,right)]