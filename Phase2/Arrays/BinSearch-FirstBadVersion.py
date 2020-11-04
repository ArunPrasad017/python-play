# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def firstBadVersion(self, n):
    """
    :type n: int
    :rtype: int
    """
    left,right = 0,n
    while left<right:
        mid = (left+right)//2
        if isBadVersion(mid)==False:
            left = mid+1
        else:
            right = mid
    return left