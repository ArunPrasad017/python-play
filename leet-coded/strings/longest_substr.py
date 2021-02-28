def Palindrome(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1 : r]


def longestPalindrome(s):
    if s == "":
        return " "
    p = ""
    for i in range(len(s)):
        p1 = Palindrome(s, i, i)
        p2 = Palindrome(s, i, i + 1)
        p = max([p, p1, p2], key=lambda x: len(x))
    return p


print(longestPalindrome("abac"))
