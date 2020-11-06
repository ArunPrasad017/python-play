# brute force - initial logic
# def findClosestElements(arr,k,x):
#     if k==len(arr):
#         return arr 
#     res =[]
#     idx = 0
#     left,right = 0,len(arr)-1
#     while left<right:
#         mid = left+(right-left)//2
#         if arr[mid]==x:
#             res.append(arr[mid])
#             idx=mid
#             break
#         elif arr[mid]<x:
#             left=mid
#         else:
#             right=mid
#     if idx:
#         for i in range(k):
#             if i!=idx:
#                 res.append(arr[i])
#     else:
#         for i in range(k):
#             res.append(arr[i])
#     return sorted(res)

def findClosestElements(arr,k,x):
    if k==len(arr):
        return arr
    l,h=0,len(arr)-k
    while l<h:
        mid = l+(h-l)//2
        if x<=arr[mid]:
            h=mid
        elif x>=arr[mid+k]:
            l=mid+1
        else:
            x_dist_from_mid = abs(x-arr[mid])
            x_dist_from_k=abs(x-arr[mid+k])
            if x_dist_from_mid<=x_dist_from_k:
                h=mid
            else:
                l=mid+1
    return arr[l:l+k]

arr = [0,1,1,1,2,3,6,7,8,9]
k = 9
x = 4
print(findClosestElements(arr,k,x))