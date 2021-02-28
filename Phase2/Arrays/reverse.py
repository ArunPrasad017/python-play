def reverse(x):
    is_neg = False
    if x<0:
        is_neg=True
    x=abs(x)
    n= len(str(x))-1
    res = 0
    while x:
        temp=x%10
        res+=(temp*(10**n))
        x=x//10
        n-=1
    if res>2**31:
        return 0
    return -1*res if is_neg else res

num = 1534236469
print(reverse(num))
