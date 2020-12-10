
def modifyString(s):
    res = ''
    if not s:
        return res
    if s=='?':
        return 'a'
    lst= [c for c in 'abcdefghijklmnopqrstuvwxyz']
    for i in range(len(s)):
        if s[i]!='?':
            res+=s[i]
        else:
            for c in lst:
                if i==0:
                    if c!=s[1]:
                        res+=c
                        break
                elif i==len(s)-1:
                    if res[i-1]!=c:
                        res+=c
                        break
                else:
                    if res[i-1]!=c and s[i+1]!=c:
                        res+=c
                        break
    return res

s="??yw?ipkj?"
print(modifyString(s))