"""
implementing pow(x,n)
"""
def pow_of(x,n):
    if n<0:
        x = 1/x
        n=abs(n)
    curr=x
    ans=1
    while n>0:
        if n%2==1:
            ans*=curr
        curr*=curr
        n//=2
    return ans

n,x = 2.100,3
print(pow_of(x,n))