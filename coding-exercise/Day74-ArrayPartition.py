def arrayPairSum(nums):
    # easy method
    nums.sort()
    return sum(nums[::2])

def arrayPairsTwoPointer(nums):
      nums.sort()
      pos1 = 0
      pos2 = 1
      total = 0
      if len(nums)==2:
          return min(nums)
      while pos2<=len(nums)-1:
          total+=min(nums[pos1],nums[pos2])
          pos1+=2
          pos2+=2
      return total

def arrayPairsSourcery(nums):
    # using for instead of while - this is a suggested method by sourcery
    nums.sort()
    pos1 = 0
    total = 0
    if len(nums)==2:
        return min(nums)
    for pos2 in range(1, len(nums), 2):
        total+=min(nums[pos1],nums[pos2])
        pos1+=2
    return total