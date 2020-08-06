def isPowerOfFour(self, num: int) -> bool:
    if num==1:
        return 1
    if num<=0:
        return 0
    return (num & (num-1))==0 and (num%3)==1
    # counter =0
    # n=num
    # while num>1:
    #     num>>=2
    #     counter+=2
    # num2 = num<<counter
    # return num2==n