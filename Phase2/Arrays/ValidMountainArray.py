def validMountainArray(arr):
    i=0
    while i<len(arr)-1 and arr[i+1]>arr[i]:
        i+=1
    if i in [len(arr) - 1, 0]:
        return False
    while i<len(arr)-1 and arr[i+1]<arr[i]:
        i+=1
    return i==len(arr)-1

arr = [3,5,5]
print(validMountainArray(arr))
arr = [3,4,5,6,2,1]
print(validMountainArray(arr))