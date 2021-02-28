def mySqrt(x):
    if x<2:
        return x
    left,right=0,x//2
    while left<=right:
        mid = left+(right-left)//2
        if mid**2==x:
            return mid
        elif mid**2>x:
            right = mid-1
        elif mid**2<x:
            left = mid+1
    return right

x = 8
print(mySqrt(x))