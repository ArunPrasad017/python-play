class Solution:
    def twoSum(self,nums,tgt_idx,left,right):
        while left<right:
            if nums[left]+nums[tgt_idx]+nums[right]==0:
                temp = [nums[left], nums[tgt_idx], nums[right]]
                self.res.append(temp)
                left+=1
                right-=1
                while left<right and nums[left]==nums[left-1]:
                    left+=1
            elif nums[left]+nums[tgt_idx]+nums[right]>0:
                right-=1
            else:
                left+=1
                
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.res =[]
        if not nums:
            return self.res
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]>0:
                break
            elif i==0 or nums[i]!=nums[i-1]:
                self.twoSum(nums,i,i+1,len(nums)-1)
        return self.res