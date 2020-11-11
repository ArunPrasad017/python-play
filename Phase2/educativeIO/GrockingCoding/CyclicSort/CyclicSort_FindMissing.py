def find_missing_number(nums):
      # TODO: Write your code here
  i=0
  while i<len(nums)-1:
    j = nums[i]
    if nums[i]<len(nums) and nums[j]!=nums[i]:
      nums[i],nums[j] = nums[j],nums[i]
    else:
      i+=1
  for i in range(len(nums)):
    if i!=nums[i]:
      return i
  return -1

def main():
    print(find_missing_number([0,1,2,3,5]))

if __name__ == "__main__":
    main()