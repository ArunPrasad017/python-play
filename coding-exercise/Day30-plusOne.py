def plusOne(digits):
    l=len(digits)
    total = 0;carry=0
    digits=digits[::-1]
    for i in range(0,l):
        if i==0:
            total+= digits[i]+1
            carry= total%10
        else:
            total+=(digits[i])*(10**i)
    lst2=[int(i) for i in str(total)]
    return lst2


# lst =[4,3,2,1]
lst = [9,9,9,9]
print(plusOne(lst))