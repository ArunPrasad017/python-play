def checkIfExist(arr):
    dict1 = {c: i for i, c in enumerate(arr)}
    containZero = 0
    for num in arr:
        if num*2 in dict1 and num!=0:
            return True
        if num==0: containZero+=1
    return containZero>1

def validMountainArray(A):
    i = 0
    while i<len(A) and A[i+1]>A[i]:
        i+=1
    if i==len(A)-1 or i==0:
        return False
    while i<len(A) and A[i+1]<A[i]:
        i+=1
    return i==len(A)-1


lst = [3,5,5]
print(validMountainArray(lst))