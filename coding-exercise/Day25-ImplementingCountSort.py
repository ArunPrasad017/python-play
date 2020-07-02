def countSort(arr): 
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    res = [0 for _ in arr]
    
    for i in arr:
        count[ord(str(i))]+=1

    for i in range(256):
        count[i]+= count[i-1]
    
    for i in range(len(arr)):
        output[count[ord(str(arr[i]))]-1] = arr[i]
        count[ord(str(arr[i]))]-=1
    
    for i in range(len(arr)):
        res[i] = output[i]
    
    return res


arr = [1, 4, 1, 2, 7, 5, 2]
print(countSort(arr))