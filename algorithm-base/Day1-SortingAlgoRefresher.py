"""
Algo modules + algo visualizer links
Sorting refresher
1. Bubble sort
2. 
"""
#################################################################################
# bubble Sort - brute force
def swap(lst,a,b):
    temp = lst[a]
    lst[a] = lst[b]
    lst[b] = temp

def bubbleSort(lst):
    isSorted = False
    lastUnsorted = len(lst)-1
    while not isSorted:
        isSorted = True
        for i in range(lastUnsorted):
            if lst[i] > lst[i+1]:
                swap(lst,i,i+1)
                isSorted = False
        lastUnsorted -=1
    return lst

lst = [6,5,4,3,2,1]
# print(bubbleSort(lst))
#################################################################################

# Merge Sort - Divide and Conquer
# https://algorithm-visualizer.org/divide-and-conquer/merge-sort
def mergeHalves(left, right):
    left_idx, right_idx = 0,0
    res = []
    while left_idx<len(left) and right_idx<len(right):
        if left[left_idx]<right[right_idx]:
            res.append(left[left_idx])
            left_idx+=1
        else:
            res.append(right[right_idx])
            right_idx+=1
    res+=left[left_idx:]
    res+=right[right_idx:]
    return res

def mergeSort(lst):
    if len(lst)<=1:
        return lst
    mid = len(lst)//2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])
    return mergeHalves(left, right)
    
print(mergeSort(lst))