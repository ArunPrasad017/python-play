"""
# --------------------From CodeSignal--------------------
https://app.codesignal.com/coding-report/pdEiPBEa27PACfSg6-XvsprpMX9R4NKba8c3AHjvYx/pGkyymPXAxwc9QN6f

You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".
You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.
Given two strings s1 and s2, return the result of the special merge function you are implementing.
Example
For s1 = "dce" and s2 = "cccbd", the output should be
mergeStrings(s1, s2) = "dcecccbd".
All symbols from s1 goes first, because all of them have only 1 occurrence in s1 and c has 3 occurrences in s2.
For s1 = "super" and s2 = "tower", the output should be
mergeStrings(s1, s2) = "stouperwer".
Because in both strings all symbols occur only 1 time, strings are merged as usual. You can find explanation for this example on the image in the description.

Input/Output
[execution time limit] 4 seconds (py3)
[input] string s1
A string consisting only of lowercase English letters.
Guaranteed constraints:
1 ≤ s1.length ≤ 104.
[input] string s2
A string consisting only of lowercase English letters.
Guaranteed constraints:
1 ≤ s2.length ≤ 104.
[output] string
The string that results by merging s1 and s2 using your special merge function.
"""
from collections import Counter
def mergeStrings(s1, s2):
    dict1 = Counter()
    dict2 = Counter()
    res = ""
    ptr1, ptr2 = 0,0
    for c in s1:
        dict1[c]+=1
    for c in s2:
        dict2[c]+=1
    while ptr1<=len(s1)-1 and ptr2<=len(s2)-1:
        if (dict1[s1[ptr1]] < dict2[s2[ptr2]]):
            res+=str(s1[ptr1])
            ptr1+=1
        elif (dict1[s1[ptr1]] > dict2[s2[ptr2]]):
            res+=str(s2[ptr2])
            ptr2+=1
        elif (ord(s1[ptr1]) <= ord(s2[ptr2])) and (dict1[s1[ptr1]] == dict2[s2[ptr2]]):
            res+=str(s1[ptr1])
            ptr1+=1
        elif (ord(s1[ptr1]) > ord(s2[ptr2])) and (dict1[s1[ptr1]] == dict2[s2[ptr2]]):
            res+=str(s2[ptr2])
            ptr2+=1
    if ptr2!=len(s2)-1 or len(s2)==1:
        res+=str(s2[ptr2:])
    if ptr1!=len(s1)-1 or len(s1)==1:
        res+=str(s1[ptr1:])
    return res