def getRow(rowIndex):
    lst = []
    for i in range(rowIndex+1):
        temp_lst = []
        for j in range(i+1):
            if j in [0, i]:
                temp_lst.append(1)
            else:
                temp_lst.append(lst[i-1][j-1]+ lst[i-1][j])
            j+=1
        lst.append(temp_lst)
        i+=1
    return lst[rowIndex]

def getRowN(rowIndex):
    res = [1] * (rowIndex+1)
    for i in range(1, rowIndex):
        for j in range(i,0,-1):
            res[j]+=res[j-1]
    return res


k = 3
print(getRowN(k))