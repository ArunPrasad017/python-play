# # o(n^2) implementation
# def find_product(lst):
#     # Write your code here
#     res=[]
#     for i in range(len(lst)):
#         temp =1
#         for j in range(len(lst)):
#             if i==j:
#                 continue
#             else:
#                 temp *= lst[j]
#         res.append(temp)
#     return res

# o(n) implementation
# def find_product(lst):
#     res =[]
#     left,right = [1]*len(lst), [1]*len(lst)
#     for i in range(1,len(lst)):
#         left[i] = left[i-1]*lst[i-1]
#     for i in range(len(lst)-1,-1,-1):
#         if i==len(lst)-1:
#             right[i]=1
#         else:
#             right[i] = right[i+1]*lst[i+1]
#     res =[]
#     for i,j in zip(left,right):
#         res.append(i*j)
#     return res

def find_product(lst):
    res=[]
    left = 1
    for item in lst:
        res.append(left)
        left *= item
    right=1
    for i in range(len(lst)-1,-1,-1):
        res[i] = res[i]*right
        right *= lst[i]
    return res
    
lst=[1,2,3,4]
print(find_product(lst))