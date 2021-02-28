def replaceElements(arr):
    if len(arr) == 1:
        return [-1]
    for i in range(len(arr)):
        if i != len(arr) - 1:
            arr[i] = max(arr[i + 1 :])
    arr[len(arr) - 1] = -1
    return arr
