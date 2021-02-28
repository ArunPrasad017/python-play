def productExceptSelf(nums):
    length = len(nums)
    left= [1]* length
    right = [1]* length
    center = [1]*length

    for i in range(length):
        left[i] = 1 if i==0 else nums[i-1] * left[i-1]
    for j in reversed(range(length-1)):
        right[j] = 1 if j == length-1 else nums[j+1] * right[j+1]
    for k in range(length-1,-1,-1):
        center[k] = 1 if k == length-1 else nums[k+1] * center[k+1]
    return [a*b for a,b in zip(left,right)]

nums=[1,2,3,4]
print(productExceptSelf(nums))