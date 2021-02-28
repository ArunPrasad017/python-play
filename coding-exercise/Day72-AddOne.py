"""
66. Plus One
Given a non-empty array of digits representing a non-negative integer, increment one to the integer.

The digits are stored such that the most significant digit is at the head of the list, 
and each element in the array contains a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.
"""


class Solution:
    def plusOne(self, lst: List[int]) -> List[int]:
        n = len(lst)
        if lst[n - 1] != 9:
            lst[n - 1] += 1
            return lst
        else:
            res, carry = "", 1
            lst = lst[::-1]
            for num in lst:
                val = num + carry
                carry = val // 10
                res = str(val % 10) + res
            if carry:
                res = "1" + res
            return [int(x) for x in res]
