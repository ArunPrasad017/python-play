def myPow_Brute(x, n):
    # brute force solution
    if n<0:
        x = 1/x
        n=abs(n)
    ans =1
    for _ in range(n):
        ans*=x
    return ans

# Exponention by Squaring method or Binary Exponentiation
# the recursive method
# def powHelper(x,n):
#     if n==0:
#         return 1.0
#     half_ans = powHelper(x,n//2)
#     if n%2 ==0:
#         return half_ans*half_ans
#     else:
#         return half_ans*half_ans*x
# def myPow(x,n):
#     if n<0:
#         x = 1/x
#         n = abs(n)
#     return powHelper(x,n)

def myPow(x,n):
    if n<0:
        x = 1/x
        n = abs(n)
    current = x
    ans =1
    i = n
    while i>0:
        if i%2==1:
            ans*=current
        current*=current
        i=i//2
    return ans

x =  2.00000
n = 11
print(myPow(x,n))