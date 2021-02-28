def pivoted_binary_search(nums, n, key):
    """
    Function to search key in a list
    :param lst: A list of integers
    :param n: The size of the list
    :param key: A key to be searched in the list
    """

    # Write your code here!
    def binary_search(nums,left,right):
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]==key:
                return mid
            elif nums[mid]>key:
                right=mid-1
            else:
                left=mid+1
                
    def rotation_idx(nums):
        left,right=0,len(nums)-1
        if nums[left]<nums[right]:
            return 0
        while left<=right:
            mid = left+(right-left)//2
            if nums[mid]>nums[mid+1]:
                return mid+1
            elif nums[mid]>=nums[left]:
                left=mid+1
            else:
                right=mid-1
    if not nums:
        return True
    if len(nums)==1:
        return nums[0]==key
    idx = rotation_idx(nums)
    if not idx:
        return binary_search(nums,0,len(nums)-1)
    elif key==nums[idx]:
        return idx
    elif key>nums[0]:
        return binary_search(nums,0,idx)
    else:
        return binary_search(nums,idx,len(nums)-1)
    
print(pivoted_binary_search([7, 8, 9, 0, 3, 5, 6], 7, 3))