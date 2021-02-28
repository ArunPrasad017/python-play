def plusOne(digits):
    if digits[-1]!=9:
        digits[-1]+=1
    else:
        res, carry ="", 0
        for i,num in enumerate(digits[::-1]):
            if carry or i==0:
                sumval = num+1
                res+=str(sumval%10)
                carry =sumval//10
            else:
                res+=str(num)
        if carry:
            res+='1'
        return list(res[::-1])
    return digits

lst = [9,9,9,9]
print(plusOne(lst))