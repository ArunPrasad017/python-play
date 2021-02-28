def binarySearch(sorted_lst,x, n):
    if sorted_lst[n-1][0][0] < x:
        return -1
    l,h= 0,n-1
    while l<=h:
        mid = l+(h-l)//2
        if sorted_lst[mid][0][0]>=x:
            h=mid-1
        else:
            l=mid+1
    return sorted_lst[l][1]

def findRightInterval(lst):
    n = len(lst)
    if n==1:
        return [-1]
    res = [0]*n
    sorted_lst = sorted([[c,i] for i,c in enumerate(lst)], key=lambda x:x[0][0])
    for i in range(n):
        res[i] = binarySearch(sorted_lst, lst[i][1],n)
    return res

lst = [ [1,4], [2,3], [3,4] ]
print(findRightInterval(lst))