from collections import defaultdict


def find_two_pairs(my_list):
    d = defaultdict(list)
    res = []
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list)):
            sumVal = my_list[i] + my_list[j]
            if sumVal not in d:
                d[sumVal].append(my_list[i])
                d[sumVal].append(my_list[j])
            else:
                res.append(d[sumVal])
                res.append([my_list[i], my_list[j]])
    return res


my_list = [3, 4, 7, 1, 12, 9]
print(find_two_pairs(my_list))
