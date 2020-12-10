def tuple_ex():
    # tuple unpacking
    tuplex = 1, 2, 3, 4
    c1, c2, c3, c4 = tuplex
    tuplex += (9,)
    # return c1,c2,c3,c4
    # return tuplex
    # str1 = ''.join(str(tuplex))
    # return str1
    # print(tuplex[-4])
    # return tuplex[4]

    # most common element in tuplex

    # checking whether element exists - in can be used
    lst = list(tuplex)
    return lst


print(tuple_ex())
