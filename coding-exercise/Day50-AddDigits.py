def AddDigits(num):
    # looping and math
    # if num==0:
    #     return 0
    # total = 0
    # while num>0:
    #     total+=num%10
    #     num//=10
    # return 9 if total%9==0 else total%9

    # math only
    if num == 0:
        return 0
    if num % 9 == 0:
        return 9
    else:
        return num % 9


num = 90071
print(AddDigits(num))
