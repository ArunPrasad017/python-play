from collections import defaultdict
def sum_hash(lst):
    d = defaultdict(list)
    res = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            sumVal = lst[i]+lst[j]
            if sumVal not in d:
                d[sumVal].append(lst[i])
                d[sumVal].append(lst[j])
            else:
                res.append([lst[i],lst[j]])
                res.append(d.get(sumVal))
                return res
    return res
my_list = [3, 4, 7, 1, 12, 9]
print(sum_hash(my_list))