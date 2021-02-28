def plusOne(digits):
    carry = 0
    sum_val = 0
    digits = digits[::-1]
    for i in range(len(digits)):
        if i==0:
            sum_val+=(digits[i]+1)
            carry = sum_val%10
        else:
            sum_val+=((10**i)*(digits[i]))
    lst2 = [int(i) for i in str(sum_val)]
    return lst2

digits = [9,9,9,9]
print(plusOne(digits))
