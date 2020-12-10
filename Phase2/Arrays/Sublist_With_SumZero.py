def sublist_sum_zero(lst):
    d = {}
    sumVal = 0
    for item in lst:
        sumVal += item
        if item == 0 or sumVal == 0 or d.get(sumVal) is not None:
            return True
        d[sumVal] = item
    return False


lst = [4, -7, 12, 9]
print(sublist_sum_zero(lst))
