class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits[n-1]!=9:
            digits[n-1]+=1
        else:
            res,sumVal=[],0
            carry=0
            for i in range(n-1,-1,-1):
                sumVal = digits[i]+1 if i==n-1 else digits[i]+carry
                carry=sumVal//10
                res.append(sumVal%10)
            if carry:
                res.append(1)
            return res[::-1]
        return digits