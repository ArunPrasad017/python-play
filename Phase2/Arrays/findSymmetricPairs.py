def find_symmetric(my_list):
    # Write your code here
    res =[]
    pair_set = set()
    for num in my_list:
        straight_set = tuple(num)
        num.reverse()
        reversed_set = tuple(num)
        if reversed_set in pair_set:
            res.append(list(straight_set))
            res.append(list(reversed_set))
        else:
            pair_set.add(straight_set)
    return res

lst = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
print(find_symmetric(lst))