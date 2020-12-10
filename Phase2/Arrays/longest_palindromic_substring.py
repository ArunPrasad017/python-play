def expandFromMiddle(s,left,right):
    while left>=0 and right<=len(s)-1 and s[left]==s[right]:
        left-=1
        right+=1
    return s[left+1:right]
        

def longestPalindrome(s):
    p=''
    if len(s)==1:
        return s
    for i in range(len(s)):
        p1=expandFromMiddle(s,i,i)
        p2=expandFromMiddle(s,i,i+1)
        p = max([p,p1,p2],key= lambda x:len(x))
    return p

s = "babad"
print(longestPalindrome(s))