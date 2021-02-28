# using the two pointer method
def max_min(nums):
    # Write your code here
    left,right = 0,len(nums)-1
    res= []
    while left<right:
        res.append(nums[right])
        right-=1
        res.append(nums[left])
        left+=1
    if len(nums)%2==1:
        res.append(nums[len(nums)//2])
    return res

# simpler technique dividing the size of list by 2
def max_min(nums):
    # Write your code here
    res =[]
    for i in range(len(nums)//2):
        res.append(nums[-(i+1)])
        res.append(nums[i])
    if len(nums)%2==1:
        res.append(nums[len(nums)//2])
    return res