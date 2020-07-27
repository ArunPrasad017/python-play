"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Hint: Used two pointer technique
"""
def isPalindrome(s,a,b):
    while a<b:
        if s[a]!=s[b]:
            return False
        a+=1
        b-=1
    return True

def validPalindrome(s):
    right = len(s)-1
    for left in range(right):
        if s[left]!=s[right]:
            return (isPalindrome(s,left+1,right) or isPalindrome(s,left,right-1))
        right-=1
    return True


s = "abcaa"
print(validPalindrome(s))