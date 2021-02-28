def arraysIntersection(arr1, arr2, arr3):
    set1 = set(arr1)
    set2 = set(arr2)
    set3 = set(arr3)

    return sorted(list(set1 & set2 & set3))
