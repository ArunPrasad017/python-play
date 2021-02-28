from collections import defaultdict


def groupAnagrams(strs):
    string_dict = defaultdict(list)
    for s in strs:
        key = "".join(sorted(s))
        string_dict[key].append(s)
    return list(string_dict.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
