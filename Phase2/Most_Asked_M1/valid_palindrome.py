def isPalindrome(s):
    left,right = 0,len(s)-1
    while left<right:
        if s[left]==' ':
            left+=1
        else:
            break
    while right>0:
        if s[right]==' ':
            right-=1
        else:
            break
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower()==s[right].lower():
            left+=1
            right-=1
        else:
            return False
    return True

s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))