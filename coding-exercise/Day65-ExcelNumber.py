class Solution:
    def titleToNumber(self, s: str) -> int:
        cnt = 0
        dict1 = {}
        for i in range(65,91):
            cnt+=1
            dict1[chr(i)] = cnt
        sum_val = 0
        s = s[::-1]
        for i in range(len(s)):
            temp = dict1[s[i]]
            sum_val+=(temp*(26**i))
        return sum_val
