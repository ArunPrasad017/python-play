"""
Given a string, determine if a permutation of the string could form a palindrome.

Input: "carerac"
Output: true

"""

    # Time limit Exceeded    
    #     def isPalindrome(s):
    #         return s == s[::-1]
    #     lst = [''.join(p) for p in permutations(s)]
    #     for item in lst:
    #         if isPalindrome(item):
    #             return True
    #     return False

def canPermutePalindrome(s):
    dict_string = {}
    for c in s:
        if c not in dict_string:
            dict_string[c]=1
        else:
            dict_string[c]+=1
    count = sum((v%2) for k,v in dict_string.items())
    return count<=1

#string = "aabbhijkkjih"
string = "aab"
print(canPermutePalindrome(string))