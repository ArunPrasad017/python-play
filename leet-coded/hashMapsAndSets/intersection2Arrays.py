def arraysIntersection(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    return list(set1 & set2)