def find_duplicate(nums):
# TODO: Write your code here
    # method 1
    # o(n*log(n))
    # nums.sort()
    # for i in range(1,len(nums)):
    #   if nums[i-1]==nums[i]:
    #     return nums[i]
    # return -1

    # method 2
    i,n = 0,len(nums)
    while i<n:
      if nums[i]-1!=i:
        j=nums[i]-1
        if nums[i]!=nums[j]:
          nums[i],nums[j]=nums[j], nums[i]
        else:
          return nums[i]
      else:
        i+=1

def main():
    nums = [2, 1, 3, 3, 5, 4]
    print(find_duplicate(nums))
    nums = [1, 4, 4, 3, 2]
    print(find_duplicate(nums))
    
if __name__ == "__main__":
    main()