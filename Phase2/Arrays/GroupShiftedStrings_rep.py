from collections import defaultdict


def groupStrings(strings):
    dict1 = defaultdict(list)
    for s in strings:
        key = ()
        for i in range(len(s) - 1):
            temp = (ord(s[i + 1]) - ord(s[i])) % 26
            key += (temp,)
        dict1[key].append(s)
    return list(dict1.values())
