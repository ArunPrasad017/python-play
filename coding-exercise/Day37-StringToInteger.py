class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        if string =="":
            return 0
        num = 0
        isNegative = False
        if string[0]=='-':
            isNegative = True
            string = string[1:]
        elif string[0] == '+':
            isNegative = False
            string = string[1:]
        for i,c in enumerate(string):
            if ord(c) in range(48,58):
                val = ord(c) - ord('0')
                num = (num*10)+val
            else:
                break
        if isNegative:
            if num*(-1) in range((-2)**31,1):
                return (-1)*num
            else:
                return (-2)**31
        return num if num in range(((2)**31)-1) else ((2)**31)-1