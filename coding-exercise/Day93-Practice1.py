def merge(s1,s2):
    ptr1, ptr2= 0,0
    res = ""
    while ptr1<len(s1) and ptr2<len(s2):
        if ptr1<=ptr2:
            res+=s1[ptr1]
            ptr1+=1
        else:
            res+=s2[ptr2]
            ptr2+=1
    if ptr1<len(s1):
        res+=s1[ptr1:]
    if ptr2<len(s2):
        res+=s2[ptr2:]
    return res

s1 = "aaaaa"
s2 = "bbb"
print(merge(s1,s2))