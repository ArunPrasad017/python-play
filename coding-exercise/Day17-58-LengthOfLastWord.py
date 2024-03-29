"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',  return the length of last word 
(last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

Note: A word is defined as a maximal substring consisting of non-space characters only.
"""


def lengthOfLastWord(s):
    lst = s.strip().split(" ")
    if len(lst) >= 1:
        return len(lst[-1])
    return 0


# s = "H      "
s = "Hello World"
print(lengthOfLastWord(s))
