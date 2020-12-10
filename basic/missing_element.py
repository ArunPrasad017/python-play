def finder(a1, a2):
    a1.sort()
    a2.sort()

    for i in range(0, len(a1)):
        if a1[i] != a2[i]:
            return a1[i]


# x = finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
# print(x)

# #Other solution
# def finder2(a1,a2):
#     a1.sort()
#     k = int(len(a1)/2) + 1

#     for i in range(0,len(a2)):
#         if a2[i] < a1[k]:
#             for j in range(0,k):
#                 if a1[j] != a2[i]:

#         else:
#             for j in


# x = finder2([1,2,3,4,5,6,7],[3,7,2,1,4,6])

import collections


def finder3(arr1, arr2):

    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1
    print(d)

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] = -1


y = finder3([1, 2, 3, 4, 5, 6, 7], [3, 7, 2, 1, 4, 6])
print(y)
