# def selection_sort(arr):

#     for fillslot in range(len(arr)-1,0,-1):
#         posMax = 0
#         for loc in range(1,fillslot+1):
#             if arr[loc]>arr[posMax]:
#                 posMax = loc
#         temp = arr[fillslot]
#         arr[fillslot] = arr[posMax]
#         arr[posMax] = temp

# arr = [2,1,6,3,5]
# selection_sort(arr)
# print(arr)

# def insertion_sort(arr):
#     for i in range(1,len(arr)):
#         curr_val = arr[i]
#         pos = i

#         while pos > 0 and arr[pos-1]>curr_val:
#             arr[pos] = arr[pos-1]
#             pos =pos-1
#         arr[pos] = curr_val

# arr = [2,1,6,3,5]
# insertion_sort(arr)
# print(arr)

# shell sort
# def shell_sort(arr):
#     sublistcount =len(arr)//2

#     while sublistcount>0:
#         for start in range(sublistcount):
#             gap_insertion_sort(arr,start,sublistcount)
#         sublistcount =sublistcount//2

# def gap_insertion_sort(arr,start,gap):
#     for i in range(start+gap, len(arr),gap):
#         current_val = arr[i]
#         pos = i

#         while pos>=gap and arr[pos-gap] > current_val:
#             arr[pos] = arr[pos-gap]
#             pos = pos-gap
#         arr[pos] = current_val

# arr2 = [2,1,6,3,5]
# shell_sort(arr2)
# arr2


# def merge_sort(arr):
#     if len(arr)>1:
#         mid = len(arr)//2
#         left_half = arr[:mid]
#         right_half = arr[mid:]

#         merge_sort(left_half)
#         merge_sort(right_half)

#         i = 0
#         j = 0
#         k = 0

#         while(i<len(left_half) and j<len(right_half)):
#             if left_half[i] < right_half[j]:
#                 arr[k] = left_half[i]

#                 i+=1
#             else:
#                 arr[k] = right_half[j]
#                 j+=1
#             k+=1

#         while(i<len(left_half)):
#             arr[k] = left_half[i]
#             i+=1
#             k+=1

#         while(j<len(right_half)):
#             arr[k] = right_half[j]
#             j+=1
#             k+=1

# arr2 = [2,1,6,3,5,9]
# merge_sort(arr2)
# print(arr2)


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point + 1, last)


def partition(arr, first, last):
    pivot = arr[first]
    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot:
            leftmark += 1
        while arr[rightmark] >= pivot and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


arr8 = [5, 8, 9, 1, 2]
quick_sort(arr8)
print(arr8)
