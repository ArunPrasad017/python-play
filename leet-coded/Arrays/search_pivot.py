def search_pivot(list1):
    Sum_val =  sum(list1)
    leftsum = 0

    for i, x in enumerate(list1):
        if leftsum == (Sum_val - leftsum - x):
            return i
        leftsum+=x
    return -1

list1=[1, 7, 3, 6, 5, 6]
print(search_pivot(list1))