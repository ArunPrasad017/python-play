def isPalindrome(self, s: str) -> bool:
    # s1 = ''.join(c.lower() for c in s if c.isalnum())
    # return s1==s1[::-1]
    # two pointer technique
    start, end = 0, len(s)-1
    while start<end:
        while start<end and not s[start].isalnum():
            start+=1
        while start<end and not s[end].isalnum():
            end-=1
        if start<end and s[start].lower() != s[end].lower():
            return False
        start+=1
        end-=1
    return True