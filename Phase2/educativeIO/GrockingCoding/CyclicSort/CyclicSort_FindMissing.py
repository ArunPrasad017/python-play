def find_missing_number(nums):
      # TODO: Write your code here
  i=0
  while i<len(nums):
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
    print(find_missing_number([1,4,2,0]))

if __name__ == "__main__":
    main()