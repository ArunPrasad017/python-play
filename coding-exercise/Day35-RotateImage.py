def rotateImage(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            nums[i][j],nums[j][i] = nums[j][i], nums[i][j]
    for i in range(len(nums)):
        nums[i] = nums[i][::-1]
    return nums


nums = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
print(rotateImage(nums))