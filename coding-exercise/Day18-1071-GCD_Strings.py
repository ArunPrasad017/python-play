def gcdStrings(s1,s2):
    if len(s1)<len(s2):
        gcdStrings(s2,s1)
    
    if s1==s2:
        return s1
    
    if s1[:len(s2)]!=s2:
        return ""
    else:
        return gcdStrings(s1[len(s2):],s2)

str1 = "ABCABC"
str2 = "ABC"

print(gcdStrings(str1,str2))
