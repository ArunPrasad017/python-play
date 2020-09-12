def mySqrt(x):
    left = 0
    right= x//2
    while left<=right:
        mid = left+(right-left)//2
        if (mid**2)== x:
            return mid
        if (mid**2)>x:
            right = mid-1
        if (mid**2)<x:
            left=mid+1
    return right
