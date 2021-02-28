def twoSum(lst,i,res):
    target = -1*(lst[i])
    l,r=i+1,len(lst)-1
    temp_res =[]
    while l<r:
        mid=lst[l]+lst[r]
        if mid==target:
            temp_res.append(-1*target)
            temp_res.append(lst[l])
            temp_res.append(lst[r])
            return temp_res
        elif mid>target:
            r-=1
        else:
            l+=1


def threeSum(lst):
    res = []
    if lst is None or len(lst)<3:
        return res
    lst.sort()
    if lst[0]>0:
        return res
    for i in range(len(lst)):
        if lst[i]>0:
            break
        s = twoSum(lst,i,res)
        if s is not None:
            res.append(s)
    return res

lst = [-1,0,1,2,-1,-4]
print(threeSum(lst))