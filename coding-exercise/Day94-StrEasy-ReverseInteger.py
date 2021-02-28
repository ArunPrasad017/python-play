def reverse(num):
    isNeg = False
    if num<0:
        isNeg=True
    n = len(str(abs(num))) -1
    res = 0
    num = abs(num)
    while num>0:
        rem=num%10
        num=num//10
        res+=(rem*(10**n))
        n-=1
    return -1*res if isNeg else res

nums=-123
print(reverse(nums))