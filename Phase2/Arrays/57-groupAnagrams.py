from collections import defaultdict
def groupAnagrams(strs):
    d = defaultdict(list)
    for s in strs:
        temp = ''.join(sorted(s))
        d[temp].append(s)
    res = []
    for k,v in d.items():
        res.append(v)
    return res

s = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(s))