"""
Palindrome permutation
(ex) 
Input: Taco Cat
Output: True(Taco Cat - when we remove o we have the possibility of this being a palindrome)


Hint: Use dictionary
"""
import string
def palindrome_permutation(s):
    dict_string = {}
    for c in s:
        if c.lower() not in dict_string and ord(c.lower()) in range(97,123):
            dict_string[c.lower()] = 1
        elif ord(c.lower()) in range(97,123):
            dict_string[c.lower()]+=1
    count =0
    for k,v in dict_string.items():
        if v%2==1:
            count+=1
    if count>1:
        return False
    return True

s = "Taco Cat"
print(palindrome_permutation(s))