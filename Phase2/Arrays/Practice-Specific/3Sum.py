def twoSum(lst,i,res):
    l,r = i+1, len(lst)-1
    while l<r:
        sumVal = lst[i]+lst[l]+lst[r]
        if sumVal==0:
            res.append([lst[i],lst[l],lst[r]])
            l+=1
            r-=1
            while l<r and lst[l]==lst[l-1]:
                l+=1
        elif sumVal<0:
            l+=1
        else:
            r-=1

def threeSum(lst):
    res = []
    if lst is None or len(lst)<3:
        return res
    lst.sort()
    for i in range(len(lst)):
        if lst[i]>0:
            break
        if i==0 or lst[i]!=lst[i-1]:
            twoSum(lst,i,res)
    return res

nums = [-1,0,2]
print(threeSum(nums))