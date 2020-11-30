def sublist_sum_zero(lst):
    d = {}
    total_sum = 0
    for item in lst:
        total_sum+=item
        if item==0 or total_sum==0 or d.get(total_sum) is not None:
            return True
        d[total_sum]=item
    return False

lst = [4,-7,3,12,9]
sublist_sum_zero(lst)
