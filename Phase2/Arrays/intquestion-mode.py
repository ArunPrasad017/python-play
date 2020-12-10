# o(n) space solution
from collections import Counter


def mode(lst):
    dict1 = dict(Counter(lst))
    return max(dict1, key=lambda k: dict1[k])


# lst = [1,1,2,5,1,2,4,1,4,4,4,4,4,4,4,4]
# print(mode(lst))

# o(1) solution - o(nlogn solution)
def mode2(lst):
    if len(lst) == 0:
        return 0
    max_cnt, count = 1, 1
    lst.sort()
    res = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1]:
            count += 1
        else:
            if count > max_cnt:
                max_cnt = count
                res = lst[i - 1]
            count = 0
    return res


lst = [1, 1, 2, 5, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 4, 1]
print(mode2(lst))
