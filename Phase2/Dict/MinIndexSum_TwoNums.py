from collections import defaultdict
def findRestaurant(list1, list2):
        dict1,dict2 = {}, defaultdict(list)
        if not list1 and not list2:
            return []
        min_val = float('inf')
        for i,n in enumerate(list1):
            dict1[n]=i
        for i,n in enumerate(list2):
            if n in dict1 and (dict1[n]+i)<=min_val:
                min_val = dict1[n]+i
                dict2[min_val].append(n)
        return dict2[min_val]

list1 = ["Shogun","Tapioca Express","Burger King","KFC"]
list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
print(findRestaurant(list1,list2))