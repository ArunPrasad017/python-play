# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        left,right=0,1
        while reader.get(right)<target:
            left+=1
            right<<=2
        while left<=right:
            mid = left+(right-left)//2
            num = reader.get(mid)
            if num==target:
                return mid
            elif num>target:
                right=mid-1
            else:
                left=mid+1
        return -1