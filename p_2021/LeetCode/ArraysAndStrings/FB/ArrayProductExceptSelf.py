def productExceptSelf(nums):
    l1 = [1]* len(nums)
    l2 = [1]* len(nums)
    res = []
    for i in range(1,len(l1)):
        l1[i]=nums[i-1]*l1[i-1]
    for j in range(len(nums)-1,-1,-1):
        if j==len(nums)-1:
            l2[j]=1
        else:
            l2[j]= nums[j+1]*l2[j+1]
    size = len(l2)
    i=0
    for l,r in zip(l1,l2):
        res.append(l*r)
    return res