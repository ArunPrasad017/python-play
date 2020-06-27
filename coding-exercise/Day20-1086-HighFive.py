from collections import defaultdict
def highFive(items):
    dict1 = defaultdict(list)
    lst3 = []
    for lst in items:
        dict1[lst[0]].append(lst[1])
    print(dict1)

    for key in dict1.keys():
        id = key
        val = int(sum(sorted(dict1[id],reverse=True)[:5])/5)
        lst3.append([id,val])
    return lst3


items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
x = highFive(items)
print(x)