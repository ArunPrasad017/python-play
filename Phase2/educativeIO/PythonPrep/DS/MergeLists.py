# # o(n) extra space
# def merge_lists(lst1, lst2):
#     # Write your code here
#     ptr1,ptr2 = 0,0
#     res=[]
#     while lst1 and lst2:
#         if lst1[ptr1]<=lst2[ptr2]:
#             res.append(lst1[ptr1])
#             lst1.pop(0)
#         else:
#             res.append(lst2[ptr2])
#             lst2.pop(0)
#     if lst1 or lst2:
#         res.extend(lst1)
#         res.extend(lst2)
#     return res

# merge without extra space
def merge_no_extra_space(lst1,lst2):
    ptr1,ptr2 = 0,0
    while ptr1<len(lst1) and ptr2<len(lst2):
        if lst1[ptr1]>lst2[ptr2]:
            lst1.insert(ptr1,lst2[ptr2])
            ptr2+=1
        ptr1+=1
    if lst2:
        lst1.extend(lst2[ptr2:])
    return lst1


lst1 = [1,3,4,5]  
lst2 = [2,6,7,8]
print(merge_no_extra_space(lst1,lst2))