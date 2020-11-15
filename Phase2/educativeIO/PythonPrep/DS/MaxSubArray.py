def find_max_sum_subarray(nums): 
  # Write your code here!
  curr_sum = max_sum = nums[0]
  for i in range(1,len(nums)):
    if nums[i-1]>0:
      nums[i]+=nums[i-1]
    max_sum=max(nums[i],max_sum)
  return max_sum

# nums = [-2,10,7,-5,15,6]
# print(find_max_sum_subarray(nums))


def rearrange(lst):
    # Write your code here
    left_most_pos = 0
    i=0
    while i<len(lst):
        if lst[i]>0:
            i+=1
        else:
            lst[i],lst[left_most_pos]=lst[left_most_pos],lst[i]
            left_most_pos+=1
            i+=1
    return lst

lst = [10,-1,20,4,5,-9,-6]
print(rearrange(lst))
lst = [-1, 2, -3, -4, 5]
print(rearrange(lst))