def threeSumClosest(lst, target):
    if not lst or len(lst)<3:
        return None
    minRes = float('inf')
    lst.sort()
    for i in range(len(lst)):
        l = i+1
        r = len(lst)-1
        while l<r:
            sumVal = lst[i]+lst[l]+lst[r]
            if sumVal == target:
                minRes =0
                break
            elif abs(target-sumVal)<abs(minRes):
                minRes = target-sumVal
            if sumVal<target:
                l+=1
            else:
                r-=1
        if minRes==0:
            break
    return target-minRes

nums = [-1,2,1,-4]
tgt = 1
print(threeSumClosest(nums,tgt))