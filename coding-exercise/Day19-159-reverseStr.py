"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. 
If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, 
then reverse the first k characters and left the other as original.

Input: s = "abcdefg", k = 2
Output: "bacdfeg"

This is an absolute Naive solution
"""


def reverseStr(s, k):
    lst = [x for x in s]
    for i in range(0, len(lst), 2 * k):
        lst[i : i + k] = reversed(lst[i : i + k])
    return "".join(lst)


s = "abcdefg"
k = 2
print(reverseStr(s, k))
