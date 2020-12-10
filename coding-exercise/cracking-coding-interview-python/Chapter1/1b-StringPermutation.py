"""
Find Whether Two Strings are Permutation of each other
Output: True or false based on whether strings are permutation of other or not.
"""


def stringPermutations(str1, str2):
    if len(str1) != len(str2):
        return False
    # key: Char and value is auto-inrement value
    dict1 = {}
    for c in str1:
        if c not in dict1:
            dict1[c] = 1
        else:
            dict1 += 1
    for c in str2:
        if c in dict1.keys():
            dict1[c] -= 1
        else:
            return False
    res = all(x == 0 for x in dict1.values())
    return res


str1 = "abcd"
str2 = "beea"
print(stringPermutations(str1, str2))
