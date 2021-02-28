# Brute force
# def isUgly(num):
#     i=2
#     while i in range(2,6) and num>0:
#         while num%i==0:
#             num//=i
#         i+=1
#     return num==1

# def nthUglyNumber(n) -> int:
#     i = 0
#     while n>0:
#         i+=1
#         if isUgly(i):
#             n-=1
#     return i


def nthUglyNumber(n):
    i2 = 0
    i3 = 0
    i5 = 0
    lst1 = [1]
    uglyNum = 1
    next2 = 2
    next3 = 3
    next5 = 5

    for i in range(1, n):
        uglyNum = min(next2, next3, next5)
        lst1.append(uglyNum)
        if uglyNum == next2:
            i2 += 1
            next2 = lst1[i2] * 2
        if uglyNum == next3:
            i3 += 1
            next3 = lst1[i3] * 3
        if uglyNum == next5:
            i5 += 1
            next5 = lst1[i5] * 5

    return uglyNum


print(nthUglyNumber(1690))
