"""
Given an arbitrary ransom note string and another string containing letters from all the magazines, 
write a function that will return true if the ransom note can be constructed 
from the magazines ; otherwise, it will return false.

Input: ransomNote = "a", magazine = "b"
Output: false

Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

def canConstruct(ransomNote, magazine):
    dict_ransom= {}
    dict_magazine= {}

    for c in ransomNote:
        if c not in dict_ransom.keys():
            dict_ransom[c]=1
        else:
            dict_ransom[c]+=1
    
    for c in magazine:
        if c not in dict_magazine.keys():
            dict_magazine[c]=1
        else:
            dict_magazine[c]+=1

    for k,v in dict_ransom.items():
        if dict_magazine[k] < v:
            return False
    return True

ransomNote = "aa"
magazine = "aab"

print(canConstruct(ransomNote,magazine))