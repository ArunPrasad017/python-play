"""
28. Implement strStr()

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""


def strStr(haystack, needle):
    if needle == "":
        return 0
    if needle == haystack:
        return 0
    if len(needle) < len(haystack):
        for i in range(len(haystack) - 1):
            if haystack[i : i + len(needle)] == needle:
                return i
    return -1
