from collections import defaultdict
def groupAnagrams(strs):
    dict_combo = defaultdict(list)
    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        dict_combo[key].append(strs[i])
    return list(dict_combo.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
