from collections import Counter


def canPermutePalindrome(s):
    d = Counter()
    for c in s:
        d[c] += 1
    cnt = sum((v % 2) for k, v in d.items())
    return cnt <= 1


s = "code"
print(canPermutePalindrome(s))
s = "racecar"
print(canPermutePalindrome(s))
