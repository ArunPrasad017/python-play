# in this case all the items in the list are unique
def max_idx(lst):
    max_index,max_val = 0,lst[0]
    for i in range(1,len(lst)):
        if lst[i]>lst[i-1] and max_val<lst[i]:
            max_val=lst[i]
            max_index=i
    return max_index

def find_second_maximum(lst):
    # Write your code here
    temp=max_idx(lst)
    lst.pop(temp)
    return lst[max_idx(lst)]

# print(find_second_maximum([4, 2, 1, 5, 0]))
# print(find_second_maximum([1,2,4,4]))

# in this case all the items in the list are not unique
def secondMax(lst):
    first_max, second_max = float('-inf'),float('-inf')
    for i in range(len(lst)):
        if lst[i]>first_max:
            first_max=lst[i]
    for i in range(len(lst)):
        if lst[i]>second_max and lst[i]<first_max:
            second_max=lst[i]
    return second_max

# print(secondMax([1,2,3,3]))

# improve by one pass
def secondMax_one_time(lst):
    first_max, second_max = float('-inf'),float('-inf')
    for i in range(len(lst)):
        if lst[i]>first_max:
            second_max = first_max
            first_max=lst[i]
        elif lst[i]>second_max and lst[i]!=first_max:
            second_max=lst[i]
    if second_max==float('-inf'):
        return None
    else:
        return second_max

print(secondMax_one_time([1,2,3,3]))