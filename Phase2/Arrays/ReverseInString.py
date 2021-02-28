def reverse(s,left,right):
    while left<right:
        s[left],s[right]=s[right],s[left]
        left+=1
        right-=1

def reverseWords(s):
    left,right =0,len(s)-1
    while left<right:
        if s[left]!=' ':
            break
        left+=1
    while right>0:
        if s[right]!=' ':
            break
        right-=1
    if not s:
        return ""
    lst = s.split()
    reverse(lst,0,len(lst)-1)
    return ' '.join(lst)

s = "Alice does not even like bob"
print(reverseWords(s))

