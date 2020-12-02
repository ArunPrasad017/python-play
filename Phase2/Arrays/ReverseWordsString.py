def reverseWords(s):
    left,right= 0,len(s)-1
    while left<right:
        s[left],s[right] = s[right], s[left]
        left+=1
        right-=1
    start,end = 0,0
    while start<len(s):
        if end+1<=len(s)-1 and s[end+1]!=' ':
            end+=1
        else:
            temp=end
            while start<end:
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
            start=temp+2
            end=temp+2
    return s

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
print(reverseWords(s))