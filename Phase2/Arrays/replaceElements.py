def replaceElements(arr):
    maxVal=0
    for i in range(len(arr)):
        if i+1<len(arr):
            maxVal=max(arr[i+1:len(arr)])
            arr[i] = maxVal
        else:
            arr[i]=-1
    return arr

arr= [17,18,5,4,6,1]
print(replaceElements(arr))