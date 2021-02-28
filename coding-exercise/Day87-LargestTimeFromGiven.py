from itertools import permutations


def largestTimeFromDigits(A):
    temp = list(permutations(A, 4))
    max_val, max_combo = 0, ""
    for a, b, c, d in temp:
        if (a < 3 and b < 10) and (c < 6 and d < 10):
            val = ((int(a) * 10) + int(b)) * 60 + (int(c * 10) + int(d))
            if val >= max_val and val <= 1439:
                max_val = val
                max_combo = str(a) + str(b) + ":" + str(c) + str(d)
    return max_combo


lst = [1, 2, 3, 4]
print(largestTimeFromDigits(lst))
