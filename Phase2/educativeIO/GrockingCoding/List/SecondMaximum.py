def second_max_list(lst):
    if len(lst)<2:
        return 0
    max = second_max = float('-inf')
    for i in range(len(lst)):
        if lst[i]>max:
            second_max=max
            max=lst[i]
        elif lst[i]>second_max and lst[i]!=max:
            second_max = lst[i]
    if second_max==float('-inf'):
        return 0
    return second_max

lst = [1,2,4,4]
print(second_max_list(lst))