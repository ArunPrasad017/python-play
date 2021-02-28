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
    for str_ in strs:
        key = "".join(sorted(str_))
        dict_combo[key].append(str_)
    return list(dict_combo.values())

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
