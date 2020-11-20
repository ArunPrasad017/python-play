def find_pair(lst):
    d = {}
    res = []
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            added = lst[i] + lst[j]
            if added not in d:
                d[added] = [lst[i],lst[j]]
            else:
                prev_pair = d[added]
                curr_pair = [lst[i],lst[j]]
                res.append(prev_pair)
                res.append(curr_pair)
    return res

lst = [1,2,3,4]
print(find_pair(lst))