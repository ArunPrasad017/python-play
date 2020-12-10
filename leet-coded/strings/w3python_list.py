import itertools


def listfunction():
    # Prog1
    list1 = [1, 2, 4]
    # sum_val = 0
    # for i in list:
    #     sum_val+=i
    # return sum_val

    # prog5
    # sample = ['abc', 'xyz', 'aba', '1221']
    # ctr = 0
    # for word in sample:
    #     if len(word)>1 and word[0]==word[-1]:
    #         ctr+=1
    # return ctr

    # Prog6:
    # Get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
    # n = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    # def last(n):
    #     return n[-1]
    # sorted_list = sorted(n,key=last)
    # return sorted_list

    # prog7
    # remove duplicate
    # a = [10,20,30,20,10,50,60,40,80,50,40]
    # a = list(sorted(set(a)))
    # return a

    # Prog 8:
    # Is list empty
    # list1 =[]
    # if not list1:
    #     return "Empty"

    # Prog 9:
    ### Clone or copy list
    # list2 = list(list1)
    # print(list1,list2)

    # Prog 10:
    ## using list comprehension
    # n = 5
    # list2 = ['Hey','Hello','Meelo']
    # list2 = [x for x in list2 if len(x)>=n]
    # return list2

    # lst1 = [1,2,3,4,5]
    # lst2 = [5,6,7,8]
    # set1 = set(lst1)
    # set2 = set(lst2)
    # return list(set1.symmetric_difference(set2))
    # # return str(set(lst1) - set(lst2)) + str(set(lst2) - set(lst1))

    # prog 12
    ## for in place deletion in list use the list comprehension
    # Sample = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yello']
    # Sample = [x for i,x in enumerate(Sample) if i not in [0,4,5] ]
    # return Sample

    # Prog 14
    ## remove even numbers
    # lst1 = [1,2,3,4,5,6]
    # lst1 = [x for x in lst1 if x%2!=0]
    # return lst1

    # Prog 16
    # lst1 = [1,4,9,16,25,36,49.64,81,100,121,144,169,196,225,256,289,324,361,400]
    # lst1 = [x for i,x in enumerate(lst1) if i not in range(5,14)]
    # return lst1

    # Prog 20:
    ## use enumerate

    # Prog21:
    # Sample = ['R', 'e', 'e', 'l']
    # return ''.join(Sample)
    # string = "This is Arun How are you doing"
    # lst1 = string.split()
    # return lst1

    # Prog 28:
    # lst1 = [1,121,144,169,196,225,256,289,324,361,400,225,121,256,4,9,16,25,36,49.64,81,100]
    # set1 = set()
    # uniq_lst1 = []
    # for i in lst1:
    #     if i not in set1:
    #         uniq_lst1.append(i)
    #         set1.add(i)
    # return(sorted(uniq_lst1)[8])

    # Prog number 34 to be started with
    # sieve of Eratosthenes
    # import math
    # n = 20
    # primes =[]
    # for i in range(2,n+1):
    #     primes.append(i)

    # j = 2
    # while (j <= int(math.sqrt(n))):
    #     if j in primes:
    #         for k in range(j*2,n+1,j):
    #             if k in primes:
    #                 primes.remove(k)
    #     j+=1
    # return primes

    # 35
    ## String formatting with list comprehension
    # my_list = ['p','q']
    # n=4
    # new_list = ['{}{}'.format(x,y) for y in range(1,n+1) for x in my_list]
    # return new_list

    # 37
    ## Common elements between 2 lists
    # list1 = [2,3,4,5,6]
    # list2 = [1,2,3,9,0]
    # return (set(list1) & set(list2))

    # 38
    # lst = [0,1,2,3,4,5]
    # n = len(lst)
    # for i in range(0,n-1,2):
    #     temp = lst[i]
    #     lst[i] = lst[i+1]
    #     lst[i+1] = temp
    # return lst

    # 39:
    ##  list of multiple integers into a single integer.
    # sample_lst = [11,33,50]
    # sample2 = "".join(map(str,sample_lst))
    # return sample2

    # 40:
    ## split list based on first character
    # done using itertools(operator) and opertor(itemgetter)

    # 42
    # lst1 = ['a','b','c','d','e','f']
    # lst2 = ['d','e','f','g','h']
    # return set(lst1)-set(lst2), set(lst2)-set(lst1)

    # 44 - groups of 5
    # l = [[5*i + j for j in range(1,6)] for i in range(5)]
    # return l

    # # 45 - convert list of tuples to unique set
    # L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
    # S = sorted(set().union(*L)) # * indicates space separated values in a list
    # return S

    # 46
    # only odd
    # l = [1,2,3,4,5,6,7]
    # l = [x for i,x in enumerate(l) if i%2==0]
    # return l

    # 47
    # insert an element before each element of a list
    # l = [1,2,3,4,5,6,7]
    # l = [v for i in l for v in ('c',i)]
    # return l

    # 48
    # colors = [['Red'], ['Green'], ['Black']]
    # colors = '\n'.join( [str(lst) for lst in colors])
    # return colors

    # 49
    # ## list to dict - use the zip method
    # color_name = ["Black", "Red", "Maroon", "Yellow"]
    # color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
    # #method 1
    # #return ([{'color_name':i , 'color_code':j} for i,j in zip(color_name,color_code)])
    # #method  2 :
    # ## using dict comprehension - having key:val from two lists
    # res = {color_name[i]:color_code[i] for i in range(len(color_name))}
    # return res

    # 50 - TBD
    # my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
    # sort_list =  my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
    # return sort_list

    # 51 - Slice list based on n value
    # step = 3
    # C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

    # return [C[i::step] for i in range(step)]

    # 52
    # lst1 = ["red", "orange", "green", "blue", "white"]
    # lst2 = ["black", "yellow", "green", "blue"]
    # return list(set(lst1) - set(lst2)), list(set(lst2) - set(lst1))

    # 54 - for using the concatenation of list element together
    # ''.join(lst)

    # 56 - str.split()
    # str1 =  'Hello Geeks for geeks'
    # return str1.split(' ')
    ## try2 - with special characters
    # str2 = "They're going! up to the Stark's , castle"
    # import re
    # return re.findall(r"[A-Za-z@#]+|\S", str2)

    # 57 - all same
    # color1 = ["green", "orange", "black", "white"]
    # color2 = ["green", "green", "green", "green"]
    # def same_color(lst):
    #     if len(set(lst))==1:
    #         return True
    #     return False
    # print(same_color(color1))
    # print(same_color(color2))

    # 59
    n = 2
    # color1 = ["green", "orange", "black", "white"]
    # if n<=len(color1):
    #     return True
    # else: return False
    # 60: not able to understand
    # 64 - using zip (helps to iterate two of the lists at same time)
    # color1 = ["green", "orange", "black", "white"]
    # C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    # from itertools import cycle
    # # for (a,b) in zip(C,color1):
    #     print(a,b)
    # use cycle for not same lists
    # for (a,b) in zip(C,cycle(color1)):
    #     print(a,b)

    # 65 - dictionary key
    # num = {'physics': 80, 'math': 90, 'chemistry': 86}
    # return list(num)[0]

    # # 66 - list in a list of lists whose sum of elements is the highest
    # lst1 = [ [1,2,3], [4,5,6], [10,11,12], [7,8,9]]
    # return max(lst1, key=sum)

    # 67
    # lst1 = [1,2,3,4,5,6]
    # n = 2
    # lst1 = [x for x in lst1 if x>= n]
    # return lst1

    # 68
    # lst1 = [1,2,3,4,5,6]
    # lst2 = [0,0]
    # lst2.extend(lst1)
    # return lst2

    # 69 - remove duplicates (not working)
    # lst1 = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    # num = lst1.sort()
    # new_lst = list(num for num,_ in itertools.groupby(num))
    # return new_lst

    # 70 depth of dictionary - using the string and then finding the number of open braces

    # 71 - check whether all dictionaries in a list are empty or not
    # lst1 = [{},{},{1}]
    # count = 0
    # for val in lst1:
    #     if len(val):
    #         return False
    #     else:
    #         count+=1
    # return count == len(lst1)

    # 73:
    ## remove consecutive duplicates of a given list
    # n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ]
    # n_list = [key for key, group in itertools.groupby(n_list)]
    # return n_list

    # 75, 76 - run-length encoding
    # can be used to create dict
    n_list = [1, 1, 2, 3, 4, 4.3, 5, 1]

    x = [[len(list(group)), key] for key, group in itertools.groupby(n_list)]
    return x


print(listfunction())
