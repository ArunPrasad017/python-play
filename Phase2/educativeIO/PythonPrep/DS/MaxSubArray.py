def find_max_sum_subarray(nums): 
  # Write your code here!
  curr_sum = max_sum = nums[0]
  for i in range(1,len(nums)):
    if nums[i-1]>0:
      nums[i]+=nums[i-1]
    max_sum=max(nums[i],max_sum)
  return max_sum

nums = [-2,10,7,-5,15,6]
print(find_max_sum_subarray(nums))