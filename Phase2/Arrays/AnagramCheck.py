def Anagram(s1, s2):
    l1 = sorted(list("".join(s1.split())))
    l2 = sorted(list("".join(s2.split())))
    return l1 == l2


####other type


def Anagram2(s1, s2):
    l1 = s1.replace(" ", "")
    l2 = s2.replace(" ", "")
    return sorted(l1) == sorted(l2)


# type3:
from collections import Counter


def Anagram3(s1, s2):
    if len(s1) != len(s2):
        return False
    d1 = Counter(s1.replace(" ", ""))
    d2 = Counter(s2.replace(" ", ""))
    return d1 == d2


s1 = "clint eastwood"
s2 = "old west actions"

print(Anagram3(s1, s2))
