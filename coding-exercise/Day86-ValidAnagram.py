def isAnagram(s,t):
    if not s and not t:
        return True
    if len(s)!=len(t):
        return False
    s = sorted(s)
    t = sorted(t)
    return all(i == j for i,j in zip(s, t))

def isAnagram2(s, t):
    # first check if lengths are same - if not equal they are not considered as anagrams
    if len(s)!=len(t):
        return False
    # creates an empty dictionary
    dict1 = Counter()
    # iterate through first string and add one each time to the corresponding key
    # the best advantage of using a counter - we need not check if elements exists in the dictionary
    for c in s:
        dict1[c]+=1
    # Iterate through second string and reduce the number by 1 each time 
    # we encounter the same key in second string
    for c in t:
        dict1[c]-=1 
    # all function returns True if all the values in dictionary match with condition here(val==0)
    return all(val==0 for val in dict1.values())

