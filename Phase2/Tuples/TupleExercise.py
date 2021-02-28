# Tuple
tuples = 5, 10, 15, 20, 25
# tuple unpacking
item1, item2, item3 = tuples[0], tuples[1], tuples[2]
item1, item2, item3, item4, item5 = tuples
# print(item1, item2, item3,item4,item5)
import operator

# add item to tuple
tuplex = (4, 5, 6, 7, 8, 9)
# tuplex+=(3,)
# print(tuplex)
tuplex = tuplex[:2] + (1, 2, 3) + tuplex[2:]
# print(tuplex)
# sort a list of tuples
lst = [("item1", "12.20"), ("item2", "35.10"), ("item3", "24.5")]
lst2 = []
# print(sorted(lst,key=lambda x:x[1],reverse=True))
for item in lst:
    item2 = tuple(list(item[:-1]), 100)
    lst2.append(item2)
print(lst2)
