from collections import Counter
def findAnagrams(s,p):
    dict_p = Counter(p)
    dict_s = Counter(s[:len(p)])
    res = []
    i,j = 0,len(p)
    while j<=len(s):
        if dict_p == dict_s:
            res.append(i)
        dict_s[s[i]]-=1
        if dict_s[s[i]]<=0:
            dict_s.pop(s[i])
        if j<len(s):
            dict_s[s[j]]+=1
        i+=1
        j+=1
    return res

s= "cbaebabacd"
p= "abc"
print(findAnagrams(s,p))