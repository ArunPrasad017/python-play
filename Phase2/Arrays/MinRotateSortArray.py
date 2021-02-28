def findMin(nums):
    left, right = 0, len(nums) - 1
    # edge cases
    if nums[left] < nums[right]:
        return nums[left]
    if len(nums) == 1:
        return nums[0]

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid - 1] > nums[mid]:
            return nums[mid]
        elif nums[mid] > nums[left]:
            left = mid + 1
        else:
            right = mid - 1


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))
