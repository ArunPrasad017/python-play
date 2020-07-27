from nose.tools import assert_equal

def addStrings(num1, num2):
    carry = 0
    str_val = ""
    while num1 and num2:
        val = 0
        a = len(num1) -1
        b = len(num2) -1

        val = (int(num1[a])+ int(num2[b])+carry)%10
        carry = int((int(num1[a])+ int(num2[b])+carry)/10)

        str_val=str(val)+str_val
        num1 = num1[:-1]
        num2 = num2[:-1]

    if num1:
        str_val= str(int(num1)+carry)+str_val
        return str_val
    if num2:
        str_val= str(int(num2)+carry)+str_val
        return str_val
    if carry:
        str_val=str(carry)+str_val
        return str_val
    return str_val

assert_equal(addStrings("9","99"),"108")
assert_equal(addStrings("5099","4000"),"9099")
assert_equal(addStrings("5000","5000"),"10000")