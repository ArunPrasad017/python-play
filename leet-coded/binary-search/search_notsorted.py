def rotate_index(nums,left,right):
    if nums[left]<nums[right]:
        return 0
    
    while left<=right:
        pivot = (left+right)//2
        if nums[pivot] > nums[pivot+1]:
            return pivot+1
        else:
            if nums[pivot]<nums[left]:
                right = pivot-1
            else:
                left = pivot+1

def search(nums,left,right,target):
    n = len(nums)
    if n==0: 
        return -1
    if 
    while left<=right:
        pivot = (left+right)//2

        if nums[pivot] == target:
            return pivot
        elif nums[pivot]>target:
            left = pivot+1
        elif nums[pivot]<target:
            right = pivot - 1
    return -1

x = [4,5,6,7,8,9,0,1,2]
target = 0



