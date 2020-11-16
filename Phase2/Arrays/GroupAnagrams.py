from collections import defaultdict
def groupAnagrams(strs):
        d = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            d[key].append(s)
        return d.values()