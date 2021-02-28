from collections import Counter


def numJewelsInStones(J, S):
    if J == S:
        return len(J)
    cntr = Counter(S)
    return sum(cntr[c] for c in J)


J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(S, J))
