def find_symmetric(lst):
    seen = set()
    res = []
    for item in lst:
        cur_item = tuple(item)
        item.reverse()
        rev_item = tuple(item)
        if rev_item not in seen:
            seen.add(cur_item)
        else:
            res.append(cur_item)
            res.append(rev_item)
    return res


lst = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
print(find_symmetric(lst))
