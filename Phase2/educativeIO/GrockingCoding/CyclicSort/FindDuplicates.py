def find_all_duplicates(nums):
    # TODO: Write your code here
    i,n=0,len(nums)
    while i<n:
        j=nums[i]-1
        if nums[i]!=nums[j]:
            nums[i], nums[j] = nums[j], nums[i]    
        else:
            i+=1
    return [nums[i] for i in range(n) if nums[i]!=i+1]
