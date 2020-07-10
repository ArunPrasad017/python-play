# def twoSum(nums,target):
#     dict1={}
#     lst=[]
#     for i,num in enumerate(nums):
#         dict1[target-num]=i
#     for i,num in enumerate(nums):
#         if num in dict1.keys() and i!=(dict1[num]):
#             lst.append(i)
#             lst.append(dict1[num])
#             break
#     return lst

# def twoSum2(nums,target):
#     left = 0
#     right = len(nums)-1
#     while left<right:
#         if nums[left]+nums[right]==target:
#             return ([left+1,right+1])
#         elif nums[left]+nums[right]>target:
#             right-=1
#         elif nums[left]+nums[right]<target:
#             left+=1
#     return [-1,-1]

def twoSum(nums,i,res):
    left=i+1
    right = len(nums)-1
    while left<right:
        total = nums[i]+nums[left]+nums[right]
        if total<0 or (left>i+1 and nums[left]==nums[left-1]):
            left+=1
        elif total>0 or (right<len(nums)-1 and nums[right]==nums[right+1]):
            right-=1
        else:
            res.append([nums[i],nums[left],nums[right]])
            left+=1
            right-=1

def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i]>0:
            break
        if i==0 or nums[i]!=nums[i-1]:
            twoSum(nums,i,res)
    return res

# nums=[3,2,4]
# nums = [1,3,8,5]
# target=6
# print(twoSum(nums,target))
# nums2 = [2,7,11,15]
# target2 = 9
# print(twoSum2(nums2,target2))

nums = [0,-4,-1,-4,-2,-3,2]
print(threeSum(nums))