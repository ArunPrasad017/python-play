# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

def guessNumber(n):
    low = 0
    high = n-1
    while low<=high:
        mid = (low+(high-low)//2)
        res = guess(mid)
        if res == -1:
            right = mid-1
        elif res == 0:
            return mid
        elif res == 1:
            left = mid+1
    return -1