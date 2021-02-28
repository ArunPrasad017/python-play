# if recursive
def binarySearch(nums, l, r):
    if l == r:
        return nums[l]
    mid = l + (r - l) // 2
    if nums[mid] < nums[r]:
        return binarySearch(nums, l, mid)
    elif nums[mid] > nums[r]:
        return binarySearch(nums, mid + 1, r)
    return nums[r]


def search(nums):
    return binarySearch(nums, 0, len(nums) - 1)


# nums = [4,5,6,7,0,1,2]
# print(search(nums))

## if iterative
def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[right]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid + 1
        else:
            return nums[right]
    return nums[left]


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))
