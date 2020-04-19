import operator
def dict_test():
    # 1. to sort (ascending and descending) a dictionary by value
    # dict1 = {1: 20, 2: 30,0: 10}
    # dict2 = dict(sorted(dict1.items(), key = operator.itemgetter(1)))
    # dict3 = dict(sorted(dict1.items(), key = operator.itemgetter(1),reverse=True))
    # return dict2,dict3

    # # 2. add to dict
    # dict1 = {1: 20, 2: 30,0: 10}
    # dict1[3] = 60
    # return dict1

    # 3 - update doesn't work for dict creation
    # it nees dict to be created first
    # dic1={1:10, 2:20}
    # dic2={3:30, 4:40}
    # dic3={5:50,6:60}
    # dic_final = {}
    # for d in (dic1,dic2,dic3):
    #     dic_final.update(d)
    # return dic_final

    # 4 - 
    # dic1={1:10, 2:20}
    # n =1
    # if n in dic1.keys():
    #     return True

    # 5 - using for
    # dic1={1:10, 2:20}
    # for k, v in dic1.items():
    #     print('Key = {} and value = {}'.format(k,v))

    # #10
    # dic1={1:10, 2:20}
    # return sum(dic1.values())

    # del command is to delete the elements from the dict based on key

    # # using dict comprehension
    # color_name = ["Black", "Red", "Maroon", "Yellow"]
    # color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    # dict1 = {color_name[i]:color_code[i] for i in range(0,len(color_name))}
    # return dict1

    ## sort dictionary by key
    # color_dict = {'red':'#FF0000',
    #       'green':'#008000',
    #       'black':'#000000',
    #       'white':'#FFFFFF'}
    # new_dict = {}
    # for key in sorted(color_dict.keys()):
    #     new_dict[key] = color_dict[key]
    # return new_dict

    # # 15 - max val and min val
    # my_dict = {'x':500, 'y':5874, 'z': 560}
    # max_val = max(my_dict.keys(), key= lambda k:my_dict[k])
    # min_val = min(my_dict.keys(), key= lambda k:my_dict[k])
    # return max_val, min_val

    # 17 - duplicates in dict
    # iterate thru the K,V pairs and find if values 
    # are already present in the new dict you created

    #18 - dict is empty
    # dict1 = {}
    # if not dict1:
    #     return True

    #19 - 

    #20:
    # lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
    # set_dict = set()

    # for val in lst:
    #     for k,v in val.items():
    #         if v not in set_dict:
    #             set_dict.add(v)
    # return set_dict

    #22 - Write a Python program to find the highest 3 values in a dictionary.
    # from heapq import nlargest
    # my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}  
    # l = nlargest(3,my_dict, key=my_dict.get)
    # return l

    #23 - combine from list
    # from collections import Counter
    # lst1 = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
    # result = Counter()
    # for d in lst1:
    #     result[d['item']] = d['amount']
    # return result

    # 24 -  count the letters
    # from collections import Counter
    # str1 = 'w3resource'
    # result = Counter(str1)
    # return result

    #25 related to print

    #26 - scan through element in list 1 by 1 
    # and see the value in dic.items() by matching the key

    #27 - list into a nested dictionary of keys.
    # lst = [1,2,3,4]
    # d = current ={}
    # for i in lst:
    #     current[i] = {}
    #     current = current[i]
    # return current

    #dict to be done (last 10)
    # enumerate()

print(dict_test())