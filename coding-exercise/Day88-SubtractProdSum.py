def subtractProductAndSum(n):
    prod, sumVal = 1,0
    while n>0:
        rem=n%10
        sumVal+=rem
        prod*=rem
        n//=10
    return prod-sumVal

n = 234
print(subtractProductAndSum(n))