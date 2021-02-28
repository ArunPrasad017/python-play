# initial code without consideration of the cases
# def merge(l):
#     if len(l)<=1:
#         return l
#     l.sort(key = lambda x:x[0])
#     lst2 =[]
#     cnt =1
#     for i in range(len(l)-1):
#         if l[i][1] >=l[i+1][0] and l[i][1] <= l[i+1][1]:
#             lst2.append([l[i][0], l[i+1][1]])
#             cnt+=1
#         elif l[i][1] >=l[i+1][0] and l[i][1] > l[i+1][1]:
#             lst2.append([l[i][0], l[i+1][1]])
#             cnt+=1
#     if cnt>1:
#         return lst2+l[cnt:]
#     return l


def merge(l):
    if len(l) <= 1:
        return l
    l.sort(key=lambda x: x[0])
    i = 1
    while i < len(l):
        if l[i][0] <= l[i - 1][1]:
            l[i - 1][0] = min(l[i][0], l[i - 1][0])
            l[i - 1][1] = max(l[i][1], l[i - 1][1])
            l.pop(i)
        else:
            i += 1
    return l


# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1, 4], [0, 2], [3, 5]]
print(merge(intervals))
