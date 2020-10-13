import operator
#1 - sort dictionary as ascending and descending by value
def sorted_dict():
    dict1 = {'a':20, 'b':10, 'c':30}
    return dict(sorted(dict1.items(),key=operator.itemgetter(1)))

def sorted_dict_reverse():
    dict1 = {'a':20, 'b':10, 'c':30}
    return dict(sorted(dict1.items(),key=operator.itemgetter(1),reverse=True))

dict1 = {0: 10, 1: 20}
def add_key(dict1):
    dict1[2] = 30
    # or 
    # dict1.update({2:30})
    return dict1

def dict_append():
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50,6:60}
    dic4 ={}
    for d in dic1,dic2,dic3:
        dic4.update(d)
    return dic4

def dict_key_check(dict1,k):
    # actual - return True if k in dict1 else False
    return k in dict1

def dict1_sq(n):
    # dict1 = {}
    # for i in range(1,n+1):
    #     dict1[i] = i*i
    # return dict1
    return {i: i*i for i in range(1,n+1)}

def remove_key_from_dict(dict1, x):
    if x in dict1:
        del dict1[x]
    return dict1

def map_two_list_dict(l1,l2):
    return dict(zip(l1,l2))

def max_min_dict():
    dic1={1:10, 2:20}
    return (max(dict1.values()), min(dict1.values()))

# combine two dicts
from collections import Counter
def combine(d1,d2):
    return dict(Counter(d1)+Counter(d2))

def combine_list_dict(lst):
     # [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    res = Counter()
    for d in lst:
        res[d['item']] += d['amount']
    return res

#python dictionary as a table (Could be useful)
def dict_to_table(dict1):
    for row in zip(*([key]+value for key,value in dict1.items())):
        print(*row)

# count the values associated with key in dict - success:'True'
def count(lst):
    # cntr = 0
    # for item in list:
    #     if 'success' in item.keys() and item['success'] == True:
    #         cntr+=1
    # return cntr
    return sum(
        1
        for item in lst
        if 'success' in item.keys() and item['success'] == True
    )

# create an nested dictionary from the keys
# def lst_to_nested_dict(lst):
#     res_dict = current = {}
#     for item in lst:
#         current[item] = {}
#         current = current[item]
#     return res_dict
# lst = [1,2,3,4]
# print(lst_to_nested_dict(lst))

# sort a dict based on values
# dict1 = {'b':100, 'c':200, 'f':1000, 'd':100,'a':1000}
# dict2 = dict(sorted(dict1.items(),key=operator.itemgetter(1)))
# # dict2 = {x: sorted(y) for x,y in dict1.items()}
# print(dict2)

# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x:sorted(y) for x,y in num.items()}
# print(sorted_dict)

# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# dict_student = {}
# for k,v in student_list.items():
#     new_key = k.replace(' ','')
#     dict_student[new_key] = v
# print(dict_student)

# import heapq
# items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# for name in (heapq.nlargest(3,items,key=items.get)):
#     print(name, items[name])

# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# count = 0
# for k,v in dict_num.items():
#     count+=1
#     print(str(k)+'->'+ str(v) + '->'+str(count))

# above same as here
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for count, (k, v) in enumerate(dict_num.items(), start=1):
#     print(str(k)+'->'+ str(v) + '->'+str(count))

# from collections import Counter
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# new_dict = Counter(dict_num)
# print(new_dict.most_common())

# # 
# dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# avg = (sum(dict_num.values()) / len(dict_num))
# for k,v in dict_num.items():
#     dict_num[k]=avg
# print(dict_num)

from collections import defaultdict
d= defaultdict(list)
for i,c in enumerate(list('xyz')):
    n = (i+1)*10
    d[c] = [n+i for i in range(1,10)]
print(dict(d))
for k, v in d.items():
    print(v[4])
for k, v in d.items():
    print("{} has value {}".format(k,v))

    


##################################################################################################################################
#####function calls
# print(sorted_dict())
# print(sorted_dict_reverse())
# print(add_key(dict1))
# print(dict_append())

# print(dict_key_check(dict1,1))
# print(dict_key_check(dict1,3))
# print(dict1_sq(15))
# dict1 = {'a':10, 'b':30, 'c':20}
# print(remove_key_from_dict(dict1,'a'))
# l1 = ['Blue','Black']
# l2 = [1,2]
# print(map_two_list_dict(l1,l2))

# print(max_min_dict())

# d1 = {'a':100, 'b':200}
# d2 = {'b':100, 'a':300, 'c':900, 'd':900}
# # print(combine(d1,d2))
# print(set(d2.values()))

# # highest 3 - use the heapq nlargest function
# lst = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# print(combine_list_dict(lst))

# string = 'W3Resource'
# print(dict(Counter(string)))

# dict1 = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# print(dict_to_table(dict1))


# lst = [{'id': 1, 'success': True, 'name': 'Lary'}, 
#         {'id': 2, 'success': False, 'name': 'Rabi'}, 
#         {'id': 3, 'success': True, 'name': 'Alex'}]

# print(count(lst))

# set operation refreshers
new_set1 = set([3,4,5,6])
new_set2 = set([1,2,3,4])
print(new_set1.intersection(new_set2))
print(new_set1.union(new_set2))
print(new_set1.symmetric_difference(new_set2))
print(new_set1.difference(new_set2))
print(new_set1.issubset(new_set2))
print(max(new_set1))
print(new_set1.isdisjoint(new_set2))
print("\n")
set1 = set2 = set()
set1.add(1)
print(set1)
print(set2)
# clear all
set1.clear()
print("\n")
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])
print(x.issubset(y))
print(x.isdisjoint(y))
print(x.symmetric_difference(y))
