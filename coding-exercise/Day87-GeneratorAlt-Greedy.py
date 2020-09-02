def rev_str(my_array):
    length = len(my_array)
    for i in range(length):
        if my_array[i] is None:
            my_array[i] = my_array[i-1]
        yield my_array[i]
array1 = [1,None,2,3,None,None,5,None]
# print(list(rev_str(array1)))

def greedy_test(arr):
    for i in range(1,len(arr)):
        if arr[i] is None:
            arr[i] = arr[i-1]
    return arr
print(greedy_test(array1))