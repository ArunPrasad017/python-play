def binarySearch(nums, left, right):
    if left == right:
        return nums[left]
    mid = left + (right - left) // 2
    if nums[mid] < nums[right]:
        return binarySearch(nums, left, mid)
    elif nums[mid] > nums[right]:
        return binarySearch(nums, mid + 1, right)
    else:
        return binarySearch(nums, left, right - 1)


def search(nums):
    return binarySearch(nums, 0, len(nums) - 1)


# nums = [4,4,4,5,6,7,0,1,2]
# print(search(nums))


def findMinIter(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            right -= 1
    return nums[left]


nums = [1, 3, 5]
print(findMinIter(nums))
