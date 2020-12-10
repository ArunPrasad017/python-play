"""
Given an array of strings, group anagrams together.
Ex:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]

    Returns:
        list: the list of common anagrams
"""
from collections import defaultdict


def groupAnagrams(strs):
    dict_combo = defaultdict(list)
    for i in range(len(strs)):
        key = "".join(sorted(strs[i]))
        dict_combo[key].append(strs[i])
    return list(dict_combo.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
