"""
quicksort
"""


def partition(arr, left, right):
    pivot = arr[left]
    low = left + 1
    high = right
    while True:
        while low <= high and arr[high] >= pivot:
            high -= 1
        while low <= high and arr[low] <= pivot:
            low += 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]  # swap operation
        else:
            break
    arr[left], arr[high] = arr[high], arr[left]
    return high


def quicksort(arr, left, right):
    if left >= right:
        return
    p = partition(arr, left, right)
    quicksort(arr, left, p - 1)
    quicksort(arr, p + 1, right)


lst = [10, 16, 8, 12, 15, 6, 3, 9, 5]
quicksort(lst, 0, len(lst) - 1)
print(lst)
