from collections import Counter
def numJewelsInStones(J,S):
        res = 0
        if J==S:
            return len(J)
        cntr = Counter(S)
        for c in J:
            res+=cntr[c]
        return res

J = "aA"
S = "aAAbbbb"
print(numJewelsInStones(S,J))