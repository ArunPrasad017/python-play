"""
https://www.educative.io/courses/grokking-the-coding-interview/B8qXVqVwDKY
time complexity - o(n)

"""
def cyclic_sort(nums):
      # TODO: Write your code here
  i=0
  while i<len(nums):
    if nums[i]-1==i:
      i+=1
    else:
      temp=nums[i]-1
      nums[i],nums[temp]=nums[temp],nums[i]
  return nums

def main():
    print(cyclic_sort([3,2,1,5,4]))

if __name__ == "__main__":
    main()