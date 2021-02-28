class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        max_index = nums.index(max(nums))
        for i in range(len(nums)):
            if (2*nums[i]) > nums[max_index] and max_index!=i:
                return -1
        return max_index